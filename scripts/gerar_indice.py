# Gera README.md, areas/, as pastas por setor, normas.json e a extração do grafo a partir das planilhas em dados/.
# As planilhas (CSV separado por ";", abrem no Excel) são a fonte dos dados: edite lá e rode
#     python graphify-out/rebuild_graph.py
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dados import ler  # noqa: E402


def sem_rev(c):
    return re.sub(r"\s*\(R\d+\)", "", c).strip()


# links oficiais do CPC (scripts/cpc.json, gerado por scripts/atualizar_cpc.py)
def _ncpc(c):
    return sem_rev(c or "").replace(" ", "").upper()


_cpcj = ROOT / "scripts" / "cpc.json"
CPC_URL = {_ncpc(x["codigo"]): x["url"] for x in json.loads(_cpcj.read_text(encoding="utf-8"))} if _cpcj.exists() else {}


def link_cpc(c):
    if not c or c == "—":
        return c or "—"
    u = CPC_URL.get(_ncpc(c))
    return f"[{c}]({u})" if u else c


SECOES = ler("secoes.csv")
NORMAS = ler("normas.csv")
secoes_ids = {s["secao"] for s in SECOES}
erros = [n["codigo"] for n in NORMAS if n["secao"] not in secoes_ids]
assert not erros, f"normas.csv: seção inexistente em secoes.csv para {erros}"

HEAD = """# Normas Contábeis Brasileiras: CPC, NBC TG, ITG e NBC TA

Índice das normas contábeis e de auditoria do Brasil, com links para os textos oficiais:
pronunciamentos do **CPC** (Comitê de Pronunciamentos Contábeis), **NBC TG / ITG / CTG** (contabilidade)
e **NBC TA** (auditoria independente) do **CFC** (Conselho Federal de Contabilidade).

> **Aviso:** este repositório não hospeda o texto das normas. Os documentos têm direitos autorais
> (parte deriva das IFRS © IFRS Foundation e das ISA © IFAC) e são revisados com frequência.
> Os links levam ao texto no site do CFC. Confira sempre a versão vigente. Este índice não é aconselhamento profissional.

## Sumário
- [Fontes oficiais](#fontes-oficiais)
- [Como ler a numeração](#como-ler-a-numeração)
- [NBC TG (correlação CPC / IFRS)](#nbc-tg--normas-técnicas-gerais)
- [ITG / CTG / OTG (ICPC / OCPC)](#itg--ctg--otg--interpretações-e-comunicados)
- [NBC TA (auditoria independente)](#nbc-ta--auditoria-independente)
- PMEs (NBC TG 1000), normas específicas (ITG 2000), NBC TSP, NBC TDS, NBC TR, NBC TO, NBC TSC, NBC TI, NBC TP, NBC PG, NBC PA e NBC PP: logo após as NBC TA
- [IFRS e IAS (IASB)](#normas-internacionais--ifrs-e-ias-iasb)

## Fontes oficiais
- CFC, Normas Brasileiras de Contabilidade: <https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/>
- CFC, normas completas (NBC TG, ITG, CTG): <https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/normas-completas/>
- CFC, NBC TA: <https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>
- CPC: <https://www.cpc.org.br>
- CVM: <https://www.gov.br/cvm>

- IFRS Foundation (IFRS, IAS, IFRS S): <https://www.ifrs.org/issued-standards/list-of-standards/>
- IAASB (ISA): <https://www.iaasb.org/>

## Como ler a numeração
`CPC 26 (R1)` é o pronunciamento do CPC. O CFC o torna obrigatório para os contadores como `NBC TG 26 (R5)`.
`(Rn)` indica a revisão. As interpretações `ICPC` correspondem às `ITG`, e as orientações `OCPC` correspondem aos `CTG`.
"""

# formato de cada seção do README: cabeçalho da tabela e linha de cada norma
FORMATOS = {
    "tg": ("| NBC TG | Título | CPC | IFRS/IAS | Texto |\n|---|---|---|---|---|",
           lambda n: f"| {n['codigo']} | {n['titulo']} | {link_cpc(n['cpc'])} | {n['internacional']} | [abrir]({n['url']}) |"),
    "itg": ("| Norma | Título | CPC equivalente | Texto |\n|---|---|---|---|",
            lambda n: f"| {n['codigo']} | {n['titulo']} | {link_cpc(n['cpc'])} | [abrir]({n['url']}) |"),
    "ta": ("| NBC TA | Título | Texto |\n|---|---|---|",
           lambda n: f"| {n['codigo']} | {n['titulo']} | [abrir]({n['url']}) |"),
    "simples": ("| Norma | Título | Texto |\n|---|---|---|",
                lambda n: f"| {n['codigo']} | {n['titulo']} | [abrir]({n['url']}) |"),
    "ifrs": ("| Norma | Título | CPC | NBC TG |\n|---|---|---|---|",
             lambda n: f"| {n['codigo']} | {n['titulo']} | {link_cpc(n['cpc'])} | {n['internacional']} |"),
}

