# Gera uma pasta por setor (Industrial/, Comercio/, Servicos/...) com os trechos das normas que importam
# para aquele tipo de empresa, e anota cada norma em normas.json (campo "setores").
# Os dados de cada setor ficam em scripts/dados_setores/<setor>.py com:
#   NOME, PASTA, USE_PARA, INTRO, TOPICOS, FAQ e, opcional, EXTERNAS (regras de fora do CFC: BCB, CVM, SUSEP, leis).
# Os itens seguem a numeração do CPC/NBC (a mesma da IAS/IFRS). scripts/verificar_itens.py confere cada item no PDF oficial.
import importlib, re, shutil

SETORES = ["industrial", "comercio", "servicos", "agronegocio", "construcao", "terceiro_setor", "financeiro"]
AVISO = ("> Resumo orientativo dos trechos das normas aplicáveis ao setor; não substitui o texto oficial. "
         "Os números de item seguem o CPC/NBC (mesma numeração da IAS/IFRS) e são conferidos automaticamente "
         "contra os PDFs oficiais (`verificacao/CONTEUDO.md`). Confira sempre pelo link oficial.")


def gerar_todos(root, REC, sem_rev):
    por_cod = {sem_rev(r["codigo"]): r for r in REC}
    for r in REC:
        r["setores"] = []
    return [gerar_setor(root, por_cod, importlib.import_module("dados_setores." + s)) for s in SETORES]


def gerar_setor(root, por_cod, m):
    externas = getattr(m, "EXTERNAS", {})
    usados = {c for t in m.TOPICOS for c, _, _ in t[4]} | {f[2] for f in m.FAQ}
    falta = sorted(c for c in usados if c not in por_cod and c not in externas)
    assert not falta, f"{m.NOME}: normas não encontradas no índice nem em EXTERNAS: {falta}"

    def cab(c):
        if c in externas:
            titulo, url, nota = externas[c]
            return f"### {c} – {titulo} · [texto oficial]({url})" + (f"\n\n{nota}" if nota else "")
        r = por_cod[c]
        cpc = f"[{r['cpc']}]({r['url_cpc']})" if r.get("url_cpc") else r["cpc"]
        refs = " · ".join(x for x in (cpc, r["internacional"]) if x)
        aviso = f"\n\n⚠ {r['situacao']}" if r.get("situacao", "vigente") != "vigente" else ""
        return f"### {r['codigo']} – {r['titulo']}" + (f" ({refs})" if refs else "") + f" · [texto oficial]({r['url']}){aviso}"

    def nome_url(c):
        if c in externas:
            return c, externas[c][1]
        return por_cod[c]["codigo"], por_cod[c]["url"]

    pasta = root / m.PASTA
    shutil.rmtree(pasta, ignore_errors=True)
    pasta.mkdir()
    for arq, titulo, usar, intro, pontos, check in m.TOPICOS:
        md = [f"# {m.NOME}: {titulo}\n", f"**Use para:** {usar}.\n", intro + "\n", AVISO + "\n"]
        ordem = []
        for c, _, _ in pontos:
            if c not in ordem:
                ordem.append(c)
        for c in ordem:
            md.append("\n" + cab(c) + "\n\n| Item | O que diz para o setor |\n|---|---|")
            for c2, itens, txt in pontos:
                if c2 == c:
                    md.append(f"| {itens} | {txt} |")
                    if c in por_cod:
                        por_cod[c]["setores"].append({"setor": m.NOME, "pasta": m.PASTA, "topico": titulo,
                                                      "arquivo": f"{m.PASTA}/{arq}.md", "itens": itens, "ponto": txt})
        md.append("\n## Checklist na prática\n")
        md += [f"- [ ] {x}" for x in check]
        md.append(f"\n[← {m.NOME}: índice](README.md) · [Todas as áreas](../areas/README.md)")
        (pasta / f"{arq}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    idx = [f"# {m.NOME}: normas que importam\n", m.INTRO + "\n", AVISO + "\n",
           "## Tópicos\n\n| Tópico | Use para | Normas |\n|---|---|---|"]
    for arq, titulo, usar, _, pontos, _ in m.TOPICOS:
        cods = []
        for c, _, _ in pontos:
            n = nome_url(c)[0]
            if n not in cods:
                cods.append(n)
        idx.append(f"| [{titulo}]({arq}.md) | {usar} | {', '.join(cods)} |")
    idx.append("\n## Perguntas frequentes\n\n| Pergunta | Resposta curta | Norma (item) |\n|---|---|---|")
    for p, resp, c, it in m.FAQ:
        n, u = nome_url(c)
        rot = "" if it in ("—", "") else (" (itens " if re.search(r"[–,]| e ", it) else " (item ") + it + ")"
        idx.append(f"| {p} | {resp} | [{n}]({u}){rot} |")
    idx.append("\n[Todas as áreas](../areas/README.md) · [Índice geral](../README.md)")
    (pasta / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    return m.NOME, m.PASTA, m.USE_PARA, [(arq, titulo) for arq, titulo, *_ in m.TOPICOS]
