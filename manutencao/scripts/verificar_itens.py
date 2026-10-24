# Confere o conteúdo do índice contra o texto oficial das normas (PDFs do CFC).
# 1) Cada trecho citado nas pastas de setor (campo "setores"): o item existe? o texto do item
#    trata do assunto descrito? (sobreposição de palavras-chave)
# 2) Cada resumo: as palavras-chave do resumo aparecem no texto da norma?
# Pré-requisitos: python scripts/verificar_links.py --baixar  (baixa os PDFs para .cache/normas/)
#                 pdftotext (poppler) instalado.
# Saída: verificacao/CONTEUDO.md (sem reproduzir texto das normas). --detalhe imprime trechos no terminal.
import json, re, subprocess, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PARADAS = set("""quando sobre entre pelos pelas outros outras sempre antes depois tambem mesmo mesma podem
pode devem deve ficam fica para como partir norma normas item itens exemplo exemplos valor valores entidade
qualquer cada todos todas seguinte seguintes desta deste dessa desse essas esses nesta neste onde ainda
apenas parte partes forma modo caso casos ponto pontos inclusive conforme vigor""".split())
# trechos com pouca sobreposição de palavras que foram lidos no texto oficial e estão corretos
# (dados/revisao_manual.csv: norma, itens, data da revisão)
sys.path.insert(0, str(ROOT / "manutencao" / "scripts"))
from dados import ler  # noqa: E402
REVISADOS = {(x["norma"], x["itens"]): x["data"] for x in ler("revisao_manual.csv")}
ITEM_RX = r"(?m)^\s*{}\.?\s+\S"
QUALQUER_ITEM = re.compile(r"(?m)^\s*(?:[A-Z]{1,2})?\d+[A-Z]?(?:\.\d+)*\.?\s+[A-ZÀ-Ý(“\"]")


