# Instruções para agentes de IA (GitHub Copilot, Claude, ChatGPT etc.)

Este repositório é um **índice das normas contábeis e de auditoria do Brasil** (CFC e CPC) e das
internacionais (IFRS, IAS, ISA), com trechos por setor, glossário e exemplos de lançamentos. O texto
integral das normas não está aqui: cada norma tem um resumo do que trata, as demonstrações que afeta e o link oficial.

## Como responder a um pedido

0. **A pergunta é de um setor específico?** Comece pela pasta do setor. Cada uma traz os trechos das normas
   que importam, com os itens, um checklist e perguntas frequentes no `README.md`:

   | Setor | Pasta |
   |---|---|
   | Indústria (custo de produção, estoques, máquinas, incentivos de ICMS) | [`setores/industrial/`](../setores/industrial/README.md) |
   | Varejo (mercadorias, marketplace, fidelidade, cartões, lojas) | [`setores/varejo/`](../setores/varejo/README.md) |
   | Serviços (contratos, SaaS, comissões, folha, pequenas empresas) | [`setores/servicos/`](../setores/servicos/README.md) |
   | Agronegócio (ativo biológico, colheita, plantas portadoras, crédito rural) | [`setores/agronegocio/`](../setores/agronegocio/README.md) |
   | Construção e incorporação (POC, permuta, obras, garantia) | [`setores/construcao/`](../setores/construcao/README.md) |
   | Terceiro setor, cooperativas e partidos | [`setores/terceiro-setor/`](../setores/terceiro-setor/README.md) |
   | Bancos, seguradoras e fundos de pensão (BCB, SUSEP, CVM) | [`setores/financeiro/`](../setores/financeiro/README.md) |

1. **Tem o código da norma?** Procure em [`normas/README.md`](../normas/README.md) (lista A–Z).
   **Ache a área.** Abra [`areas/README.md`](../areas/README.md) e escolha a área pela coluna "Use para".
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
   | Instituição financeira autorizada pelo BC | COSIF / Res. CMN 4.966 | [`setores/financeiro/`](../setores/financeiro/README.md) |
   | Auditoria das demonstrações | NBC TA ≡ ISA (mesma numeração) | Auditoria Independente |
   | Revisão de ITR | NBC TR | Revisão |
   | Auditoria de companhia aberta registrada na SEC (EUA) ou de corretora | PCAOB AS, AT, ET, QC, EI (não são normas brasileiras; as de 15/12/2026 estão em `status` futura) | Padrões PCAOB (EUA) |
   | Perícia judicial | NBC TP, NBC PP | Perícia Contábil |
   | Ética e exercício profissional | NBC PG, NBC PA | Ética e Exercício Profissional |
   | ESG e clima | NBC TDS ≡ IFRS S1/S2 | Sustentabilidade |
   | Partidos e campanhas eleitorais | NBC TPE 01 | Contabilidade Eleitoral |

7. **Cite as fontes.** Todo arquivo termina com uma seção **Fontes** com o link oficial de cada norma ou lei citada.
   Use esses links na resposta.
8. **Responda** citando o código (ex.: "NBC TG 27 (R4) / CPC 27 / IAS 16"), o item quando houver e o link oficial.
   Os resumos são orientação: para detalhes, confira o texto oficial.

### Exemplos
- "Como depreciar uma máquina?" → [`setores/industrial/02-maquinas-e-fabrica.md`](../setores/industrial/02-maquinas-e-fabrica.md) → NBC TG 27 (R4) ≡ CPC 27 ≡ IAS 16.
- "A ociosidade da fábrica entra no custo?" → [`setores/industrial/01-estoques-e-custo-de-producao.md`](../setores/industrial/01-estoques-e-custo-de-producao.md) → NBC TG 16, item 13 (não: vai para despesa).
- "No marketplace a receita é o valor total?" → [`setores/varejo/02-vendas-e-receita.md`](../setores/varejo/02-vendas-e-receita.md) → NBC TG 47, itens B34–B38.
- "O que muda com a IFRS 18?" → **Apresentação e Divulgação** → NBC TG 51 ≡ CPC 51 (vigente a partir de 2027).
- "IBS e CBS em 2026?" → [`areas/reforma-tributaria.md`](../areas/reforma-tributaria.md) → OT CFC 01/2026, itens 25–29.
- "Prefeitura, como registrar uma escola?" → **Setor Público** → NBC TSP 37.
- "Quando o auditor emite opinião com ressalva?" → **Auditoria Independente** → NBC TA 705.

## Regras para não errar (leia antes de responder)

1. **Só afirme o que está aqui.** Não cite número de item, parágrafo, prazo, alíquota ou valor que não apareça nestes arquivos ou no link oficial.
   Se a informação não estiver no repositório, diga isso e indique o link oficial. Não complete de memória.