out = [HEAD]
for i, s in enumerate(SECOES):
    cab, linha_norma = FORMATOS[s["formato"]]
    out.append(("" if i == 0 else "\n") + f"## {s['titulo']}\n\n" + (s["intro"] + "\n\n" if s["intro"] else "") + cab)
    out += [linha_norma(n) for n in NORMAS if n["secao"] == s["secao"]]
out.append("\nAs **NBC TA** seguem a mesma numeração das **ISA** do IAASB (ex.: NBC TA 700 = ISA 700). "
           "Textos das ISA: <https://www.iaasb.org/>.")
out.append("""
## Manutenção
Repositório mantido exclusivamente pelo autor; não são aceitas contribuições externas (issues desativadas e pull requests e comentários restritos ao autor).
Última conferência do índice: 2026-10-23.

## Licença
O índice (organização e metadados) está em domínio público sob [CC0 1.0](LICENSE).
Os textos das normas pertencem aos respectivos titulares.
""")

# ---------- registros estruturados ----------
VAZIO = ("", "—", "Framework")
serie_da = {s["secao"]: s["serie"] for s in SECOES}
REC = []
for n in NORMAS:
    serie = n["codigo"].split()[0] if serie_da[n["secao"]] == "(prefixo do código)" else serie_da[n["secao"]]
    REC.append({"codigo": n["codigo"], "titulo": n["titulo"], "serie": serie, "url": n["url"],
                "cpc": None if n["cpc"] in VAZIO else n["cpc"],
                "internacional": None if n["internacional"] in VAZIO else n["internacional"]})

# ---------- o que cada norma trata e afeta (colunas resumo/afeta; IFRS sem resumo herda da NBC TG equivalente) ----------
POR_COD = {sem_rev(n["codigo"]): n for n in NORMAS}
faltando = []
for r, n in zip(REC, NORMAS):
    fonte = n if n["resumo"] else POR_COD.get(sem_rev(r["internacional"] or ""), {})
    if not fonte.get("resumo"):
        faltando.append(r["codigo"])
    r["resumo"], r["afeta"] = fonte.get("resumo", ""), fonte.get("afeta", "")
    r["url_cpc"] = CPC_URL.get(_ncpc(r["cpc"])) if r["cpc"] else None
assert not faltando, f"normas.csv: sem resumo: {faltando}"

# ---------- situação (coluna situacao: vazio = vigente; texto = motivo da revogação) ----------
for r, n in zip(REC, NORMAS):
    r["situacao"] = n["situacao"] or "vigente"
    if r["situacao"] != "vigente":
        r["resumo"] = "⚠ " + r["situacao"] + " " + r["resumo"]

# ---------- áreas (dados/areas.csv) ----------
AREAS_CSV = ler("areas.csv")
QUANDO = {a["area"]: a["use_para"] for a in AREAS_CSV if a["use_para"]}
AREA_SERIE = {s.strip(): a["area"] for a in AREAS_CSV for s in a["series"].split(",") if s.strip()}

# ---------- temas (dados/temas.csv: regex no título + normas extras + sinônimos) ----------
TEMAS_CSV = ler("temas.csv")
TEMAS = [(t["tema"], t["area"], t["regex"] or None, t["sinonimos"]) for t in TEMAS_CSV]
TEMA_COD = {t["tema"]: [c.strip() for c in t["normas_extras"].split(",") if c.strip()] for t in TEMAS_CSV if t["normas_extras"]}
# temas de auditoria/profissão só valem para normas dessas séries (evita "Relatório Financeiro" virar relatório do auditor)
TEMAS_AUDITORIA = {t["tema"] for t in TEMAS_CSV if t["so_auditoria"].lower() == "sim"}
SERIES_CONTABEIS = {"NBC TG", "ITG", "CTG", "OTG", "Específicas", "PME", "NBC TSP", "IFRS/IAS"}

