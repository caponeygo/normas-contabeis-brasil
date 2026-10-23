# Graph Report - normas-contabeis-brasil  (2026-10-23)

## Corpus Check
- 105 files · ~122,850 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: .csv 11, (none) 2)

## Summary
- 501 nodes · 1343 edges · 21 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Apresentação e Divulgação / Setor Público
- Ativos
- Setores Específicos
- Instrumentos Financeiros / Normas Internacionais
- Fundamentos / Pequenas e Médias Empresas
- Passivos
- Participações Societárias
- Asseguração / Sustentabilidade
- Ética e Exercício Profissional / Perícia Contábil
- Revisão
- Auditoria Independente
- Moeda e Câmbio
- Tributos
- Riscos, materialidade e planejamento
- Evidência de auditoria
- Receitas
- Serviços Correlatos
- ISA 315
- Auditoria Interna
- Mensuração
- Contabilidade Eleitoral

## God Nodes (most connected - your core abstractions)
1. `Demonstração: BP (Balanço patrimonial)` - 76 edges
2. `Área: Normas Internacionais` - 60 edges
3. `Demonstração: NE (Notas explicativas)` - 55 edges
4. `Área: Apresentação e Divulgação` - 53 edges
5. `Demonstrações contábeis e divulgação (balanço, DRE, DFC, DVA, DMPL, notas explicativas, IAS 1, IFRS 18)` - 51 edges
6. `Demonstração: DRE (Demonstração do resultado)` - 46 edges
7. `Área: Auditoria Independente` - 44 edges
8. `Área: Setor Público` - 41 edges
9. `Área: Ativos` - 33 edges
10. `Área: Setores Específicos` - 33 edges

## Surprising Connections (you probably didn't know these)
- `IAS 32` --pertence_a_area--> `Área: Apresentação e Divulgação`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 0 → community 3_
- `IFRS S1 – Requisitos Gerais de Divulgação de Sustentabilidade` --pertence_a_area--> `Área: Apresentação e Divulgação`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 0 → community 7_
- `CTO 03 – Relatórios sobre Serviços de Depósito Centralizado, Custódia, Escrituração e Emissão de Certificados` --pertence_a_area--> `Área: Asseguração`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 7 → community 4_
- `NBC TO 3402 – Relatórios de Asseguração sobre Controles em Organização Prestadora de Serviços` --pertence_a_area--> `Área: Asseguração`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 7 → community 18_
- `IFRS 5` --pertence_a_area--> `Área: Ativos`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 1 → community 0_

## Communities (21 total, 0 thin omitted)

### Community 0 - "Apresentação e Divulgação / Setor Público"
Cohesion: 0.07
Nodes (70): Área: Apresentação e Divulgação, Área: Setor Público, Demonstração: DFC (Fluxos de caixa), Demonstração: DVA (Valor adicionado), Demonstração: NE (Notas explicativas), CPC 03 (R2), CPC 05 (R1), CPC 09 (R1) (+62 more)

### Community 1 - "Ativos"
Cohesion: 0.08
Nodes (51): Área: Ativos, Demonstração: DVP (Variações patrimoniais (setor público)), CPC 01 (R1), CPC 04 (R1), CPC 06 (R2), CPC 16 (R1), CPC 27, CPC 28 (+43 more)

### Community 2 - "Setores Específicos"
Cohesion: 0.09
Nodes (44): Área: Setores Específicos, Demonstração: DRE (Demonstração do resultado), CPC Liquidação, CTG 01 – Entidades de Incorporação Imobiliária, CTG 04 – Aplicação da ITG 02 – Contrato de Construção do Setor Imobiliário, CTG 05 – Contratos de Concessão, CTG 08 – Reconhecimento de Determinados Ativos e Passivos – Distribuidoras de Energia Elétrica, ICPC 01 (R1) (+36 more)

### Community 3 - "Instrumentos Financeiros / Normas Internacionais"
Cohesion: 0.12
Nodes (39): Área: Instrumentos Financeiros, Área: Normas Internacionais, Área: Patrimônio Líquido, Demonstração: DMPL (Mutações do patrimônio líquido), CPC 10 (R1), CPC 39, CPC 40 (R1), CPC 41 (+31 more)

### Community 4 - "Fundamentos / Pequenas e Médias Empresas"
Cohesion: 0.12
Nodes (29): Área: Fundamentos, Área: Pequenas e Médias Empresas, CPC 00 (R2), CPC 37 (R1), CPC 43 (R1), CPC PME, CTG 1000 – Adoção Plena da NBC TG 1000, CTG 2000 – Ajustes das Novas Práticas Contábeis da Lei 11.638/07 e MP 449/08 (+21 more)

