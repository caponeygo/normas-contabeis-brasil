# Instruções para agentes de IA (GitHub Copilot, Claude, ChatGPT etc.)

Este repositório é um **índice das normas contábeis e de auditoria do Brasil** (CFC e CPC) e das
internacionais (IFRS, IAS, ISA). O texto integral das normas não está aqui: cada norma tem um
resumo do que trata, as demonstrações que afeta e o link oficial.

## Como responder a um pedido

1. **Ache a área.** Abra [`areas/README.md`](areas/README.md) e escolha a área pela coluna "Use para".
   Cada área tem seu arquivo em `areas/` (ex.: `areas/ativos.md`, `areas/auditoria-independente.md`).
2. **Se o usuário falou só o assunto** ("depreciação", "leasing", "PCLD", "parecer com ressalva"),
   use a tabela **Busca por tema** em `areas/README.md`. A coluna "Também chamado de" tem os sinônimos.
3. **Se a pergunta é sobre uma demonstração** ("o que muda a DRE?", "o que afeta a DFC?"),
   use a tabela **Busca por demonstração afetada** em `areas/README.md`.
4. **Leia o resumo da norma** no arquivo da área antes de indicar. O título engana: a IFRS 18 /
   NBC TG 51 se chama "Apresentação e Divulgação", mas na prática muda a **DRE**.
5. **Escolha a série pelo tipo de entidade:**

   | Entidade ou trabalho | Série | Área |
   |---|---|---|
   | Empresa em geral (S.A., Ltda. grande) | NBC TG ≡ CPC ≡ IFRS/IAS | conforme o assunto |
   | Pequena e média empresa | NBC TG 1000, 1001, 1002 | Pequenas e Médias Empresas |
   | Órgão público | NBC TSP | Setor Público |
   | Auditoria das demonstrações | NBC TA ≡ ISA (mesma numeração) | Auditoria Independente |
   | Revisão de ITR | NBC TR | Revisão |
   | Perícia judicial | NBC TP, NBC PP | Perícia Contábil |
   | Ética e exercício profissional | NBC PG, NBC PA | Ética e Exercício Profissional |
   | ESG e clima | NBC TDS ≡ IFRS S1/S2 | Sustentabilidade |

6. **Responda** citando o código (ex.: "NBC TG 27 (R4) / CPC 27 / IAS 16") e o link oficial (`url`).
   Os resumos são orientação: para detalhes, confira o texto oficial.

### Exemplos
- "Como depreciar uma máquina?" → área **Ativos**, tema Imobilizado → NBC TG 27 (R4) ≡ CPC 27 ≡ IAS 16.
- "Aluguel de loja entra no balanço?" → **Ativos**, tema Arrendamentos → NBC TG 06 (R3) ≡ CPC 06 ≡ IFRS 16.
- "O que muda com a IFRS 18?" → **Apresentação e Divulgação**, tema DRE → NBC TG 51 ≡ CPC 51.
- "Prefeitura, como registrar uma escola?" → **Setor Público** → NBC TSP 37.
- "Quando o auditor emite opinião com ressalva?" → **Auditoria Independente** → NBC TA 705.

## Arquivos

| Arquivo | Uso |
|---|---|
| [`areas/README.md`](areas/README.md) | **Comece aqui.** Áreas, busca por tema (com sinônimos) e por demonstração |
| `areas/<area>.md` | Normas de uma área: resumo, o que afeta, CPC/IFRS equivalente e link |
| [`normas.json`](normas.json) | Os mesmos dados em JSON: `codigo`, `titulo`, `serie`, `areas`, `temas`, `resumo`, `afeta`, `cpc`, `internacional`, `url` |
| [`README.md`](README.md) | Índice por série (NBC TG, ITG, NBC TA, NBC TSP…) |
| `graphify-out/graph.json` | Grafo: norma ↔ tema ↔ área ↔ demonstração ↔ CPC/IFRS (`graphify query "imobilizado"`) |
| `graphify-out/graph.html` | Mapa interativo para pessoas |

## Atualizar (para quem mantém o repositório)

Os dados ficam em `scripts/gerar_indice.py` (normas, temas, áreas) e `scripts/resumos.py` (resumos).
Depois de editar, rode da raiz:

```bash
python graphify-out/rebuild_graph.py
```

Isso regenera `areas/`, `README.md`, `normas.json`, as cópias deste arquivo (`CLAUDE.md` e
`.github/copilot-instructions.md`), o grafo e o `graph.html`. Edite só o `AGENTS.md`: as cópias são geradas.

> Os resumos foram escritos a partir do conteúdo conhecido das normas, não copiados do texto oficial.
> Confira sempre o link oficial antes de citar.
