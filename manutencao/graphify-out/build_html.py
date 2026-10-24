# Gera graph.html: UM círculo com uma bolinha por NORMA, agrupadas por ÁREA (bolinha maior com contorno).
# As áreas da mesma série (cor) ficam lado a lado; ligações em curva: equivalências (NBC TG ↔ CPC ↔ IFRS),
# áreas secundárias e, com a opção marcada, normas que tratam do mesmo tema.
# Rodar da raiz do projeto: python graphify-out/build_html.py
import json, math, re
from pathlib import Path

d = json.loads(Path('normas.json').read_text(encoding='utf-8'))
NORMAS, TEMAS = d['normas'], {t['tema']: t for t in d['temas']}

CATS = [
    ('soc', 'Contabilidade (NBC TG / ITG / CTG)', '#9d8cff'),
    ('cpc', 'CPC (pronunciamentos)',              '#c4b5fd'),
    ('pme', 'Pequenas e Médias Empresas',         '#f28fb4'),
    ('pub', 'Setor Público (NBC TSP)',            '#34d399'),
    ('sus', 'Sustentabilidade (NBC TDS)',         '#a3e635'),
    ('aud', 'Auditoria Independente (NBC TA)',    '#5aa9f0'),
    ('isa', 'ISA (IAASB)',                        '#93c5fd'),
    ('ass', 'Revisão, Asseguração e Correlatos',  '#f0b464'),
    ('per', 'Auditoria Interna e Perícia',        '#e6d15a'),
    ('eti', 'Ética e Exercício Profissional',     '#94a3b8'),
    ('int', 'IFRS / IAS (IASB)',                  '#fb7185'),
]
ORDEM = [c[0] for c in CATS]
CAT_AREA = {
    'Pequenas e Médias Empresas': 'pme', 'Setor Público': 'pub', 'Sustentabilidade': 'sus',
    'Auditoria Independente': 'aud', 'Revisão': 'ass', 'Asseguração': 'ass', 'Serviços Correlatos': 'ass',
    'Auditoria Interna': 'per', 'Perícia Contábil': 'per', 'Ética e Exercício Profissional': 'eti',
    'Normas Internacionais': 'int',
}

def chave(c):                       # "NBC TG 27 (R4)" e "NBC TG 27" são a mesma norma
    return re.sub(r'\s*\(R\d+\)', '', c).strip()

import sys, unicodedata
sys.path.insert(0, 'manutencao/scripts')
from dados import ler
SETORES = [s['nome'] for s in ler('setores.csv')]
REPO = 'https://github.com/caponeygo/normas-contabeis-brasil/blob/main/'

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def arquivo_da_area(g):          # link da bolinha de área para o arquivo .md da área
    if g.startswith('Auditoria · ') or g == 'ISA (IAASB)':
        return REPO + 'areas/auditoria-independente.md'
    if g == 'CPC (pronunciamentos)':
        return REPO + 'README.md'
    return REPO + f'areas/{slug(g)}.md'

ents = {}
def ent(eid, label, cat, kind, path='', url=None, grupo=None, setores=()):
    if eid not in ents:
        ents[eid] = {'id': eid, 'label': label, 'cat': cat, 'kind': kind, 'path': path, 'url': url,
                     'grupo': grupo or eid, 'fn': [], 'set': set()}
        if kind == 'área':
            ents[eid]['url'] = arquivo_da_area(label)
    ents[eid]['set'] |= set(setores)
    return ents[eid]

# --- áreas e normas: cada norma entra no grupo da sua área principal ---
def grupo_da(n):
    a = n['areas'][0]
    if n['serie'] == 'NBC TA':      # 43 normas de auditoria: subdivide pelo tema
        return 'Auditoria · ' + (n['temas'][0] if n['temas'] else 'Princípios gerais')
    return a

for n in NORMAS:
    g = grupo_da(n)
    cat = CAT_AREA.get(n['areas'][0], 'soc')
    ent('a:' + g, g, cat, 'área')
    refs = ' · '.join(x for x in (n['cpc'], n['internacional']) if x)
    temas = '; '.join(f"{t} ({TEMAS[t]['sinonimos']})" for t in n['temas'])
    e = ent('n:' + chave(n['codigo']), n['codigo'], cat, 'norma',
            path=' · '.join(x for x in (n['titulo'], refs) if x) + f"<br><br>{n['resumo']}<br><br>Afeta: {n['afeta']}" + (f'<br>Temas: {temas}' if temas else '')
                 + (('<br><br><b>Setores:</b> ' + ' · '.join(sorted({x['setor'] + ': ' + x['topico'] for x in n.get('setores', [])}))) if n.get('setores') else ''),
            url=n['url'], grupo='a:' + g, setores=(x['setor'] for x in n.get('setores', [])))
    ents['a:' + g]['fn'].append(n['codigo'])