def norm(s):
    return unicodedata.normalize("NFC", s.lower())

CONTABIL_FALLBACK = "Contabilidade Geral"
for r in REC:
    t = norm(r["titulo"])
    cod = re.sub(r"\s*\(R\d+\)", "", r["codigo"]).strip()
    r["temas"] = [nome for nome, _, rx, _ in TEMAS
                  if (rx and re.search(rx, t) or cod in TEMA_COD.get(nome, []))
                  and not (nome in TEMAS_AUDITORIA and (r["serie"] in SERIES_CONTABEIS or r["serie"].startswith("CTSP")))]
    areas = []
    if r["serie"] in AREA_SERIE:
        areas.append(AREA_SERIE[r["serie"]])
    for nome, area, _, _ in TEMAS:
        if nome in r["temas"] and area not in areas and r["serie"] not in ("NBC TA", "NBC TR", "NBC TO", "NBC TSC", "NBC PA", "NBC PG", "NBC PP", "NBC TP", "NBC TI"):
            areas.append(area)
    r["areas"] = areas or [CONTABIL_FALLBACK]

SINONIMOS = {nome: sin for nome, _, _, sin in TEMAS}
AREA_DO_TEMA = {nome: area for nome, area, _, _ in TEMAS}

# ---------- pastas por setor (dados/setores*.csv) ----------
import gerar_setores
SETORES_GER = gerar_setores.gerar_todos(ROOT, REC, sem_rev)   # [(nome, pasta, use_para, [(arq, titulo)])]