### Community 5 - "Passivos"
Cohesion: 0.13
Nodes (29): Área: Passivos, CPC 20 (R1), CPC 25, CPC 33 (R1), CPC 49, IAS 19, IAS 23, IAS 26 (+21 more)

### Community 6 - "Participações Societárias"
Cohesion: 0.17
Nodes (27): Área: Participações Societárias, Demonstração: BP (Balanço patrimonial), CPC 15 (R1), CPC 18 (R2), CPC 19 (R2), CPC 35 (R2), CPC 36 (R3), CPC 44 (+19 more)

### Community 7 - "Asseguração / Sustentabilidade"
Cohesion: 0.12
Nodes (26): Área: Asseguração, Área: Sustentabilidade, CBPS 01, CBPS 02, CTG 09 – Correlação à Estrutura Conceitual Básica do Relato Integrado, CTG 10 – Créditos de Carbono (tCO2e), Permissões de Emissão (allowances) e CBIO, CTO 01 – Relatório de Asseguração sobre Sustentabilidade e Responsabilidade Social, CTO 02 – Asseguração Razoável sobre Informações Financeiras Pro Forma (Instrução CVM 565) (+18 more)

### Community 8 - "Ética e Exercício Profissional / Perícia Contábil"
Cohesion: 0.16
Nodes (22): Área: Ética e Exercício Profissional, Área: Perícia Contábil, ISA 220, ITP 01 – Apuração de Haveres, NBC PA 01 – Gestão de Qualidade para Firmas de Auditores Independentes, NBC PA 02 – Revisão de Qualidade do Trabalho, NBC PA 11 – Revisão Externa de Qualidade pelos Pares, NBC PA 13 (R4) – Exame de Qualificação Técnica (+14 more)

### Community 9 - "Revisão"
Cohesion: 0.11
Nodes (21): Área: Revisão, CTR 01 (R1) – Relatório de Revisão sobre as Informações Trimestrais (ITR), CTR 02 – Relatório de Revisão das ITR e IFT de Instituições Autorizadas pelo Banco Central, CTR 03 – Relatório de Revisão sobre ITR de Entidade de Incorporação Imobiliária, CTR 04 – Relatório de Revisão sobre ITR de Entidade de Incorporação Imobiliária, ISA 700, ISA 701, ISA 705 (+13 more)

### Community 10 - "Auditoria Independente"
Cohesion: 0.13
Nodes (16): Área: Auditoria Independente, ISA 200, ISA 240, ISA 550, ISA 560, ISA 710, ISA 800, ISA 805 (+8 more)

### Community 11 - "Moeda e Câmbio"
Cohesion: 0.27
Nodes (16): Área: Moeda e Câmbio, Demonstração: DRA (Resultado abrangente / ORA), CPC 02 (R2), CPC 42, IAS 21, IAS 29, ICPC 21, ICPC 23 (+8 more)

### Community 12 - "Tributos"
Cohesion: 0.24
Nodes (16): Área: Tributos, CPC 32, IAS 12, ICPC 19, ICPC 22, IFRIC 21 – Tributos (Levies), IFRIC 23 – Incerteza sobre Tratamento de Tributos sobre o Lucro, ITG 19 – Tributos (+8 more)

### Community 13 - "Riscos, materialidade e planejamento"
Cohesion: 0.13
Nodes (15): ISA 210, ISA 250, ISA 265, ISA 300, ISA 320, ISA 330, ISA 450, NBC TA 210 (R1) – Concordância com os Termos do Trabalho de Auditoria (+7 more)

### Community 14 - "Evidência de auditoria"
Cohesion: 0.13
Nodes (15): ISA 230, ISA 500, ISA 505, ISA 510, ISA 530, ISA 570, ISA 580, NBC TA 230 (R1) – Documentação de Auditoria (+7 more)

### Community 15 - "Receitas"
Cohesion: 0.27
Nodes (13): Área: Receitas, CPC 07 (R1), CPC 47, IAS 20, IFRS 15, NBC TG 07 (R2) – Subvenção e Assistência Governamentais, NBC TG 47 – Receita de Contrato com Cliente, Setor: Serviços (receita de serviços e contratos, SaaS e licenças, comissões de venda, projetos, pessoal (férias, 13º, PLR), stock options, software, escritórios alugados, ISS, pequenas empresas de serviço) (+5 more)

