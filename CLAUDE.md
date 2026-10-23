# Instruções para agentes de IA

Este repositório é um índice das normas contábeis e de auditoria do Brasil (CFC/CPC) e das
internacionais (IFRS/IAS/ISA). O texto das normas não está aqui: cada norma tem um link oficial.

## Como achar a norma certa para um pedido

1. **Identifique o tema** do pedido (ex.: "como depreciar uma máquina?" → tema *Imobilizado*).
2. **Procure o tema** em `normas.json` → `temas[]` (campos `tema`, `area`, `sinonimos`).
   Os sinônimos cobrem termos do dia a dia: ativo fixo, leasing, impairment, PCLD, ESG etc.
3. **Liste as normas** em `normas.json` → `normas[]` cujo campo `temas` contém o tema.
   Cada norma tem `codigo`, `titulo`, `serie`, `areas`, `cpc`, `internacional` e `url`.
4. **Escolha pela entidade:**
   - empresa em geral → NBC TG / CPC (correlação IFRS/IAS no campo `internacional`)
   - pequena e média empresa → NBC TG 1000 (área *Pequenas e Médias Empresas*)
   - órgão público → NBC TSP (área *Setor Público*)
   - auditoria → NBC TA (mesma numeração das ISA)
5. **Abra o `url`** para ler o texto vigente antes de responder, e cite o código da norma.

Exemplo: "imobilizado" → NBC TG 27 (R4) ≡ CPC 27 ≡ IAS 16; setor público → NBC TSP 37;
adoção inicial → ITG 10; perda por impairment → NBC TG 01 (R4).

## Arquivos

| Arquivo | Uso |
|---|---|
| `normas.json` | Dados estruturados (fonte para busca) |
| `AREAS.md` | Normas agrupadas por área + tabela de busca por tema |
| `README.md` | Índice por série |
| `graphify-out/graph.json` | Grafo de conhecimento (norma ↔ tema ↔ área ↔ CPC/IFRS) |
| `graphify-out/graph.html` | Mapa interativo: um círculo com uma bolinha por norma, agrupadas por área e coloridas por série; busca por tema/sinônimo |
| `graphify-out/GRAPH_REPORT.md` | Relatório do grafo (comunidades, nós centrais) |

Com o [graphify](https://github.com/safishamsi/graphify) instalado: `graphify query "imobilizado"`.

## Atualizar

Edite os dados em `scripts/gerar_indice.py` e rode, da raiz do projeto:

```bash
python graphify-out/rebuild_graph.py
```

Ele regenera README.md, AREAS.md e normas.json, refaz `graphify-out/graph.json` e gera o
`graph.html` (layout em `graphify-out/build_html.py`, visual em `graphify-out/template.html`).
Use o Python que tem o graphify instalado (`uv tool install graphifyy`).
