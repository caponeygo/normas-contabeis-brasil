# Regera o índice (README, AREAS.md, normas.json), refaz graph.json e gera o graph.html.
# Rodar da raiz do projeto:  <python do graphify> graphify-out/rebuild_graph.py
import json, subprocess, sys
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster
from graphify.export import to_json

if __name__ == '__main__':
    subprocess.run([sys.executable, 'scripts/gerar_indice.py'], check=True)
    ext = json.loads(Path('graphify-out/.graphify_extract.json').read_text(encoding='utf-8'))
    G = build_from_json(ext, root='.', directed=False)
    assert G.number_of_nodes() > 0, 'extração vazia'
    com = cluster(G)
    # --force: o grafo pode ter mudado de tamanho (normas novas/removidas)
    to_json(G, com, 'graphify-out/graph.json', force=True)
    print(f'{G.number_of_nodes()} nós, {G.number_of_edges()} arestas')
    subprocess.run([sys.executable, 'graphify-out/build_html.py'], check=True)
