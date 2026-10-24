# Gera README.md, areas/, as pastas por setor, normas.json e a extração do grafo a partir das planilhas em dados/.
# As planilhas (CSV separado por ";", abrem no Excel) são a fonte dos dados: edite lá e rode
#     python manutencao/scripts/reconstruir.py
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dados import ler  # noqa: E402


def sem_rev(c):
    return re.sub(r"\s*\(R\d+\)", "", c).strip()


# links oficiais do CPC (scripts/cpc.json, gerado por scripts/atualizar_cpc.py)
def _ncpc(c):
    return sem_rev(c or "").replace(" ", "").upper()


_cpcj = ROOT / "manutencao" / "scripts" / "cpc.json"
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


def _iso(d):
    dd, mm, aa = d.split("/")
    return f"{aa}-{mm}-{dd}"


def vigencia(sit):
    """Campos estruturados a partir do texto de 'situacao' (datas em ISO, vazio = não informado)."""
    v = {"status": "vigente" if sit == "vigente" else "revogada", "substituida_por": None,
         "revogada_em": None, "substituta_vale_a_partir_de": None, "vigente_a_partir_de": None,
         "observacao_vigencia": None}
    if sit == "vigente":
        return v
    d = re.search(r"(\d{2}/\d{2}/\d{4})", sit)
    if sit.startswith("Ainda não vigente"):        # ex.: "Ainda não vigente: vale a partir de 15/12/2026."
        v["status"] = "futura"
        v["vigente_a_partir_de"] = _iso(d.group(1)) if d else None
        return v
    if sit.startswith("Será revogada"):            # ex.: "Será revogada em 15/12/2026 e substituída por: PCAOB QC 1000."
        v["status"] = "vigente"
        v["revogada_em"] = _iso(d.group(1)) if d else None
        m = re.search(r"substituída por: (.+?)\.?$", sit)
        v["substituida_por"] = m.group(1).strip() if m else None
        return v
    if sit.startswith("Vigente;"):                 # vigente, com observação (ex.: parágrafo que muda numa data)
        v["status"] = "vigente"
        v["observacao_vigencia"] = sit
        return v
    m = re.match(r"Revogada pela? (.+?)(?: \(|\.|,|$)", sit)
    v["substituida_por"] = m.group(1).strip() if m else None
    m = re.search(r"DOU (\d{2}/\d{2}/\d{4})", sit) or re.search(r"(\d{2}/\d{2}/\d{4})", sit)
    if m:
        v["revogada_em"] = _iso(m.group(1))
    else:
        m = re.search(r"\((\d{4})\)", sit)
        v["revogada_em"] = m.group(1) if m else None            # só o ano
    m = re.search(r"a partir de (\d{1,2}/\d{1,2}/\d{4})", sit)
    if m:
        d, mo, a = m.group(1).split("/")
        v["substituta_vale_a_partir_de"] = f"{a}-{int(mo):02d}-{int(d):02d}"
    return v

# ---------- situação (coluna situacao: vazio = vigente; texto = motivo da revogação) ----------
for r, n in zip(REC, NORMAS):
    r["situacao"] = n["situacao"] or "vigente"
    r.update(vigencia(r["situacao"]))
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

# ---------- relações "mesmo assunto" (dados/relacoes.csv, ex.: PCAOB AS 2401 e NBC TA 240) ----------
# Não são equivalências: tratam do mesmo assunto e podem diferir. A norma herda também as áreas da norma relacionada.
_por_cod = {sem_rev(r["codigo"]): r for r in REC}
for r in REC:
    r["relacionadas"] = []
for rel in ler("relacoes.csv"):
    a, b = _por_cod[sem_rev(rel["de"])], _por_cod[sem_rev(rel["para"])]
    if b["codigo"] not in a["relacionadas"]:
        a["relacionadas"].append(b["codigo"])
    if a["codigo"] not in b["relacionadas"]:
        b["relacionadas"].append(a["codigo"])
    for area in b["areas"]:
        if area not in a["areas"]:
            a["areas"].append(area)

# ---------- pastas por setor (dados/setores*.csv) ----------
import gerar_setores
SETORES_GER = gerar_setores.gerar_todos(ROOT, REC, sem_rev)   # [(nome, pasta, use_para, [(arq, titulo)])]
# padrões do PCAOB não têm trechos por setor: herdam, "por assunto", os setores das normas relacionadas
for r in REC:
    proprios = {x["setor"] for x in r["setores"]}
    r["setores_assunto"] = sorted({x["setor"] for c in r["relacionadas"] for x in _por_cod[sem_rev(c)]["setores"]} - proprios) if r["serie"] == "PCAOB" else []