def sem_acento(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def chaves(s):
    return {w[:6] for w in re.findall(r"[a-z]{5,}", sem_acento(s))} - {w[:6] for w in PARADAS}


def texto_pdf(arq, cache={}):
    if arq not in cache:
        out = subprocess.run(["pdftotext", "-enc", "UTF-8", arq, "-"], capture_output=True, cwd=ROOT)
        cache[arq] = out.stdout.decode("utf-8", "ignore")
    return cache[arq]


def expandir(spec):
    """'10–11' -> ['10','11']; 'B28–B33'; '60–62A' -> 60,61,62,62A; '16(c)' -> 16; 'cap. 6' -> ('cap','6')."""
    ids = []
    for parte in re.split(r",| e ", spec):
        parte = parte.strip()
        if not parte or parte in ("—", "-"):
            continue
        m = re.match(r"cap\.?\s*(\d+)", parte)
        if m:
            ids.append(("cap", m.group(1))); continue
        parte = re.sub(r"\(.*?\)", "", parte)
        m = re.match(r"((?:\d+\.)+)(\d+)\s*[–-]\s*\1(\d+)$", parte)      # 3.2.3–3.2.6
        if m:
            ids += [f"{m.group(1)}{n}" for n in range(int(m.group(2)), int(m.group(3)) + 1)]
            continue
        m = re.match(r"([A-Z]{0,2})(\d+)([A-Z]?)\s*[–-]\s*([A-Z]{0,2})(\d+)([A-Z]?)$", parte)
        if m:
            pre, a, _, _, b, suf = m.groups()
            ids += [f"{pre}{n}" for n in range(int(a), int(b) + 1)]
            if suf:
                ids.append(f"{pre}{b}{suf}")
            continue
        ids.append(parte)
    return ids


def trecho_item(txt, item):
    if isinstance(item, tuple):          # capítulo: existe algum item 6.x?
        m = re.search(ITEM_RX.format(re.escape(item[1]) + r"\.\d+"), txt)
        return txt[m.start():m.start() + 6000] if m else None
    trechos = []
    achados = list(re.finditer(ITEM_RX.format(re.escape(item)), txt))
    if not achados:   # o PDF às vezes junta o início do item ao fim da linha anterior ("... do CFC. 118. Os ...")
        achados = list(re.finditer(r"(?<=[.;:]\s)" + re.escape(item) + r"\.\s+[A-ZÀ-Ý(]", txt))
    for m in achados:
        fim = QUALQUER_ITEM.search(txt, m.end() + 5)
        trechos.append(txt[m.start():(fim.start() if fim else m.start() + 3000)][:3000])
    return " ".join(trechos) if trechos else None


def main():
    detalhe = "--detalhe" in sys.argv
    normas = json.loads((ROOT / "normas.json").read_text(encoding="utf-8"))["normas"]
    links = {x["codigo"]: x for x in json.loads((ROOT / "manutencao" / "verificacao" / "links.json").read_text(encoding="utf-8"))}
    arq_de = {c: x.get("arquivo") for c, x in links.items() if x.get("arquivo")}
    if not arq_de:
        sys.exit("Nenhum PDF em cache: rode antes  python scripts/verificar_links.py --baixar")

    linhas_it, linhas_res, sem_pdf = [], [], []
    cont = {"item ok": 0, "ok (revisado manualmente)": 0, "conferir": 0, "item não encontrado": 0, "sem PDF": 0}

    def situacao(cod, itens, sit):
        return "ok (revisado manualmente)" if sit == "conferir" and (cod, itens) in REVISADOS else sit
    for r in normas:
        arq = arq_de.get(r["codigo"])
        txt = texto_pdf(arq) if arq and (ROOT / arq).exists() else None
        # resumos
        if txt:
            k = chaves(r["resumo"]); kt = chaves(txt)
            sc = round(len(k & kt) / len(k), 2) if k else 1.0
            linhas_res.append((sc, r["codigo"]))
        # trechos de setor
        for p in r.get("setores", []):
            ids = expandir(p["itens"])
            if not txt:
                cont["sem PDF"] += 1; sem_pdf.append(r["codigo"]); continue
            if not ids:                       # sem item citado: compara com o texto inteiro
                k = chaves(p["ponto"]); sc = round(len(k & chaves(txt)) / len(k), 2) if k else 1.0
                sit = situacao(r["codigo"], p["itens"], "item ok" if sc >= 0.5 else "conferir")
                cont[sit] += 1
                linhas_it.append((sit, r["codigo"], p["itens"], sc, p["setor"] + ": " + p["topico"], ""))
                continue
            faltam = [i if isinstance(i, str) else f"cap. {i[1]}" for i in ids if not trecho_item(txt, i)]
            corpo = " ".join(t for t in (trecho_item(txt, i) for i in ids) if t)
            k = chaves(p["ponto"])
            sc = round(len(k & chaves(corpo)) / len(k), 2) if k and corpo else 0.0
            sit = situacao(r["codigo"], p["itens"], "item não encontrado" if faltam else ("item ok" if sc >= 0.3 else "conferir"))
            cont[sit] += 1
            linhas_it.append((sit, r["codigo"], p["itens"], sc, p["setor"] + ": " + p["topico"], ", ".join(faltam)))
            if detalhe and sit != "item ok":
                print(f"\n### {r['codigo']} itens {p['itens']} ({sit}, {sc}) faltam={faltam}\nPONTO: {p['ponto']}\nTEXTO: {corpo[:900]}")

    md = ["# Verificação do conteúdo contra o texto oficial\n",
          "Gerado por `scripts/verificar_itens.py` a partir dos PDFs oficiais do CFC (não versionados). "
          "Confere se cada item citado nas pastas de setor existe na norma e se o texto do item trata do assunto "
          "descrito (sobreposição de palavras-chave), e se as palavras-chave de cada resumo aparecem na norma. "
          "É uma checagem automática: \"ok\" não substitui leitura, e \"conferir\" pede revisão humana.\n",
          "## Trechos citados nas pastas de setor\n", "| Situação | Quantidade |\n|---|---|"]
    md += [f"| {k} | {v} |" for k, v in cont.items() if v]
    md.append("\n| Situação | Norma | Itens | Aderência | Tópico | Itens não encontrados |\n|---|---|---|---|---|---|")
    for sit, cod, it, sc, top, falt in sorted(linhas_it, key=lambda x: (x[0].startswith(("item ok", "ok")), x[3])):
        md.append(f"| {sit} | {cod} | {it} | {sc:.0%} | {top} | {falt} |")
    baixos = sorted(x for x in linhas_res if x[0] < 0.5)
    md.append(f"\n## Resumos\n\n{len(linhas_res)} resumos comparados com o texto da norma. "
              f"{len(baixos)} com menos de 50% das palavras-chave encontradas (revisar):\n")
    md.append("| Norma | Palavras-chave encontradas |\n|---|---|")
    md += [f"| {c} | {s:.0%} |" for s, c in baixos] or ["| — | — |"]
    if sem_pdf:
        md.append("\nSem PDF oficial para conferir: " + ", ".join(sorted(set(sem_pdf))))
    (ROOT / "manutencao" / "verificacao" / "confianca.json").write_text(json.dumps(
        {f"{c}|{i}|{t}": sit for sit, c, i, _, t, _ in linhas_it}, ensure_ascii=False, indent=1), encoding="utf-8")
    (ROOT / "manutencao" / "verificacao" / "CONTEUDO.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(cont, "| resumos abaixo de 50%:", len(baixos), "de", len(linhas_res))
    sys.exit(1 if cont["conferir"] or cont["item não encontrado"] or baixos else 0)


if __name__ == "__main__":
    main()