(ROOT / "normas.json").write_text(json.dumps({
    "descricao": "Índice das normas contábeis e de auditoria brasileiras (CFC/CPC) e internacionais (IFRS/IAS), por área e tema.",
    "atualizado_em": "2026-10-23",
    "temas": [{"tema": n, "area": a, "sinonimos": s} for n, a, _, s in TEMAS],
    "normas": REC,
}, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- pasta areas/ (um arquivo por área) ----------
from collections import defaultdict
por_area = defaultdict(list)
for r in REC:
    for a in r["areas"]:
        por_area[a].append(r)
ordem = sorted(por_area, key=lambda a: (a == "Normas Internacionais", a))

DEMOS = [("BP", "Balanço patrimonial"), ("DRE", "Demonstração do resultado"), ("DRA", "Resultado abrangente / ORA"),
         ("DMPL", "Mutações do patrimônio líquido"), ("DFC", "Fluxos de caixa"), ("DVA", "Valor adicionado"),
         ("NE", "Notas explicativas"), ("DVP", "Variações patrimoniais (setor público)")]

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

import shutil
pasta = ROOT / "areas"
shutil.rmtree(pasta, ignore_errors=True); pasta.mkdir()
(ROOT / "AREAS.md").unlink(missing_ok=True)

def linha(r):
    refs = " · ".join(x for x in ((link_cpc(r["cpc"]) if r["cpc"] else None), r["internacional"]) if x) or "—"
    return f"| **{r['codigo']}** – {r['titulo']} | {r['resumo']} | {r['afeta']} | {refs} | [abrir]({r['url']}) |"

for a in ordem:
    temas_a = [(n, s) for n, ar, _, s in TEMAS if ar == a and any(n in r["temas"] for r in por_area[a])]
    md = [f"# Área: {a}\n",
          f"**Use esta área para:** {QUANDO.get(a, a)}.\n",
          f"{len(por_area[a])} normas. Índice de todas as áreas: [areas/README.md](README.md).\n"]
    if temas_a:
        md.append("## Temas desta área\n\n| Tema | Também chamado de | Normas |\n|---|---|---|")
        for n, sin in temas_a:
            md.append(f"| {n} | {sin} | {', '.join(r['codigo'] for r in por_area[a] if n in r['temas'])} |")
    md.append("\n## Normas\n\n| Norma | O que trata | Afeta | CPC / Internacional | Texto |\n|---|---|---|---|---|")
    md += [linha(r) for r in por_area[a]]
    (pasta / f"{slug(a)}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

idx = ["# Índice por área\n",
       "Cada área tem um arquivo com o resumo de cada norma, o que ela afeta e o link oficial. "
       "Comece pela tabela abaixo; se souber só o assunto, use a busca por tema.\n",
       "## Áreas\n\n| Área | Use para | Normas | Arquivo |\n|---|---|---|---|"]
for a in ordem:
    idx.append(f"| **{a}** | {QUANDO.get(a, '')} | {len(por_area[a])} | [{slug(a)}.md]({slug(a)}.md) |")
idx.append("\n## Por setor\n\nTrechos das normas que importam para cada tipo de empresa, com itens, checklist e perguntas frequentes.\n\n"
           "| Setor | Use para | Pasta |\n|---|---|---|")
for nome, pst, usar, _ in SETORES_GER:
    idx.append(f"| **{nome}** | {usar} | [{pst}/README.md](../{pst}/README.md) |")
idx.append("\n## Apoio\n\n| Arquivo | Use para |\n|---|---|\n"
           "| [GLOSSARIO.md](../GLOSSARIO.md) | significado de siglas (CPV, CIF, VRL, MEP, ORA, PCLD, UGC, MPM…) |\n"
           "| [lancamentos/README.md](../lancamentos/README.md) | exemplos de lançamentos contábeis (débito e crédito) por tema |\n"
           "| [reforma-tributaria.md](reforma-tributaria.md) | IBS, CBS e a OT CFC 01/2026 |")
idx.append("\n## Busca por tema\n\n| Tema | Também chamado de | Área | Normas |\n|---|---|---|---|")
for nome, area, _, sin in TEMAS:
    cods = [r["codigo"] for r in REC if nome in r["temas"]]
    if cods:
        idx.append(f"| **{nome}** | {sin} | [{area}]({slug(area)}.md) | {', '.join(cods)} |")
idx.append("\n## Busca por demonstração afetada\n\nNormas contábeis brasileiras que mudam cada demonstração.\n\n"
           "| Demonstração | Normas |\n|---|---|")
for sig, nome in DEMOS:
    cods = [r["codigo"] for r in REC if r["serie"] != "IFRS/IAS" and re.search(rf"\b{sig}\b", r["afeta"])]
    idx.append(f"| **{sig}** – {nome} | {', '.join(cods)} |")
(pasta / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
# páginas escritas à mão (scripts/conteudo/*.md) entram na pasta areas/
for extra in (Path(__file__).resolve().parent / "conteudo").glob("*.md"):
    (pasta / extra.name).write_text(extra.read_text(encoding="utf-8"), encoding="utf-8")

# ---------- normas/: um arquivo por série + lista A–Z ----------
PASTA_NORMAS = ROOT / "normas"
shutil.rmtree(PASTA_NORMAS, ignore_errors=True); PASTA_NORMAS.mkdir()
area_de = {r["codigo"]: r["areas"][0] for r in REC}
sit_de = {r["codigo"]: r["situacao"] for r in REC}
arq_secao = {}
for s in SECOES:
    arq = slug(s["titulo"]) + ".md"
    arq_secao[s["secao"]] = arq
    cab, linha_norma = FORMATOS[s["formato"]]
    itens = [n for n in NORMAS if n["secao"] == s["secao"]]
    md = [f"# {s['titulo']}\n", (s["intro"] + "\n") if s["intro"] else "",
          f"{len(itens)} normas. [← Todas as normas](README.md) · [Página inicial](../README.md)\n", cab]
    md += [linha_norma(n) for n in itens]
    if s["formato"] == "ta":
        md.append("\nAs **NBC TA** seguem a mesma numeração das **ISA** do IAASB (ex.: NBC TA 700 = ISA 700).")
    (PASTA_NORMAS / arq).write_text("\n".join(x for x in md if x != "") + "\n", encoding="utf-8")

az = ["# Todas as normas\n",
      "Procure pelo código (no navegador, **Ctrl+F**). Cada norma aponta para a área onde está explicada e para o texto oficial. "
      "⚠ = revogada.\n",
      "## Por série\n\n| Série | Normas | Arquivo |\n|---|---|---|"]
for s in SECOES:
    k = sum(1 for n in NORMAS if n["secao"] == s["secao"])
    az.append(f"| {s['titulo']} | {k} | [{arq_secao[s['secao']]}]({arq_secao[s['secao']]}) |")
az.append("\n## Lista A–Z\n\n| Código | Título | Área | Texto oficial |\n|---|---|---|---|")
def _ordem(n):
    return [int(x) if x.isdigit() else x for x in re.findall(r"\d+|\D+", n["codigo"])]
for n in sorted(NORMAS, key=_ordem):
    a = area_de[n["codigo"]]
    aviso = "⚠ " if sit_de[n["codigo"]] != "vigente" else ""
    az.append(f"| {aviso}**{n['codigo']}** | {n['titulo']} | [{a}](../areas/{slug(a)}.md) | [abrir]({n['url']}) |")
(PASTA_NORMAS / "README.md").write_text("\n".join(az) + "\n", encoding="utf-8")

# ---------- README.md: página inicial curta ----------
setores_md = "\n".join(f"| [{nome}]({pst}/README.md) | {usar} |" for nome, pst, usar, _ in SETORES_GER)
areas_md = "\n".join(f"| [{a}](areas/{slug(a)}.md) | {QUANDO.get(a, '')} |" for a in ordem)
README = f"""# Normas Contábeis Brasileiras

Índice das normas contábeis e de auditoria do Brasil (**CFC** e **CPC**) e das internacionais (**IFRS**, **IAS**, **ISA**):
o que cada norma trata, o que ela afeta, os trechos por setor, exemplos de lançamentos e o link para o texto oficial.

> O texto integral das normas não está aqui (direitos autorais): cada norma tem um resumo e o link oficial.
> Confira sempre a versão vigente. Este índice não é aconselhamento profissional.

## Como achar o que você precisa

| Você tem… | Vá para |
|---|---|
| **o código** da norma (ex.: NBC TG 27, CPC 47, IAS 16, NBC TA 700) | [**normas/**](normas/README.md): lista A–Z com {len(NORMAS)} normas e um arquivo por série |
| **o assunto** (ex.: imobilizado, leasing, receita, IR diferido) | [**areas/**](areas/README.md): normas por área, busca por tema com sinônimos e por demonstração (DRE, DFC…) |
| **o tipo de empresa** (indústria, varejo, banco…) | [**setores/**](setores/README.md): trechos das normas que importam para cada setor |
| **um lançamento** para fazer | [**lancamentos/**](lancamentos/README.md): débito e crédito com a norma de cada um |
| **uma sigla** que não conhece | [**GLOSSARIO.md**](GLOSSARIO.md) |
| **reforma tributária** (IBS e CBS) | [**areas/reforma-tributaria.md**](areas/reforma-tributaria.md) |

Também dá para usar a busca do GitHub (tecla **/** ou **t** para procurar arquivos) ou o
[**mapa interativo**](https://caponeygo.github.io/normas-contabeis-brasil/graphify-out/graph.html).

## Por setor

| Setor | Use para |
|---|---|
{setores_md}

## Por área

| Área | Use para |
|---|---|
{areas_md}

## O que tem em cada pasta

| Pasta / arquivo | Conteúdo |
|---|---|
| `normas/` | Índice de todas as normas, por série e em ordem alfabética |
| `areas/` | Uma página por área de assunto, com resumo de cada norma |
| `setores/` | Uma pasta por setor, com os itens das normas, checklist e perguntas frequentes |
| `lancamentos/` | Exemplos de lançamentos contábeis |
| `GLOSSARIO.md` | Siglas e termos |
| `normas.json` | Todos os dados em JSON (para sistemas e IA) |
| `AGENTS.md` | Instruções para assistentes de IA (Copilot, Claude etc.) |
| `dados/` | Planilhas que geram tudo (manutenção) |
| `scripts/`, `testes/`, `verificacao/`, `graphify-out/` | Geradores, testes e relatórios automáticos (manutenção) |

## Fontes oficiais
- CFC, Normas Brasileiras de Contabilidade: <https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/>
- CPC: <https://www.cpc.org.br>
- CVM: <https://www.gov.br/cvm>
- Banco Central (normas contábeis): <https://www3.bcb.gov.br/aplica/cosif>
- IFRS Foundation: <https://www.ifrs.org/issued-standards/list-of-standards/>
- IAASB: <https://www.iaasb.org/>

`CPC 26 (R1)` é o pronunciamento do CPC; o CFC o torna obrigatório como `NBC TG 26 (R5)`. `(Rn)` indica a revisão.
As `ICPC` correspondem às `ITG` e as `OCPC` aos `CTG`.

## Manutenção
Repositório mantido exclusivamente pelo autor; não são aceitas contribuições externas (issues desativadas e pull requests e comentários restritos ao autor).
Última conferência do índice: 2026-10-23.

## Licença
O índice (organização e metadados) está em domínio público sob [CC0 1.0](LICENSE).
Os textos das normas pertencem aos respectivos titulares.
"""
(ROOT / "README.md").write_text(README, encoding="utf-8")
_set = ["# Normas por setor\n",
        "Cada pasta traz os trechos das normas que importam para o setor, com os itens, um checklist e perguntas frequentes.\n",
        "| Setor | Use para |\n|---|---|"]
_set += [f"| [{nome}]({pst.split('/', 1)[1]}/README.md) | {usar} |" for nome, pst, usar, _ in SETORES_GER]
_set.append("\n[Página inicial](../README.md) · [Todas as áreas](../areas/README.md) · [Todas as normas](../normas/README.md)")
(ROOT / "setores" / "README.md").write_text("\n".join(_set) + "\n", encoding="utf-8")


# instruções para IA: mesmo texto para Copilot, Claude e outros agentes
ag = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
(ROOT / "CLAUDE.md").write_text(ag, encoding="utf-8")
(ROOT / ".github").mkdir(exist_ok=True)
# a cópia fica em .github/: links relativos ganham "../" para continuarem válidos
ag_github = re.sub(r"\]\((?!https?:|#|\.\./)([^)]+)\)", r"](../\1)", ag)
(ROOT / ".github" / "copilot-instructions.md").write_text(ag_github, encoding="utf-8")

# ---------- extração para o graphify (determinística, sem LLM) ----------
SRC = "normas.json"
def nid(prefix, s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return prefix + "_" + re.sub(r"[^a-z0-9]+", "_", s).strip("_")
nodes, edges, seen = [], [], set()
def node(i, label, kind):
    if i not in seen:
        seen.add(i)
        nodes.append({"id": i, "label": label, "file_type": "concept" if kind != "norma" else "document",
                      "source_file": SRC, "source_location": None, "source_url": None, "captured_at": None,
                      "author": None, "contributor": None, "kind": kind})
    return i
def edge(a, b, rel, conf="EXTRACTED", score=1.0):
    edges.append({"source": a, "target": b, "relation": rel, "confidence": conf,
                  "confidence_score": score, "source_file": SRC, "source_location": None, "weight": 1.0})
def code_id(c):
    return nid("norma", re.sub(r"\s*\(R\d+\)", "", c))
for a in ordem:
    node(nid("area", a), f"Área: {a}", "area")
for nome, area, _, sin in TEMAS:
    t = node(nid("tema", nome), f"{nome} ({sin})", "tema")
    edge(t, node(nid("area", area), f"Área: {area}", "area"), "parte_da_area")
for r in REC:
    n = node(code_id(r["codigo"]), f"{r['codigo']} – {r['titulo']}", "norma")
    for a in r["areas"]:
        edge(n, nid("area", a), "pertence_a_area")
    for t in r["temas"]:
        edge(n, nid("tema", t), "trata_de")
    for ref in (r["cpc"], r["internacional"]):
        if ref:
            edge(n, node(code_id(ref), ref, "norma"), "equivale_a")
    if r["serie"] != "IFRS/IAS":
        for sig, nome in DEMOS:
            if re.search(rf"\b{sig}\b", r["afeta"]):
                edge(n, node(nid("demo", sig), f"Demonstração: {sig} ({nome})", "demonstracao"), "afeta")
for nome, pst, usar, tops in SETORES_GER:
    setor = node(nid("setor", nome), f"Setor: {nome} ({usar})", "setor")
    for arq, titulo in tops:
        edge(node(nid("topico_" + pst, titulo), f"{nome}: {titulo}", "topico_setor"), setor, "parte_do_setor")
for r in REC:
    for x in {(x["pasta"], x["topico"]) for x in r["setores"]}:
        edge(code_id(r["codigo"]), nid("topico_" + x[0], x[1]), "aplica_no_setor")
(ROOT / "graphify-out").mkdir(exist_ok=True)
(ROOT / "graphify-out" / ".graphify_extract.json").write_text(json.dumps(
    {"nodes": nodes, "edges": edges, "hyperedges": [], "input_tokens": 0, "output_tokens": 0}, ensure_ascii=False), encoding="utf-8")
print(f"{len(REC)} normas, {len(TEMAS)} temas, {len(ordem)} áreas; grafo: {len(nodes)} nós, {len(edges)} arestas")
sem = [r["codigo"] for r in REC if not r["temas"]]
print("sem tema:", sem)