### Community 16 - "Serviços Correlatos"
Cohesion: 0.29
Nodes (13): Área: Serviços Correlatos, CPC 50, CTSC 02 – Procedimentos Previamente Acordados – Despacho ANEEL 514/12, CTSC 03 – Procedimentos Previamente Acordados – Termo de Verificação para Substituição da ECD, CTSC 04 – Procedimentos Previamente Acordados – Questionário de Riscos Susep, CTSC 05 – Procedimentos Previamente Acordados – Art. 242 da Circular Susep 517, CTSC 06 – Procedimentos Previamente Acordados – Circular Susep 574, IFRS 17 (+5 more)

### Community 17 - "ISA 315"
Cohesion: 0.18
Nodes (13): ISA 315, ISA 501, ISA 520, ISA 540, ISA 620, NBC TA 315 (R2) – Identificação e Avaliação dos Riscos de Distorção Relevante, NBC TA 501 – Evidência de Auditoria – Considerações Específicas para Itens Selecionados, NBC TA 520 – Procedimentos Analíticos (+5 more)

### Community 18 - "Auditoria Interna"
Cohesion: 0.17
Nodes (12): Área: Auditoria Interna, ISA 260, ISA 402, ISA 600, ISA 610, NBC TA 260 (R2) – Comunicação com os Responsáveis pela Governança, NBC TA 402 – Considerações de Auditoria para Entidade que Utiliza Organização Prestadora de Serviços, NBC TA 600 (R2) – Auditorias de Demonstrações Contábeis de Grupos, Incluindo o Trabalho dos Auditores dos Componentes (+4 more)

### Community 19 - "Mensuração"
Cohesion: 0.39
Nodes (9): Área: Mensuração, CPC 12 (R1), CPC 46, IFRS 13, NBC TG 12 (R1) – Ajuste a Valor Presente, NBC TG 46 (R2) – Mensuração do Valor Justo, NBC TSP 38 – Mensuração, Ajuste a valor presente (AVP, desconto) (+1 more)

### Community 20 - "Contabilidade Eleitoral"
Cohesion: 0.70
Nodes (5): Área: Contabilidade Eleitoral, NBC TPE 01 – A Contabilidade Aplicada a Partidos e Eleições, OT CFC 02/2026 – Obrigatoriedade da NBC TPE 01 nos Processos Eleitorais a partir de 2026, Contabilidade eleitoral (partidos políticos, campanhas, candidatos, prestação de contas eleitoral, TSE), Terceiro Setor: Partidos políticos e eleições

## Knowledge Gaps
- **66 isolated node(s):** `Área: Auditoria Interna`, `CPC 00 (R2)`, `CPC 09 (R1)`, `Demonstração: DVA (Valor adicionado)`, `CPC 12 (R1)` (+61 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 66 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Área: Auditoria Independente` connect `Auditoria Independente` to `Fundamentos / Pequenas e Médias Empresas`, `Asseguração / Sustentabilidade`, `Ética e Exercício Profissional / Perícia Contábil`, `Revisão`, `Riscos, materialidade e planejamento`, `Evidência de auditoria`, `ISA 315`, `Auditoria Interna`?**
  _High betweenness centrality (0.227) - this node is a cross-community bridge._
- **Why does `Demonstrações contábeis e divulgação (balanço, DRE, DFC, DVA, DMPL, notas explicativas, IAS 1, IFRS 18)` connect `Apresentação e Divulgação / Setor Público` to `Instrumentos Financeiros / Normas Internacionais`, `Asseguração / Sustentabilidade`, `Revisão`, `Auditoria Independente`, `ISA 315`?**
  _High betweenness centrality (0.195) - this node is a cross-community bridge._
- **Why does `Área: Normas Internacionais` connect `Instrumentos Financeiros / Normas Internacionais` to `Apresentação e Divulgação / Setor Público`, `Ativos`, `Setores Específicos`, `Fundamentos / Pequenas e Médias Empresas`, `Passivos`, `Participações Societárias`, `Asseguração / Sustentabilidade`, `Moeda e Câmbio`, `Tributos`, `Receitas`, `Serviços Correlatos`, `Mensuração`?**
  _High betweenness centrality (0.191) - this node is a cross-community bridge._
- **What connects `Área: Auditoria Interna`, `CPC 00 (R2)`, `CPC 09 (R1)` to the rest of the system?**
  _66 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Apresentação e Divulgação / Setor Público` be split into smaller, more focused modules?**
  _Cohesion score 0.07204968944099378 - nodes in this community are weakly interconnected._
- **Should `Ativos` be split into smaller, more focused modules?**
  _Cohesion score 0.0815686274509804 - nodes in this community are weakly interconnected._
- **Should `Setores Específicos` be split into smaller, more focused modules?**
  _Cohesion score 0.0919661733615222 - nodes in this community are weakly interconnected._