(ROOT / "normas.json").write_text(json.dumps({
    "descricao": "Índice das normas contábeis e de auditoria brasileiras (CFC/CPC) e internacionais (IFRS/IAS), por área e tema.",
    "atualizado_em": "2026-10-23",
    "regra_vigencia": "status=revogada: não use a norma para exercícios atuais, use substituida_por. status=futura: ainda não vale, só a partir de vigente_a_partir_de. status=vigente com revogada_em: vale até essa data (se for futura), depois use substituida_por. Se substituta_vale_a_partir_de existir, a norma revogada continua válida para exercícios anteriores a essa data. revogada_em pode ter só o ano.",
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
FICHA = {r["codigo"]: slug(r["codigo"]) for r in REC}
assert len(set(FICHA.values())) == len(FICHA), "ficha: código repetido após slug"
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
    az.append(f"| {aviso}[**{n['codigo']}**](ficha/{FICHA[n['codigo']]}.md) | {n['titulo']} | [{a}](../areas/{slug(a)}.md) | [abrir]({n['url']}) |")
(PASTA_NORMAS / "README.md").write_text("\n".join(az) + "\n", encoding="utf-8")

# ---------- normas/ficha/: uma ficha por norma (leitura barata e sem ambiguidade para IA) ----------
(PASTA_NORMAS / "ficha").mkdir()
_CONF_TXT = {"auto": "✅ conferido", "manual": "✅👤 revisado por pessoa", "pendente": "⚠ revisar", "nao_conferido": "⚠ não conferido"}
for r in REC:
    resumo = r["resumo"]
    if r["situacao"] != "vigente":
        resumo = resumo.removeprefix("⚠ " + r["situacao"] + " ")
    fm = ["---", f"codigo: {json.dumps(r['codigo'], ensure_ascii=False)}", f"titulo: {json.dumps(r['titulo'], ensure_ascii=False)}",
          f"serie: {json.dumps(r['serie'], ensure_ascii=False)}", f"status: {r['status']}"]
    for k in ("substituida_por", "revogada_em", "substituta_vale_a_partir_de", "vigente_a_partir_de", "observacao_vigencia"):
        if r.get(k):
            fm.append(f"{k}: {json.dumps(r[k], ensure_ascii=False)}")
    if r["cpc"]:
        fm.append(f"cpc: {json.dumps(r['cpc'], ensure_ascii=False)}")
    if r["internacional"]:
        fm.append(f"internacional: {json.dumps(r['internacional'], ensure_ascii=False)}")
    fm += [f"url_oficial: {r['url']}", "---", ""]
    md = fm + [f"# {r['codigo']} – {r['titulo']}\n"]
    if r["situacao"] != "vigente":
        rotulo = {"revogada": "REVOGADA.", "futura": "AINDA NÃO VIGENTE."}.get(r["status"], "ATENÇÃO À VIGÊNCIA.")
        md.append(f"> ⚠ **{rotulo}** {r['situacao']}\n")
    md.append(f"**O que trata:** {resumo}\n")
    md.append(f"**O que afeta:** {r['afeta']}\n")
    eq = [x for x in (r["cpc"], r["internacional"]) if x]
    if eq:
        md.append("**Equivalentes:** " + " · ".join(eq) + "\n")
    md.append("**Áreas:** " + ", ".join(f"[{a}](../../areas/{slug(a)}.md)" for a in r["areas"]) + "\n")
    if r["setores_assunto"]:
        md.append("**Setores (por assunto, via normas relacionadas):** " + ", ".join(r["setores_assunto"]) + chr(10))
    if r["temas"]:
        md.append("**Temas:** " + ", ".join(r["temas"]) + "\n")
    if r["setores"]:
        md.append("## Trechos por setor\n\n| Setor | Tópico | Itens | Conferência |\n|---|---|---|---|")
        for x in r["setores"]:
            md.append(f"| {x['setor']} | [{x['topico']}](../../{x['arquivo']}) | {x['itens']} | {_CONF_TXT[x['conferencia']]} |")
        md.append("")
    if r["relacionadas"]:
        NL = chr(10)
        md.append("## Mesmo assunto em outras normas" + NL + NL + "Tratam do mesmo tema, mas não são equivalentes: leia as duas." + NL)
        md += [f"- [{x}]({FICHA[x]}.md)" for x in r["relacionadas"]]
        md.append("")
    md.append(f"## Fonte\n\n- [Texto oficial (CFC)]({r['url']})")
    if r.get("url_cpc"):
        md.append(f"- [Pronunciamento do CPC]({r['url_cpc']})")
    md.append("\n[← Todas as normas](../README.md) · [Página inicial](../../README.md)")
    (PASTA_NORMAS / "ficha" / (FICHA[r["codigo"]] + ".md")).write_text("\n".join(md) + "\n", encoding="utf-8")

# ---------- normas/mudancas-futuras.md: o que será revogado ou ainda não vale ----------
ATUAL = "2026-10-23"          # mesma data de "atualizado_em" em normas.json


def _br(d):
    p = (d or "").split("-")
    return f"{p[2]}/{p[1]}/{p[0]}" if len(p) == 3 else (d or "")


def _lnk(cod, de="ficha/"):
    return f"[{cod}]({de}{FICHA[cod]}.md)" if cod in FICHA else (cod or "—")


_futuro = lambda d: bool(d) and len(d) == 10 and d > ATUAL
_serao = sorted((r for r in REC if r["status"] == "vigente" and _futuro(r.get("revogada_em"))), key=lambda r: (r["revogada_em"], r["codigo"]))
_novas = sorted((r for r in REC if r["status"] == "futura"), key=lambda r: (r.get("vigente_a_partir_de") or "", r["codigo"]))
_trans = [r for r in REC if r["status"] == "revogada" and _futuro(r.get("substituta_vale_a_partir_de"))]
_obs = [r for r in REC if r.get("observacao_vigencia")]
mf = ["# Normas que serão revogadas ou ainda não valem\n",
      f"Situação em {_br(ATUAL)}. Esta página é gerada das planilhas e lista só o que já está registrado nelas. "
      "Antes de aplicar uma norma, confira a data e o texto no link oficial.\n",
      "[← Todas as normas](README.md) · [Página inicial](../README.md)\n",
      "## Em vigor hoje, mas serão revogadas\n"]
if _serao:
    mf.append("| Norma | Título | Deixa de valer em | Substituída por |\n|---|---|---|---|")
    mf += [f"| {_lnk(r['codigo'])} | {r['titulo']} | {_br(r['revogada_em'])} | {_lnk(r['substituida_por'])} |" for r in _serao]
else:
    mf.append("Nenhuma registrada.")
mf.append("\n## Ainda não vigentes (já aprovadas)\n")
if _novas:
    mf.append("| Norma | Título | Vale a partir de | Observação |\n|---|---|---|---|")
    mf += [f"| {_lnk(r['codigo'])} | {r['titulo']} | {_br(r['vigente_a_partir_de'])} | {r['situacao']} |" for r in _novas]
else:
    mf.append("Nenhuma registrada.")
mf.append("\n## Já revogadas, com substituta que só vale mais tarde\n")
if _trans:
    mf.append("| Norma revogada | Substituída por | A substituta vale a partir de |\n|---|---|---|")
    mf += [f"| {_lnk(r['codigo'])} | {_lnk(r['substituida_por'])} | {_br(r['substituta_vale_a_partir_de'])} |" for r in _trans]
    mf.append("\nA norma revogada continua válida para os exercícios anteriores a essa data.")
else:
    mf.append("Nenhuma registrada.")
mf.append("\n## Vigentes, com trecho que muda\n")
if _obs:
    mf.append("| Norma | Título | O que muda |\n|---|---|---|")
    mf += [f"| {_lnk(r['codigo'])} | {r['titulo']} | {r['observacao_vigencia']} |" for r in _obs]
else:
    mf.append("Nenhuma registrada.")
mf.append("\n## Como esta lista é mantida\n\n"
          "- Os dados vêm da coluna `situacao` de `manutencao/dados/normas.csv`: `Será revogada em DD/MM/AAAA e substituída por: CÓDIGO.`, "
          "`Ainda não vigente: vale a partir de DD/MM/AAAA.` ou `Vigente; <observação>`.\n"
          "- Hoje estão registradas aqui as mudanças dos padrões do PCAOB e a transição da NBC TG 26 para a NBC TG 51. O robô do CFC avisa de normas novas e de revogações já publicadas, "
          "mas não de revogações futuras: quem mantém o índice precisa registrá-las nas planilhas.\n"
          "- Os links do PCAOB não são verificados automaticamente (o site bloqueia robôs).")
(PASTA_NORMAS / "mudancas-futuras.md").write_text("\n".join(mf) + "\n", encoding="utf-8")

# ---------- llms.txt: mapa curto para assistentes de IA ----------
(ROOT / "llms.txt").write_text("\n".join([
    "# Normas Contábeis Brasileiras",
    "",
    "> Índice (não o texto) das normas contábeis e de auditoria do Brasil (CFC/CPC) e das internacionais (IFRS/IAS/ISA) e dos padrões do PCAOB (EUA): "
    "resumo, o que afeta, equivalências, trechos por setor e link oficial. Não hospeda o texto integral das normas.",
    "",
    "Regras: leia `AGENTS.md` antes de responder; cite sempre o código da norma e o link oficial; "
    "não afirme item/parágrafo que não esteja nestes arquivos; normas com status=revogada têm substituta em `substituida_por`; "
    "trechos com ⚠ na coluna Conferência devem ser confirmados no texto oficial; se algo não está aqui, diga que não está.",
    "",
    "## Entradas",
    "- [AGENTS.md](AGENTS.md): como usar este repositório e seus limites",
    "- [normas.json](normas.json): todos os dados estruturados (status, vigência, equivalências, trechos por setor)",
    "- [normas/README.md](normas/README.md): lista A–Z; cada norma tem ficha em normas/ficha/<código>.md",
    "- [normas/mudancas-futuras.md](normas/mudancas-futuras.md): normas que serão revogadas ou ainda não valem, com datas",
    "- [areas/README.md](areas/README.md): busca por assunto, sinônimo e demonstração afetada",
    "- [setores/README.md](setores/README.md): trechos por setor com selo de conferência",
    "- [lancamentos/README.md](lancamentos/README.md): exemplos de lançamentos",
    "- [GLOSSARIO.md](GLOSSARIO.md): siglas",
]) + "\n", encoding="utf-8")

# ---------- README.md: página inicial curta ----------
setores_md = "\n".join(f"| [{nome}]({pst}/README.md) | {usar} |" for nome, pst, usar, _ in SETORES_GER)
areas_md = "\n".join(f"| [{a}](areas/{slug(a)}.md) | {QUANDO.get(a, '')} |" for a in ordem)
README = f"""<div align="center">

# 📚 Normas Contábeis Brasileiras

**Índice navegável das normas do CFC e do CPC, das internacionais (IFRS, IAS, ISA) e dos padrões do PCAOB (EUA)**
o que cada norma trata, o que ela afeta, os trechos por setor, exemplos de lançamentos e o link para o texto oficial.

![Normas](https://img.shields.io/badge/normas-{len(NORMAS)}-1f6feb) ![Áreas](https://img.shields.io/badge/áreas-{len(ordem)}-8250df) ![Setores](https://img.shields.io/badge/setores-{len(SETORES_GER)}-2da44e) ![Licença](https://img.shields.io/badge/índice-CC0%201.0-lightgrey)

[🔎 Por código](normas/README.md) · [🧭 Por assunto](areas/README.md) · [🏭 Por setor](setores/README.md) · [🧾 Lançamentos](lancamentos/README.md) · [📖 Glossário](GLOSSARIO.md) · [🕸️ Mapa interativo](https://caponeygo.github.io/normas-contabeis-brasil/mapa.html)

</div>

## 🚀 Por onde começar

| Você tem… | Vá para |
|---|---|
| 🔎 **o código** da norma (ex.: NBC TG 27, CPC 47, IAS 16, NBC TA 700) | [**normas/**](normas/README.md): lista A–Z com {len(NORMAS)} normas e um arquivo por série |
| 🧭 **o assunto** (ex.: imobilizado, leasing, receita, IR diferido) | [**areas/**](areas/README.md): normas por área, busca por tema com sinônimos e por demonstração (DRE, DFC…) |
| 🏭 **o tipo de empresa** (indústria, varejo, banco…) | [**setores/**](setores/README.md): trechos das normas que importam para cada setor |
| 🧾 **um lançamento** para fazer | [**lancamentos/**](lancamentos/README.md): débito e crédito com a norma de cada um |
| 🔤 **uma sigla** que não conhece | [**GLOSSARIO.md**](GLOSSARIO.md) |
| 📅 **o que vai mudar** (normas que serão revogadas ou ainda não valem) | [**normas/mudancas-futuras.md**](normas/mudancas-futuras.md) |
| 🏛️ **reforma tributária** (IBS e CBS) | [**areas/reforma-tributaria.md**](areas/reforma-tributaria.md) |

Dica: no GitHub, a tecla **/** busca no repositório e **t** procura arquivos pelo nome.

## 🏭 Por setor

| Setor | Use para |
|---|---|
{setores_md}

## 🧭 Por área

<details>
<summary><b>Ver as {len(ordem)} áreas</b></summary>

| Área | Use para |
|---|---|
{areas_md}

</details>

## 🗂️ O que tem em cada pasta

```text
normas-contabeis-brasil/
├── normas/        índice de todas as normas, por série, em ordem alfabética e uma ficha por norma (normas/ficha/)
├── areas/         uma página por área de assunto, com resumo de cada norma
├── setores/       uma pasta por setor: itens das normas, checklist e perguntas frequentes
├── lancamentos/   exemplos de lançamentos contábeis
├── GLOSSARIO.md   siglas e termos
├── normas.json    todos os dados em JSON (para sistemas e IA)
├── llms.txt       mapa curto do repositório para assistentes de IA
├── AGENTS.md      instruções para assistentes de IA (Copilot, Claude etc.)
└── manutencao/    planilhas, scripts, testes, relatórios e mapa (geram tudo; não precisa abrir)
```

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

print(f"{len(REC)} normas, {len(TEMAS)} temas, {len(ordem)} áreas")
sem = [r["codigo"] for r in REC if not r["temas"]]
print("sem tema:", sem)
