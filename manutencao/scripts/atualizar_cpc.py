# Baixa a lista de pronunciamentos (CPC), interpretações (ICPC) e orientações (OCPC) do site do CPC
# e salva em scripts/cpc.json (código, título, link, revogado). gerar_indice.py usa esse arquivo.
# Uso: python scripts/atualizar_cpc.py
import html, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verificar_links import baixar  # noqa: E402

BASE = "https://www.cpc.org.br"
TIPOS = {"Pronunciamentos": "Pronunciamento", "Interpretacoes": "Interpretacao", "Orientacoes": "Orientacao"}


def main():
    itens = {}
    for tipo, sing in TIPOS.items():
        st, _, corpo = baixar(f"{BASE}/CPC/Documentos-Emitidos/{tipo}")
        if st != 200:
            sys.exit(f"falhou {tipo}: {st}")
        s = corpo.decode("utf-8", "ignore")
        por_link = {}
        for href, txt in re.findall(r'<a[^>]+href="([^"]*' + sing + r'\?Id=\d+)"[^>]*>(.*?)</a>', s, re.S):
            t = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", txt)).split())
            if t:
                por_link.setdefault(href, []).append(t)
        for href, textos in por_link.items():
            cod = next((t for t in textos if re.match(r"^(CPC|ICPC|OCPC)\b", t)), None)
            if not cod:
                continue
            titulo = next((t for t in textos if t != cod), "")
            itens[cod] = {"codigo": cod, "titulo": titulo, "url": BASE + href,
                          "revogado": bool(re.search(r"revogad", titulo, re.I))}
    out = Path(__file__).resolve().parent / "cpc.json"
    out.write_text(json.dumps(sorted(itens.values(), key=lambda x: x["codigo"]), ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(itens), "documentos do CPC salvos em", out.name)


if __name__ == "__main__":
    main()
