# Converte os PDFs oficiais baixados (.cache/normas/, ver verificar_links.py --baixar) em um arquivo de texto por norma
# em textos/<ficha>.md e confere a extração: páginas sem texto (precisariam de OCR) e itens numerados faltando.
# Uso: python manutencao/scripts/extrair_textos.py
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SAIDA = ROOT / "textos"            # fora de normas/: o gerador do índice recria normas/ a cada rodada
REL = ROOT / "manutencao" / "verificacao" / "TEXTOS.md"


def slug(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def texto_paginas(pdf):
    """Texto de cada página, na ordem de leitura (sem -layout: parágrafos corridos, que o Markdown não vira bloco de código)."""
    out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True)
    return out.stdout.decode("utf-8", "replace").split("\f")[:-1] or [""]


_OCR = None


def ocr_pagina(pdf, i):
    """OCR (RapidOCR) da página i (1-based) renderizada a 220 dpi. Devolve (texto, confiança média)."""
    global _OCR
    import numpy as np, pymupdf
    if _OCR is None:
        from rapidocr_onnxruntime import RapidOCR
        _OCR = RapidOCR()
    with pymupdf.open(pdf) as doc:
        pix = doc[i - 1].get_pixmap(dpi=220)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    res, _ = _OCR(img)
    if not res:
        return "", 0.0
    itens = sorted(((sum(p[1] for p in b) / 4, min(p[0] for p in b), t, float(c)) for b, t, c in res))
    linhas, atual, ult = [], [], None
    for y, x, t, c in itens:
        if ult is not None and y - ult > 14:
            linhas.append(sorted(atual)); atual = []
        atual.append((x, t)); ult = y
    linhas.append(sorted(atual))
    return "\n".join(" ".join(t for _, t in l) for l in linhas), sum(c for *_, c in itens) / len(itens)


ITEM = re.compile(r"^((?:[A-Z]{1,2})?\d{1,3}[A-Z]?(?:\.\d{1,3})*)\.?[ 	]+(?=[A-ZÀ-ÚÇ“\"(])", re.M)


def ancorar(t, vistos):
    """Põe <a id="item-N"></a> antes da primeira linha de cada item numerado (27, 4.1.2, B42), sem mudar o texto."""
    def f(m):
        k = m.group(1)
        if k in vistos:
            return m.group(0)
        vistos.add(k)
        return f'<a id="item-{k.lower()}"></a>' + m.group(0)
    return ITEM.sub(f, t)


def limpar(t):
    t = t.replace("­", "").replace("\r", "")
    t = t.replace("](", chr(92) + "](")      # "[...](4)" do texto não vira link no Markdown
    return re.sub(r"[ \t]+\n", "\n", t)


def main():
    links = json.loads((ROOT / "manutencao" / "verificacao" / "links.json").read_text(encoding="utf-8"))
    normas = {n["codigo"]: n for n in json.loads((ROOT / "normas.json").read_text(encoding="utf-8"))["normas"]}
    SAIDA.mkdir(exist_ok=True)
    feitos, sem_pdf, vazios, ocrados = [], [], [], []
    for x in links:
        n = normas.get(x["codigo"])
        arq = ROOT / x["arquivo"] if x.get("arquivo") else None
        if not n or not arq or not arq.exists():
            if n:
                sem_pdf.append(x["codigo"])
            continue
        pags = [limpar(p) for p in texto_paginas(arq)]
        sem_texto = [i + 1 for i, p in enumerate(pags) if len(p.strip()) < 40]
        ocr = {}
        if "--ocr" in sys.argv:
            for i in sem_texto:
                t, conf = ocr_pagina(arq, i)
                if t.strip():
                    pags[i - 1] = t; ocr[i] = conf
            sem_texto = [i for i in sem_texto if i not in ocr]
        chars = sum(len(p) for p in pags)
        nome = slug(n["codigo"])
        cab = [f"# {n['codigo']} – {n['titulo']}", "",
               f"> Texto integral extraído do PDF oficial do CFC ({len(pags)} páginas). Fonte e versão vigente: [{x['url']}]({x['url']}). "
               "A extração é automática: confira o PDF oficial antes de citar. Cada item numerado tem âncora (ex.: `#item-27`).", "",
               f"[Ficha da norma](../normas/ficha/{nome}.md) · [Todas as normas](../normas/README.md)", ""]
        corpo, vistos = [], set()
        for i, p in enumerate(pags, 1):
            marca = f"página {i} (OCR, confiança {ocr[i]:.0%})" if i in ocr else f"página {i}"
            corpo.append(f"\n<!-- {marca} -->\n\n{ancorar(p.strip(), vistos)}")
        (SAIDA / f"{nome}.md").write_text("\n".join(cab) + "\n".join(corpo) + "\n", encoding="utf-8")
        feitos.append((n["codigo"], len(pags), chars, sem_texto))
        if ocr:
            ocrados.append((n["codigo"], len(ocr), min(ocr.values()), sum(ocr.values()) / len(ocr)))
        if sem_texto:
            vazios.append((n["codigo"], sem_texto, len(pags)))
    md = ["# Extração do texto integral\n",
          f"Gerado por `manutencao/scripts/extrair_textos.py`. {len(feitos)} normas extraídas dos PDFs oficiais do CFC.\n",
          "## Páginas sem texto (precisam de OCR ou conferência)\n"]
    if vazios:
        md.append("| Norma | Páginas sem texto | Total de páginas |\n|---|---|---|")
        md += [f"| {c} | {', '.join(map(str, p[:15]))}{'…' if len(p) > 15 else ''} | {t} |" for c, p, t in vazios]
    else:
        md.append("Nenhuma.")
    md.append("\n## Páginas lidas por OCR (conferir com o PDF)\n")
    if ocrados:
        md.append("| Norma | Páginas | Confiança mínima | Confiança média |\n|---|---|---|---|")
        md += [f"| {c} | {k} | {mn:.0%} | {me:.0%} |" for c, k, mn, me in ocrados]
    else:
        md.append("Nenhuma.")
    md.append("\n## Normas sem PDF extraído\n")
    md.append(", ".join(sem_pdf) if sem_pdf else "Nenhuma.")
    REL.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(feitos)} extraídas; {len(vazios)} com páginas sem texto; {len(sem_pdf)} sem PDF")
    return 1 if vazios else 0


if __name__ == "__main__":
    sys.exit(main())
