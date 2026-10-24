# Lê as planilhas de dados/ (CSV separado por ";", UTF-8 com BOM: abrem direto no Excel).
import csv
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "dados"


def ler(nome):
    with open(PASTA / nome, encoding="utf-8-sig", newline="") as f:
        return [{k: (v or "").strip() for k, v in linha.items()} for linha in csv.DictReader(f, delimiter=";")]
