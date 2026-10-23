# Instruções para agentes de IA (GitHub Copilot, Claude, ChatGPT etc.)

Este repositório é um **índice das normas contábeis e de auditoria do Brasil** (CFC e CPC) e das
internacionais (IFRS, IAS, ISA), com trechos por setor, glossário e exemplos de lançamentos. O texto
integral das normas não está aqui: cada norma tem um resumo do que trata, as demonstrações que afeta e o link oficial.

## Como responder a um pedido

0. **A pergunta é de um setor específico?** Comece pela pasta do setor. Cada uma traz os trechos das normas
   que importam, com os itens, um checklist e perguntas frequentes no `README.md`:

   | Setor | Pasta |
   |---|---|
   | Indústria (custo de produção, estoques, máquinas, incentivos de ICMS) | [`Industrial/`](../Industrial/README.md) |
   | Varejo (mercadorias, marketplace, fidelidade, cartões, lojas) | [`Varejo/`](../Varejo/README.md) |
   | Serviços (contratos, SaaS, comissões, folha, pequenas empresas) | [`Servicos/`](../Servicos/README.md) |
   | Agronegócio (ativo biológico, colheita, plantas portadoras, crédito rural) | [`Agronegocio/`](../Agronegocio/README.md) |
   | Construção e incorporação (POC, permuta, obras, garantia) | [`Construcao/`](../Construcao/README.md) |
   | Terceiro setor, cooperativas e partidos | [`TerceiroSetor/`](../TerceiroSetor/README.md) |
   | Bancos, seguradoras e fundos de pensão (BCB, SUSEP, CVM) | [`Financeiro/`](../Financeiro/README.md) |

1. **Ache a área.** Abra [`areas/README.md`](../areas/README.md) e escolha a área pela coluna "Use para".
   Cada área tem seu arquivo em `areas/` (ex.: `areas/ativos.md`, `areas/auditoria-independente.md`).
2. **Se o usuário falou só o assunto** ("depreciação", "leasing", "PCLD", "parecer com ressalva"),
   use a tabela **Busca por tema** em `areas/README.md`. A coluna "Também chamado de" tem os sinônimos.
3. **Se a pergunta é sobre uma demonstração** ("o que muda a DRE?", "o que afeta a DFC?"),
   use a tabela **Busca por demonstração afetada** em `areas/README.md`.
4. **Sigla desconhecida?** Veja o [`GLOSSARIO.md`](../GLOSSARIO.md). **Pediram o lançamento contábil?** Veja
   [`lancamentos/`](../lancamentos/README.md) (débito e crédito com a norma de cada um).
   **Reforma tributária (IBS/CBS)?** Veja [`areas/reforma-tributaria.md`](../areas/reforma-tributaria.md).
5. **Leia o resumo da norma** antes de indicar. O título engana: a IFRS 18 / NBC TG 51 se chama
   "Apresentação e Divulgação", mas na prática muda a **DRE**. Normas marcadas com ⚠ estão **revogadas**
   (ex.: NBC TG 26, substituída pela NBC TG 51 a partir de 2027): diga isso ao usuário.
6. **Escolha a série pelo tipo de entidade:**

   | Entidade ou trabalho | Série | Área |
   |---|---|---|
   | Empresa em geral (S.A., Ltda. grande) | NBC TG ≡ CPC ≡ IFRS/IAS | conforme o assunto |
   | Pequena e média empresa | NBC TG 1000, 1001, 1002 | Pequenas e Médias Empresas |
   | Órgão público | NBC TSP (auditoria: NBC TASP) | Setor Público |
   | Instituição financeira autorizada pelo BC | COSIF / Res. CMN 4.966 | [`Financeiro/`](../Financeiro/README.md) |
   | Auditoria das demonstrações | NBC TA ≡ ISA (mesma numeração) | Auditoria Independente |
   | Revisão de ITR | NBC TR | Revisão |
   | Perícia judicial | NBC TP, NBC PP | Perícia Contábil |
   | Ética e exercício profissional | NBC PG, NBC PA | Ética e Exercício Profissional |
   | ESG e clima | NBC TDS ≡ IFRS S1/S2 | Sustentabilidade |
   | Partidos e campanhas eleitorais | NBC TPE 01 | Contabilidade Eleitoral |

