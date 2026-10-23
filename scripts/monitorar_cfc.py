# Compara as páginas de normas do CFC com o índice (normas.json) e aponta:
#  - norma nova: código que o CFC lista e o índice não tem
#  - nova revisão: o CFC lista uma revisão (Rn) diferente da do índice
# Saída: verificacao/MONITOR.md. Sai com código 1 quando há novidade (o GitHub Actions abre uma issue).
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verificar_links import baixar, texto  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/"
PAGINAS = ["normas-completas", "normas-simplificadas-para-pmes", "normas-especificas", "nbc-tsp-do-setor-publico",
           "nbc-ta-de-auditoria-independente", "nbc-tr-de-revisao", "nbc-to-de-asseguracao",
           "nbc-tsc-de-servico-correlato", "nbc-ti-de-auditoria-interna", "nbc-tp-de-pericia",
           "nbc-tds-de-sustentabilidade", "nbc-pg-geral", "nbc-pa-do-auditor-independente", "nbc-pp-do-perito-contabil"]
CODIGO = re.compile(r"\b(?:NBC (?:TG|TA|TSP|TR|TO|TSC|TI|TP|TDS|TAS|PG|PA|PP|PO)|ITG|CTG|OTG|CTSP|CTR|CTO|CTSC|ITP)"
                    r" ?(?:Estrutura Conceitual|\d+)(?: ?\(R\d+\))?")
# códigos que aparecem nas páginas só como citação dentro do título de outra norma,
# ou com erro de digitação do próprio site ("NBC TO 34 10" = NBC TO 3410)
IGNORAR = {"ITG 02", "CTG 02", "NBC TO 34"}


def separa(c):
    c = re.sub(r"\s*\(", " (", c.strip())
    m = re.match(r"(.*?)(?: \((R\d+)\))?$", c)
    return m.group(1), (m.group(2) or "")


def main():
    normas = json.loads((ROOT / "normas.json").read_text(encoding="utf-8"))["normas"]
    nosso = {}
    for r in normas:
        base, rev = separa(r["codigo"])
        nosso[base] = rev
    achados, falhas = {}, []
    for p in PAGINAS:
        st, _, corpo = baixar(BASE + p + "/")
        if st != 200:
            falhas.append(p); continue
        t, _ = texto(corpo)
        for c in CODIGO.findall(t):
            base, rev = separa(c)
            if base in IGNORAR:
                continue
            if rev > achados.get(base, ("", ""))[0]:
                achados[base] = (rev, p)
            else:
                achados.setdefault(base, (rev, p))
    novas = sorted(b for b in achados if b not in nosso)
    revis = sorted(b for b, (rev, _) in achados.items() if b in nosso and rev and rev != nosso[b]
                   and int(rev[1:]) > int(nosso[b][1:] or 0))
    md = ["# Monitor de normas do CFC\n",
          "Gerado por `scripts/monitorar_cfc.py`: compara as páginas de normas do CFC com o `normas.json`.\n"]
    if falhas:
        md.append("Páginas que não abriram: " + ", ".join(falhas) + "\n")
    md.append("## Normas que o CFC lista e o índice não tem\n")
    md += [f"- {b}{' (' + achados[b][0] + ')' if achados[b][0] else ''} — página `{achados[b][1]}`" for b in novas] or ["Nenhuma."]
    md.append("\n## Revisões mais novas no CFC\n")
    md += [f"- {b}: índice tem ({nosso[b] or 'sem R'}), CFC lista ({achados[b][0]})" for b in revis] or ["Nenhuma."]
    (ROOT / "verificacao").mkdir(exist_ok=True)
    (ROOT / "verificacao" / "MONITOR.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("novas:", novas, "| revisões:", revis, "| falhas:", falhas)
    sys.exit(1 if novas or revis else 0)


if __name__ == "__main__":
    main()
