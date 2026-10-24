# Testa se uma busca por palavras-chave (como a de um assistente de IA no repositório) acha o arquivo certo.
# Para cada pergunta de testes/perguntas.json: ranqueia os .md do repositório por BM25 e confere se um dos
# arquivos esperados está entre os 3 primeiros e se ele cita as normas esperadas.
# Saída: verificacao/BUSCA.md. Sai com código 1 se o acerto ficar abaixo de 90%.
import json, math, re, sys, unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PASTAS = ["areas", "lancamentos", "normas", "normas/ficha"] + [f"setores/{x}" for x in ["industrial", "varejo", "servicos", "agronegocio", "construcao", "terceiro-setor", "financeiro"]]
PARADAS = set("""de da do das dos a o as os e em no na nos nas um uma uns umas para por com sem que qual quais
como quando onde ou ao aos se sua seu suas seus ser sao foi esta este isso essa esse pelo pela pelos pelas
mais menos ja so nao sim deve devo pode posso vira entra fica sobre entre ate apos the""".split())


def tokens(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return [w[:6] for w in re.findall(r"[a-z0-9]{2,}", s) if w not in PARADAS]


def main():
    docs = {}
    for p in PASTAS:
        for f in (ROOT / p).glob("*.md"):
            docs[f.relative_to(ROOT).as_posix()] = f.read_text(encoding="utf-8")
    docs["GLOSSARIO.md"] = (ROOT / "GLOSSARIO.md").read_text(encoding="utf-8")
    tf = {d: Counter(tokens(t)) for d, t in docs.items()}
    n = len(docs); media = sum(sum(c.values()) for c in tf.values()) / n
    df = Counter(w for c in tf.values() for w in c)
    k1, b = 1.5, 0.75

    def bm25(consulta):
        q = tokens(consulta)
        notas = {}
        for d, c in tf.items():
            tam = sum(c.values()); s = 0.0
            for w in q:
                if w in c:
                    idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
                    s += idf * c[w] * (k1 + 1) / (c[w] + k1 * (1 - b + b * tam / media))
            notas[d] = s
        return sorted(notas, key=notas.get, reverse=True)

    perguntas = json.loads((ROOT / "manutencao" / "testes" / "perguntas.json").read_text(encoding="utf-8"))
    linhas, acertos = [], 0
    for p in perguntas:
        top = bm25(p["pergunta"])[:3]
        normas = [nm.lower() for nm in p.get("normas", [])]
        # a ficha de uma norma esperada também é resposta certa (ela cita a norma pedida)
        achou = next((d for d in top if d in p["arquivos"]
                      or (d.startswith("normas/ficha/") and normas and all(nm in docs[d].lower() for nm in normas))), None)
        cita = achou and all(nm.lower() in docs[achou].lower() for nm in p.get("normas", []))
        ok = bool(achou and cita)
        acertos += ok
        linhas.append(f"| {'✅' if ok else '❌'} | {p['pergunta']} | {', '.join(top)} | {achou or '—'} |")
    taxa = acertos / len(perguntas)
    md = ["# Teste de busca\n",
          "Gerado por `scripts/testar_busca.py`: para cada pergunta de `testes/perguntas.json`, uma busca por "
          "palavras-chave (BM25) ranqueia os arquivos do repositório. Passa quando um arquivo esperado aparece "
          "entre os 3 primeiros e cita as normas esperadas.\n",
          f"**Acerto: {acertos}/{len(perguntas)} ({taxa:.0%})**\n",
          "| | Pergunta | 3 primeiros arquivos | Arquivo esperado encontrado |\n|---|---|---|---|"] + linhas
    (ROOT / "manutencao" / "verificacao").mkdir(exist_ok=True)
    (ROOT / "manutencao" / "verificacao" / "BUSCA.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"acerto {acertos}/{len(perguntas)} ({taxa:.0%})")
    for l in linhas:
        if l.startswith("| ❌"):
            print(l)
    sys.exit(0 if taxa >= 0.9 else 1)


if __name__ == "__main__":
    main()