2. **Vigência primeiro.** Em [`normas.json`](../normas.json) cada norma tem `status` (`vigente`, `revogada` ou `futura`), `substituida_por`, `vigente_a_partir_de`, `observacao_vigencia`,
   `revogada_em` e `substituta_vale_a_partir_de`. Norma revogada: indique a substituta. Se `substituta_vale_a_partir_de` existir
   (ex.: NBC TG 26 → NBC TG 51, a partir de 2027-01-01), a revogada ainda vale para exercícios anteriores a essa data: pergunte o exercício ou explique os dois casos.
   As normas com mudança de vigência marcada estão listadas em [`normas/mudancas-futuras.md`](../normas/mudancas-futuras.md): consulte antes de afirmar que uma norma vale ou deixa de valer.
3. **Olhe a coluna Conferência** nas pastas de setor: ✅ = item achado no texto oficial e assunto confere; ✅👤 = revisado por pessoa;
   ⚠ = não conferido ou a revisar (inclui regras de fora do CFC: BCB, CVM, SUSEP, leis). Em ⚠, diga ao usuário que confirme no link oficial antes de aplicar.
4. **Cada norma tem uma ficha** em `normas/ficha/<codigo>.md` (ex.: `normas/ficha/nbc-tg-27-r4.md`) com status, equivalentes, trechos por setor e link oficial. Prefira a ficha a ler a série inteira.
5. **Fora do escopo:** o repositório indexa normas do CFC/CPC/IASB/IAASB e trechos por setor. Não cobre legislação fiscal detalhada (alíquotas, obrigações acessórias),
   jurisprudência, normas de outros países nem casos concretos de empresa. Nesses casos, diga que não cobre.
6. **Código parecido não é o mesmo:** NBC TA (Brasil) ≠ PCAOB AS (EUA); NBC TG ≠ NBC TA ≠ NBC TSP; CPC ≠ ICPC ≠ OCPC; ITG ≠ CTG ≠ OTG. Confira a série pelo código completo e pela revisão `(Rn)`.
7. **Não dê aconselhamento profissional.** O resumo orienta; a decisão contábil depende do texto oficial e do caso.

## Arquivos

| Arquivo | Uso |
|---|---|
| [`areas/README.md`](../areas/README.md) | **Comece aqui.** Áreas, setores, busca por tema (com sinônimos) e por demonstração |
| `areas/<area>.md` | Normas de uma área: resumo, o que afeta, CPC/IFRS equivalente e link |
| [`normas/`](../normas/README.md) | Todas as normas: lista A–Z de códigos (com área e link oficial) e um arquivo por série |
| [`setores/`](../setores/README.md) (`setores/industrial/`, `setores/varejo/`…) | Trechos das normas por setor, com itens conferidos no texto oficial |
| [`llms.txt`](../llms.txt) | Mapa curto do repositório para assistentes de IA |
| [`normas/ficha/`](../normas/README.md) | Uma ficha por norma: status, equivalentes, trechos por setor e link oficial |
| [`GLOSSARIO.md`](../GLOSSARIO.md) | Siglas e termos (CPV, CIF, VRL, MEP, ORA, PCLD, UGC, MPM, IBS/CBS…) |
| [`lancamentos/`](../lancamentos/README.md) | Exemplos de lançamentos contábeis por tema |
| [`normas.json`](../normas.json) | Dados em JSON: `codigo`, `titulo`, `serie`, `situacao`, `areas`, `temas`, `resumo`, `afeta`, `cpc`, `url_cpc`, `internacional`, `url` e `setores` (trechos por setor: setor, tópico, itens, ponto) |
| [`README.md`](../README.md) | Página inicial: como achar norma, assunto, setor, lançamento ou sigla |
| [`manutencao/verificacao/`](../manutencao/verificacao/) | Relatórios automáticos: links, conteúdo contra o texto oficial, normas novas no CFC, teste de busca |
| `manutencao/graphify-out/graph.json` | Grafo: norma ↔ tema ↔ área ↔ setor ↔ demonstração ↔ CPC/IFRS (`graphify query "imobilizado"`) |
| `manutencao/graphify-out/graph.html` | Mapa interativo para pessoas |

## Atualizar (para quem mantém o repositório)

| O que mudar | Onde |
|---|---|
| Normas, resumos, situação, temas, áreas, setores, fontes externas | planilhas em `manutencao/dados/` (ver [`manutencao/dados/README.md`](../manutencao/dados/README.md)) |
| Páginas escritas à mão em `areas/` | `manutencao/scripts/conteudo/*.md` |
| Glossário e lançamentos | `GLOSSARIO.md`, `lancamentos/` (edição direta) |
| Instruções para IA | só este `AGENTS.md` (as cópias `CLAUDE.md` e `.github/copilot-instructions.md` são geradas) |

Depois de editar, rode da raiz:

```bash
python manutencao/graphify-out/rebuild_graph.py
```

Verificações (também rodam no GitHub Actions toda segunda):

```bash
python manutencao/scripts/verificar_links.py --baixar
python manutencao/scripts/verificar_itens.py
python manutencao/scripts/monitorar_cfc.py
python manutencao/scripts/testar_busca.py
python manutencao/scripts/verificar_links_internos.py
```

> Os resumos foram escritos a partir do conteúdo das normas e conferidos automaticamente contra os PDFs oficiais
> (`manutencao/verificacao/CONTEUDO.md`), mas não substituem o texto oficial. Confira sempre o link antes de citar.
