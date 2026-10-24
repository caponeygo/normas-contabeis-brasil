# Regera o índice (README, AREAS.md, normas.json), refaz graph.json e gera o graph.html.
# Rodar da raiz do projeto:  <python do graphify> graphify-out/rebuild_graph.py
import json, subprocess, sys
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster
from graphify.export import to_json

if __name__ == '__main__':
    subprocess.run([sys.executable, 'manutencao/scripts/gerar_indice.py'], check=True)
    subprocess.run([sys.executable, 'manutencao/scripts/adicionar_fontes.py'], check=True)
    ext = json.loads(Path('manutencao/graphify-out/.graphify_extract.json').read_text(encoding='utf-8'))
    G = build_from_json(ext, root='.', directed=False)
    assert G.number_of_nodes() > 0, 'extração vazia'
    com = cluster(G)
    # nome de cada grupo = área (ou tema) mais presente nele
    labels = {}
    for cid, nos in com.items():
        areas = [G.nodes[n]['label'].replace('Área: ', '') for n in nos if n.startswith('area_')]
        temas = [G.nodes[n]['label'].split(' (')[0] for n in nos if n.startswith('tema_')]
        labels[cid] = ' / '.join((areas or temas or [G.nodes[nos[0]]['label']])[:2])
    # --force: o grafo pode ter mudado de tamanho (normas novas/removidas)
    to_json(G, com, 'manutencao/graphify-out/graph.json', force=True, community_labels=labels)
    from graphify.cluster import score_all
    from graphify.analyze import god_nodes, surprising_connections, suggest_questions
    from graphify.report import generate
    from graphify.detect import detect
    rep = generate(G, com, score_all(G, com), labels, god_nodes(G), surprising_connections(G, com),
                   detect(Path('.')), {'input': 0, 'output': 0}, '.',
                   suggested_questions=suggest_questions(G, com, labels))
    Path('manutencao/graphify-out/GRAPH_REPORT.md').write_text(rep, encoding='utf-8')
    print(f'{G.number_of_nodes()} nós, {G.number_of_edges()} arestas')
    subprocess.run([sys.executable, 'manutencao/graphify-out/build_html.py'], check=True)
