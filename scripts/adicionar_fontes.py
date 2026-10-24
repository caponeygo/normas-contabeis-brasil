# Acrescenta (ou atualiza) uma seção "Fontes" no fim de cada arquivo de conteúdo, com o link oficial de toda
# norma (normas.json, CPC em scripts/cpc.json) e de toda lei/regra externa (dados/fontes_externas.csv) citada nele.
# Idempotente: o bloco fica entre <!-- fontes:inicio --> e <!-- fontes:fim --> e é refeito a cada execução.
# Rodar depois de scripts/gerar_indice.py (o rebuild_graph.py já faz isso).
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from dados import ler  # noqa: E402

INI, FIM = "<!-- fontes:inicio -->", "<!-- fontes:fim -->"
ALVOS = ["GLOSSARIO.md", "lancamentos/*.md", "areas/*.md", "setores/*/*.md"]
FORA = {"README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "dados/README.md", "verificacao", "testes"}


def sem_rev(c):
    return re.sub(r"\s*\(R\d+\)", "", c).strip()


# fontes: (regex, texto do link, url)
fontes = []
for n in json.loads((ROOT / "normas.json").read_text(encoding="utf-8"))["normas"]:
    if n["serie"] == "IFRS/IAS" and not n["codigo"].startswith(("IFRS", "IAS", "IFRIC", "SIC")):
        continue
    fontes.append((re.escape(sem_rev(n["codigo"])), f"{n['codigo']} – {n['titulo']}", n["url"]))
for c in json.loads((ROOT / "scripts" / "cpc.json").read_text(encoding="utf-8")):
    fontes.append((re.escape(sem_rev(c["codigo"])), f"{c['codigo']} – {c['titulo']}", c["url"]))
for e in ler("fontes_externas.csv"):
    fontes.append((e["padrao"], f"{e['codigo']} – {e['titulo']}", e["url"]))
compiladas = [(re.compile(r"(?<![\w.])(?:" + rx + r")(?![\d])"), txt, url) for rx, txt, url in fontes]


def bloco(texto):
    achados = []
    for rx, txt, url in compiladas:
        m = rx.search(texto)
        if m and url not in {u for _, _, u in achados}:
            achados.append((m.start(), txt, url))
    if not achados:
        return ""
    linhas = [f"- [{txt}]({url})" for _, txt, url in sorted(achados)]
    return (f"\n{INI}\n## Fontes\n\nTextos oficiais citados nesta página (os resumos e explicações foram elaborados para este "
            f"índice a partir deles; confira sempre a versão vigente):\n\n" + "\n".join(linhas) + f"\n{FIM}\n")


arquivos = []
for padrao in ALVOS:
    arquivos += [p for p in ROOT.glob(padrao) if p.is_file()]
total = 0
for p in sorted(set(arquivos)):
    rel = p.relative_to(ROOT).as_posix()
    if rel in FORA or rel.split("/")[0] in FORA or rel.startswith((".", "scripts/", "graphify-out/")):
        continue
    txt = p.read_text(encoding="utf-8")
    base = re.sub(r"\n?" + re.escape(INI) + r".*?" + re.escape(FIM) + r"\n?", "", txt, flags=re.S).rstrip("\n") + "\n"
    novo = base + bloco(base)
    if novo != txt:
        p.write_text(novo, encoding="utf-8")
    total += 1
print(f"Fontes atualizadas em {total} arquivos")
