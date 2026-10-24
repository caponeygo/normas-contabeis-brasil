# Gera graph.html: rede interativa em que SETORES e ÁREAS são os centros e as normas ficam presas aos centros
# a que pertencem (uma norma que serve a vários setores/áreas fica entre eles, ligando-os naturalmente).
# Dados: normas.json (gerado por gerar_indice.py) e dados/setores.csv. Sem bibliotecas externas.
# Rodar da raiz do projeto: python manutencao/graphify-out/build_html.py
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "manutencao" / "scripts"))
from dados import ler  # noqa: E402

REPO = "https://github.com/caponeygo/normas-contabeis-brasil/blob/main/"
d = json.loads((ROOT / "normas.json").read_text(encoding="utf-8"))
NORMAS = d["normas"]


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def base(c):
    return re.sub(r"\s*\(R\d+\)", "", c).strip()


SETORES = [{"nome": s["nome"], "url": REPO + s["pasta"] + "/README.md", "uso": s["use_para"]} for s in ler("setores.csv")]
s_idx = {s["nome"]: i for i, s in enumerate(SETORES)}
AREAS = []
for n in NORMAS:
    for a in n["areas"]:
        if a not in AREAS:
            AREAS.append(a)
AREAS.sort()
a_idx = {a: i for i, a in enumerate(AREAS)}
uso = {a["area"]: a["use_para"] for a in ler("areas.csv")}

por_base = {base(n["codigo"]): i for i, n in enumerate(NORMAS)}
padroes = {k: re.compile(r"(?<![\w.])" + re.escape(k) + r"(?![\w.])") for k in por_base}

nos = []
for i, n in enumerate(NORMAS):
    texto = " ".join(x for x in (n.get("internacional"), n.get("cpc")) if x)
    eq = sorted({j for k, j in por_base.items() if j != i and padroes[k].search(texto)})
    nos.append({
        "c": n["codigo"], "t": n["titulo"], "s": n["serie"], "st": n["status"],
        "a": [a_idx[a] for a in n["areas"]],
        "x": sorted({s_idx[s["setor"]] for s in n["setores"] if s["setor"] in s_idx}),
        "e": eq,
        "r": (n["resumo"] or "")[:320], "u": n["url"], "f": "normas/ficha/" + slug(n["codigo"]) + ".md",
        "sp": n.get("substituida_por"),
    })

dados = {"setores": SETORES, "areas": [{"nome": a, "uso": uso.get(a, ""), "url": REPO + "areas/" + slug(a) + ".md"} for a in AREAS],
         "normas": nos, "repo": REPO}
tpl = (Path(__file__).resolve().parent / "template.html").read_text(encoding="utf-8")
saida = tpl.replace("__DATA__", json.dumps(dados, ensure_ascii=False, separators=(",", ":")))
(Path(__file__).resolve().parent / "graph.html").write_text(saida, encoding="utf-8")
print(f"{len(SETORES)} setores, {len(AREAS)} áreas, {len(nos)} normas, "
      f"{sum(len(n['e']) for n in nos)} equivalências")
