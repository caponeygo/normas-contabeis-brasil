# Verifica os links oficiais de normas.json.
# Para páginas do CFC (detalhes_sre.aspx) não basta o HTTP 200: a página sempre responde,
# então conferimos se a norma aparece, se está em vigor e se não foi revogada.
# Saída: verificacao/LINKS.md e verificacao/links.json. Sai com código 1 se houver link quebrado.
# Uso: python scripts/verificar_links.py [--baixar]   (--baixar salva os PDFs em .cache/normas/)
import html, json, re, sys, time, unicodedata, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (verificador normas-contabeis-brasil)"}
CACHE = ROOT / ".cache" / "normas"


def baixar(url, tentativas=3):
    for i in range(tentativas):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.status, r.headers.get("Content-Type", ""), r.read()
        except Exception as e:  # rede instável: tenta de novo
            erro = e
            time.sleep(2 * (i + 1))
    return None, str(erro), b""


def texto(html_bytes):
    s = html_bytes.decode("utf-8", "ignore")
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip(), s


def campo(t, nome, ate):
    m = re.search(nome + r"\s*:?\s*(.*?)\s*(?:" + ate + ")", t)
    return m.group(1).strip() if m else None


def sem_acento(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def palavras(s):
    return {w[:6] for w in re.findall(r"[a-z]{5,}", sem_acento(s))} - {"norma", "tecni", "contab", "brasi", "sobre", "dispo", "altera", "aprov"}


def checar(r):
    url = r["url"]
    res = {"codigo": r["codigo"], "titulo": r["titulo"], "url": url}
    status, ctype, corpo = baixar(url)
    res["http"] = status
    if status != 200:
        res["situacao"] = "quebrado"; res["detalhe"] = f"HTTP {status or ctype}"
        return res
    if "detalhes_sre.aspx" not in url:
        res["situacao"] = "ok" if corpo else "quebrado"
        if url.lower().endswith(".pdf") and corpo[:4] == b"%PDF":
            res["pdf"] = url                          # PDF direto (ex.: Orientações Técnicas do CFC)
        return res
    t, bruto = texto(corpo)
    if "Número da resolução" not in t and "Numero da resolucao" not in sem_acento(t):
        res["situacao"] = "quebrado"; res["detalhe"] = "página do CFC sem a norma (código inválido)"
        return res
    res["descricao"] = campo(t, "Descrição", "Data de Publicação")
    res["em_vigor"] = campo(t, "Resolução em vigor", "Resolução foi alterada")
    res["revogada"] = campo(t, "Resolução foi revogada", "Ementa")
    pdfs = re.findall(r'href="([^"]+\.pdf)"', bruto, re.I)
    docs = re.findall(r'href="([^"]+\.docx?)"', bruto, re.I)
    res["pdf"] = pdfs[0] if pdfs else None
    res["doc"] = docs[0] if docs else None
    alvo = (res["descricao"] or "") + " " + (campo(t, "Ementa", "Esta Resolução|Para obter") or "")
    pt = palavras(r["titulo"])
    res["titulo_confere"] = round(len(pt & palavras(alvo)) / len(pt), 2) if pt else 1.0
    cod = re.sub(r"\s*\(R\d+\)", "", r["codigo"]).replace(" ", "").lower()
    if cod in alvo.replace(" ", "").lower():
        res["titulo_confere"] = 1.0
    if (res["revogada"] or "").upper().startswith("SIM") or (res["em_vigor"] or "").upper().startswith("N"):
        res["situacao"] = "revogada (já marcada no índice)" if r.get("situacao", "vigente") != "vigente" else "revogada ou fora de vigor"
    elif res["titulo_confere"] < 0.34:
        res["situacao"] = "conferir título"
    else:
        res["situacao"] = "ok"
    return res


def baixar_pdf(res):
    if not res.get("pdf"):
        return
    nome = re.sub(r"[^A-Za-z0-9]+", "_", res["codigo"]).strip("_") + ".pdf"
    destino = CACHE / nome
    if destino.exists() and destino.stat().st_size > 1000:
        res["arquivo"] = destino.relative_to(ROOT).as_posix(); return
    status, ctype, corpo = baixar(res["pdf"])
    if status == 200 and corpo[:4] == b"%PDF":
        destino.write_bytes(corpo)
        res["arquivo"] = destino.relative_to(ROOT).as_posix()


def main():
    d = json.loads((ROOT / "normas.json").read_text(encoding="utf-8"))
    alvos, vistos = [], set()
    for r in d["normas"]:
        if r.get("url") and r["url"] not in vistos:
            vistos.add(r["url"]); alvos.append(r)
        if r.get("url_cpc") and r["url_cpc"] not in vistos:     # página oficial do CPC equivalente
            vistos.add(r["url_cpc"]); alvos.append({"codigo": r["cpc"], "titulo": r["titulo"], "url": r["url_cpc"]})
    # regras de fora do CFC citadas nas pastas de setor (BCB, CVM, SUSEP, leis)
    sys.path.insert(0, str(ROOT / "scripts"))
    import importlib, gerar_setores
    for s in gerar_setores.SETORES:
        for cod, (tit, url, _) in getattr(importlib.import_module("dados_setores." + s), "EXTERNAS", {}).items():
            if url not in vistos:
                vistos.add(url); alvos.append({"codigo": cod, "titulo": tit, "url": url})
    with ThreadPoolExecutor(4) as ex:                 # 4 conexões: educado com o servidor do CFC
        res = list(ex.map(checar, alvos))
    if "--baixar" in sys.argv:
        CACHE.mkdir(parents=True, exist_ok=True)
        with ThreadPoolExecutor(3) as ex:
            list(ex.map(baixar_pdf, res))
    for x in res:                                     # PDFs já baixados antes continuam valendo
        arq = CACHE / (re.sub(r"[^A-Za-z0-9]+", "_", x["codigo"]).strip("_") + ".pdf")
        if not x.get("arquivo") and x.get("pdf") and arq.exists():
            x["arquivo"] = arq.relative_to(ROOT).as_posix()

    saida = ROOT / "verificacao"; saida.mkdir(exist_ok=True)
    (saida / "links.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    cont = {}
    for x in res:
        cont[x["situacao"]] = cont.get(x["situacao"], 0) + 1
    md = ["# Verificação dos links oficiais\n",
          "Gerado por `scripts/verificar_links.py`. Cada página do CFC é aberta e conferida: a norma existe, "
          "está em vigor, não foi revogada e o título bate com a descrição oficial.\n",
          "| Situação | Quantidade |\n|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(cont.items())]
    prob = [x for x in res if x["situacao"] not in ("ok", "revogada (já marcada no índice)")]
    md.append("\n## Para conferir\n")
    if prob:
        md.append("| Norma | Situação | Detalhe | Link |\n|---|---|---|---|")
        for x in prob:
            det = x.get("detalhe") or (x.get("descricao") or "")[:120]
            md.append(f"| {x['codigo']} | {x['situacao']} | {det} | [abrir]({x['url']}) |")
    else:
        md.append("Nenhum problema encontrado.")
    (saida / "LINKS.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(cont)
    sys.exit(1 if cont.get("quebrado") else 0)


if __name__ == "__main__":
    main()
