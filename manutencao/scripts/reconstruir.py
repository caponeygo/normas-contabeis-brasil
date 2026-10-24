# Regera tudo a partir das planilhas: README, areas/, normas/, setores/, normas.json, fichas e o mapa (mapa.html).
# Rodar da raiz do projeto:  python manutencao/scripts/reconstruir.py
import subprocess, sys

if __name__ == "__main__":
    for script in ("manutencao/scripts/gerar_indice.py", "manutencao/scripts/adicionar_fontes.py", "manutencao/mapa/gerar_mapa.py"):
        subprocess.run([sys.executable, script], check=True)