7. **Cite as fontes.** Todo arquivo termina com uma seção **Fontes** com o link oficial de cada norma ou lei citada.
   Use esses links na resposta.
8. **Responda** citando o código (ex.: "NBC TG 27 (R4) / CPC 27 / IAS 16"), o item quando houver e o link oficial.
   Os resumos são orientação: para detalhes, confira o texto oficial.

### Exemplos
- "Como depreciar uma máquina?" → [`Industrial/02-maquinas-e-fabrica.md`](../Industrial/02-maquinas-e-fabrica.md) → NBC TG 27 (R4) ≡ CPC 27 ≡ IAS 16.
- "A ociosidade da fábrica entra no custo?" → [`Industrial/01-estoques-e-custo-de-producao.md`](../Industrial/01-estoques-e-custo-de-producao.md) → NBC TG 16, item 13 (não: vai para despesa).
- "No marketplace a receita é o valor total?" → [`Varejo/02-vendas-e-receita.md`](../Varejo/02-vendas-e-receita.md) → NBC TG 47, itens B34–B38.
- "O que muda com a IFRS 18?" → **Apresentação e Divulgação** → NBC TG 51 ≡ CPC 51 (vigente a partir de 2027).
- "IBS e CBS em 2026?" → [`areas/reforma-tributaria.md`](../areas/reforma-tributaria.md) → OT CFC 01/2026, itens 25–29.
- "Prefeitura, como registrar uma escola?" → **Setor Público** → NBC TSP 37.
- "Quando o auditor emite opinião com ressalva?" → **Auditoria Independente** → NBC TA 705.

## Arquivos

| Arquivo | Uso |
|---|---|
| [`areas/README.md`](../areas/README.md) | **Comece aqui.** Áreas, setores, busca por tema (com sinônimos) e por demonstração |
| `areas/<area>.md` | Normas de uma área: resumo, o que afeta, CPC/IFRS equivalente e link |
| Pastas por setor (`Industrial/`, `Varejo/`…) | Trechos das normas por setor, com itens conferidos no texto oficial |
| [`GLOSSARIO.md`](../GLOSSARIO.md) | Siglas e termos (CPV, CIF, VRL, MEP, ORA, PCLD, UGC, MPM, IBS/CBS…) |
| [`lancamentos/`](../lancamentos/README.md) | Exemplos de lançamentos contábeis por tema |
| [`normas.json`](../normas.json) | Dados em JSON: `codigo`, `titulo`, `serie`, `situacao`, `areas`, `temas`, `resumo`, `afeta`, `cpc`, `url_cpc`, `internacional`, `url` e `setores` (trechos por setor: setor, tópico, itens, ponto) |
| [`README.md`](../README.md) | Índice por série (NBC TG, ITG, NBC TA, NBC TSP…) |
| [`verificacao/`](../verificacao/) | Relatórios automáticos: links, conteúdo contra o texto oficial, normas novas no CFC, teste de busca |
| `graphify-out/graph.json` | Grafo: norma ↔ tema ↔ área ↔ setor ↔ demonstração ↔ CPC/IFRS (`graphify query "imobilizado"`) |
| `graphify-out/graph.html` | Mapa interativo para pessoas |

## Atualizar (para quem mantém o repositório)

| O que mudar | Onde |
|---|---|
| Normas, resumos, situação, temas, áreas, setores, fontes externas | planilhas em `dados/` (ver [`dados/README.md`](../dados/README.md)) |
| Páginas escritas à mão em `areas/` | `scripts/conteudo/*.md` |
| Glossário e lançamentos | `GLOSSARIO.md`, `lancamentos/` (edição direta) |
| Instruções para IA | só este `AGENTS.md` (as cópias `CLAUDE.md` e `.github/copilot-instructions.md` são geradas) |

Depois de editar, rode da raiz:

```bash
python graphify-out/rebuild_graph.py
```

Verificações (também rodam no GitHub Actions toda segunda):

```bash
python scripts/verificar_links.py --baixar
python scripts/verificar_itens.py
python scripts/monitorar_cfc.py
python scripts/testar_busca.py
python scripts/verificar_links_internos.py
```

> Os resumos foram escritos a partir do conteúdo das normas e conferidos automaticamente contra os PDFs oficiais
> (`verificacao/CONTEUDO.md`), mas não substituem o texto oficial. Confira sempre o link antes de citar.