# --- CPC e ISA citados como equivalentes viram bolinhas próprias ---
for n in NORMAS:
    for ref, cat, grp in ((n['cpc'], 'cpc', 'CPC (pronunciamentos)'), (n['internacional'], 'isa', 'ISA (IAASB)')):
        if not ref or (cat == 'isa' and not ref.startswith('ISA')):
            continue
        if ('n:' + chave(ref)) in ents:                     # equivalente já criado: herda os setores
            ents['n:' + chave(ref)]['set'] |= {x['setor'] for x in n.get('setores', [])}
            continue
        ent('a:' + grp, grp, cat, 'área')
        ent('n:' + chave(ref), ref, cat, 'norma', path=f"Equivalente a {n['codigo']} · " + ents['n:' + chave(n['codigo'])]['path'],
            grupo='a:' + grp, setores=(x['setor'] for x in n.get('setores', [])))
        ents['a:' + grp]['fn'].append(ref)

# --- ligações ---
pesos = {}
def liga(a, b, comum=0):
    if a == b or a not in ents or b not in ents:
        return
    k = tuple(sorted((a, b)))
    w, c = pesos.get(k, (0, 1))
    pesos[k] = (w + 1, min(c, comum))

for n in NORMAS:
    me = 'n:' + chave(n['codigo'])
    for ref in (n['cpc'], n['internacional']):
        if ref:
            liga(me, 'n:' + chave(ref))                       # equivalência
    for a in n['areas'][1:]:
        if 'a:' + a in ents:
            liga(me, 'a:' + a)                                # área secundária
por_tema = {}
for n in NORMAS:
    for t in n['temas']:
        por_tema.setdefault(t, []).append('n:' + chave(n['codigo']))
for t, ids in por_tema.items():
    if len(ids) <= 12:                                        # temas enormes viram ruído
        for i, a in enumerate(ids):
            for b in ids[i + 1:]:
                liga(a, b, comum=1)

grau = {}
for (a, b) in pesos:
    grau[a] = grau.get(a, 0) + 1; grau[b] = grau.get(b, 0) + 1

# --- layout: grupos por categoria, área primeiro e normas em ordem ---
def ordem_codigo(e):
    nums = [int(x) for x in re.findall(r'\d+', e['label'])]
    return (e['label'].split(' ')[0], nums, e['label'])
grupos = {}
for e in ents.values():
    grupos.setdefault(e['grupo'] if e['kind'] == 'norma' else e['id'], []).append(e)
for g, m in grupos.items():
    m.sort(key=lambda e: (0 if e['kind'] == 'área' else 1, ordem_codigo(e)))
blocos = {c: sorted([g for g in grupos if ents[g]['cat'] == c], key=lambda g: ents[g]['label'].lower()) for c in ORDEM}
GAP_GRUPO, GAP_CAT = 1.8, 4.5
pos, slot, primeiro = {}, 0.0, True
for c in ORDEM:
    if not blocos[c]:
        continue
    if not primeiro:
        slot += GAP_CAT - GAP_GRUPO
    primeiro = False
    for g in blocos[c]:
        for e in grupos[g]:
            pos[e['id']] = slot; slot += 1
        slot += GAP_GRUPO
total = slot + GAP_CAT
R = max(560, int(total * 17.0 / (2 * math.pi)))

saida = []
for e in sorted(ents.values(), key=lambda e: pos[e['id']]):
    area = e['kind'] == 'área'
    gr = grau.get(e['id'], 0) + (len(e['fn']) if area else 0)
    saida.append({
        'id': e['id'], 'label': e['label'], 'cat': e['cat'], 'path': e['path'], 'url': e['url'], 'kind': e['kind'],
        'fn': e['fn'], 'grau': gr, 'ang': round(-math.pi / 2 + 2 * math.pi * pos[e['id']] / total, 5),
        'r': round((6 + math.sqrt(gr) * 0.9) if area else (2.8 + math.sqrt(grau.get(e['id'], 0)) * 0.85), 2),
        'rot': int(area), 'grupo': e['grupo'], 'set': sorted(e['set']),
        'rotulo': 'Abrir o arquivo da área' if area else '',
    })
# a área "contém" suas normas: liga cada norma ao seu grupo (curva curta, junto ao anel)
for e in ents.values():
    if e['kind'] == 'norma':
        liga(e['id'], e['grupo'])
dados = {
    'R': R, 'T': round(total, 2), 'ents': saida,
    'edges': [{'a': a, 'b': b, 'w': w, 'c': c} for (a, b), (w, c) in pesos.items()],
    'cats': [{'key': k, 'name': n, 'color': c} for k, n, c in CATS],
    'setores': SETORES,
}
html = Path('manutencao/graphify-out/template.html').read_text(encoding='utf-8').replace('__DATA__', json.dumps(dados, ensure_ascii=False))
Path('manutencao/graphify-out/graph.html').write_text(html, encoding='utf-8')
print(len(saida), 'bolinhas,', len(pesos), 'ligações, raio', R)
