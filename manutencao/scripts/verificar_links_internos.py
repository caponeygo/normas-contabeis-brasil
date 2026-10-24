# Confere os links internos dos .md (arquivos e âncoras #secao) e se cada norma citada nos setores tem link.
# Saída no terminal; sai com código 1 se houver link interno quebrado.
import re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
IGNORAR = {".cache", ".git", "node_modules", "conteudo"}  # scripts/conteudo: originais copiados para areas/


def ancora(titulo):  # regra do GitHub para âncoras de títulos
    t = titulo.strip().lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.UNICODE)
    return t.replace(" ", "-")


def ancoras(arq):
    return {ancora(m.group(1)) for m in re.finditer(r"(?m)^#{1,6}\s+(.+)$", arq.read_text(encoding="utf-8"))}


erros = []
mds = [p for p in ROOT.rglob("*.md") if not IGNORAR & set(p.relative_to(ROOT).parts)]
for md in mds:
    txt = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
    for alvo in re.findall(r"(?<!\\)\]\(([^)\s]+)\)", txt):     # "\](" é texto escapado, não link
        if re.match(r"(https?:|mailto:)", alvo):
            continue
        caminho, _, frag = alvo.partition("#")
        destino = (md.parent / caminho).resolve() if caminho else md
        if not destino.exists():
            erros.append(f"{md.relative_to(ROOT)} → {alvo} (arquivo não existe)")
        elif frag and destino.suffix == ".md" and unicodedata.normalize("NFC", frag.lower()) not in ancoras(destino):
            erros.append(f"{md.relative_to(ROOT)} → {alvo} (âncora não existe)")
print(f"{len(mds)} arquivos .md conferidos; {len(erros)} link(s) interno(s) quebrado(s)")
for e in erros:
    print("  ", e)
sys.exit(1 if erros else 0)
