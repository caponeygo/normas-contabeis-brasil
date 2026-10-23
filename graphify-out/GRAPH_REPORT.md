# Graph Report - normas-contabeis-brasil  (2026-10-23)

## Corpus Check
- Corpus is ~27,328 words - fits in a single context window. You may not need a graph.

## Summary
- 423 nodes · 884 edges · 19 communities (18 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Demonstrações, Instrumentos Financeiros e Setor Público
- Sustentabilidade, Asseguração, PMEs e Setores
- Ativos e Normas Internacionais
- Participações Societárias
- Revisão e Imobiliário
- Fundamentos e Estrutura Conceitual
- Passivos e Provisões
- Ética, Profissão e Perícia
- Auditoria: Evidência
- Auditoria: Riscos e Planejamento
- Auditoria Independente: Relatório
- Auditoria Interna e Uso de Terceiros
- Patrimônio Líquido
- Moeda e Câmbio
- Serviços Correlatos
- Receitas
- Mensuração e Valor Justo
- Tributos
- Procedimentos Analíticos

## God Nodes (most connected - your core abstractions)
1. `Demonstrações contábeis e divulgação (balanço, DRE, DFC, DVA, DMPL, notas explicativas, IAS 1, IFRS 18)` - 50 edges
2. `Área: Auditoria Independente` - 48 edges
3. `Área: Apresentação e Divulgação` - 45 edges
4. `Área: Normas Internacionais` - 45 edges
5. `Área: Setor Público` - 40 edges
6. `Área: Ativos` - 33 edges
7. `Área: Setores Específicos` - 31 edges
8. `Consolidação e participações (MEP, controladas, coligadas, joint venture, fusão e aquisição, IFRS 3, IFRS 10)` - 22 edges
9. `Área: Participações Societárias` - 21 edges
10. `Relatório do auditor (parecer, opinião modificada, PAA, ressalva)` - 19 edges

## Surprising Connections (you probably didn't know these)
- `IFRS 12` --pertence_a_area--> `Área: Apresentação e Divulgação`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 0 → community 3_
- `IFRS S2 – Divulgações Relacionadas ao Clima` --pertence_a_area--> `Área: Apresentação e Divulgação`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 0 → community 1_
- `CTO 03 – Relatórios sobre Serviços de Depósito Centralizado, Custódia, Escrituração e Emissão de Certificados` --pertence_a_area--> `Área: Asseguração`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 1 → community 5_
- `NBC TO 3402 – Relatórios de Asseguração sobre Controles em Organização Prestadora de Serviços` --pertence_a_area--> `Área: Asseguração`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 1 → community 11_
- `ITG 10 – Aplicação Inicial ao Ativo Imobilizado e à Propriedade para Investimento` --pertence_a_area--> `Área: Ativos`  [EXTRACTED]
  normas.json → normas.json  _Bridges community 2 → community 5_

## Communities (19 total, 1 thin omitted)

### Community 0 - "Demonstrações, Instrumentos Financeiros e Setor Público"
Cohesion: 0.07
Nodes (66): Área: Apresentação e Divulgação, Área: Instrumentos Financeiros, Área: Setor Público, CBPS 01, CPC 03 (R2), CPC 05 (R1), CPC 09 (R1), CPC 21 (R1) (+58 more)

### Community 1 - "Sustentabilidade, Asseguração, PMEs e Setores"
Cohesion: 0.06
Nodes (53): Área: Asseguração, Área: Pequenas e Médias Empresas, Área: Setores Específicos, Área: Sustentabilidade, CBPS 02, CPC PME, CTG 05 – Contratos de Concessão, CTG 08 – Reconhecimento de Determinados Ativos e Passivos – Distribuidoras de Energia Elétrica (+45 more)

### Community 2 - "Ativos e Normas Internacionais"
Cohesion: 0.10
Nodes (43): Área: Ativos, Área: Normas Internacionais, CPC 01 (R1), CPC 04 (R1), CPC 06 (R2), CPC 16 (R1), CPC 27, CPC 28 (+35 more)

### Community 3 - "Participações Societárias"
Cohesion: 0.15
Nodes (29): Área: Participações Societárias, CPC 15 (R1), CPC 18 (R2), CPC 19 (R2), CPC 35 (R2), CPC 36 (R3), CPC 44, CPC 45 (+21 more)

### Community 4 - "Revisão e Imobiliário"
Cohesion: 0.09
Nodes (25): Área: Revisão, CTG 01 – Entidades de Incorporação Imobiliária, CTG 04 – Aplicação da ITG 02 – Contrato de Construção do Setor Imobiliário, CTR 01 – Relatório de Revisão das Informações Trimestrais (ITR), CTR 02 – Relatório de Revisão das ITR e IFT de Instituições Autorizadas pelo Banco Central, CTR 03 – Relatório de Revisão sobre ITR de Entidade de Incorporação Imobiliária, CTR 04 – Relatório de Revisão sobre ITR de Entidade de Incorporação Imobiliária, ISA 700 (+17 more)

### Community 5 - "Fundamentos e Estrutura Conceitual"
Cohesion: 0.13
Nodes (24): Área: Fundamentos, CPC 00 (R2), CPC 37 (R1), CPC 43 (R1), CTG 09 – Correlação à Estrutura Conceitual Básica do Relato Integrado, CTG 1000 – Adoção Plena da NBC TG 1000, CTG 2000 – Ajustes das Novas Práticas Contábeis da Lei 11.638/07 e MP 449/08, CTG 2001 (R3) – Formalidades da Escrituração Contábil em Forma Digital para o SPED (+16 more)

### Community 6 - "Passivos e Provisões"
Cohesion: 0.17
Nodes (23): Área: Passivos, CPC 20 (R1), CPC 25, CPC 33 (R1), CPC 49, CTSP 01 – Provisões, Passivos Contingentes e Ativos Contingentes, IAS 19, IAS 23 (+15 more)

### Community 7 - "Ética, Profissão e Perícia"
Cohesion: 0.16
Nodes (22): Área: Ética e Exercício Profissional, Área: Perícia Contábil, ISA 220, ITP 01 – Apuração de Haveres, NBC PA 01 – Gestão de Qualidade para Firmas de Auditores Independentes, NBC PA 02 – Revisão de Qualidade do Trabalho, NBC PA 11 – Revisão Externa de Qualidade pelos Pares, NBC PA 13 (R4) – Exame de Qualificação Técnica (+14 more)

### Community 8 - "Auditoria: Evidência"
Cohesion: 0.11
Nodes (19): ISA 230, ISA 500, ISA 501, ISA 505, ISA 510, ISA 530, ISA 540, ISA 570 (+11 more)

### Community 9 - "Auditoria: Riscos e Planejamento"
Cohesion: 0.12
Nodes (17): ISA 210, ISA 250, ISA 265, ISA 300, ISA 315, ISA 320, ISA 330, ISA 450 (+9 more)

### Community 10 - "Auditoria Independente: Relatório"
Cohesion: 0.13
Nodes (16): Área: Auditoria Independente, ISA 200, ISA 240, ISA 550, ISA 560, ISA 710, ISA 800, ISA 805 (+8 more)

### Community 11 - "Auditoria Interna e Uso de Terceiros"
Cohesion: 0.14
Nodes (14): Área: Auditoria Interna, ISA 260, ISA 402, ISA 600, ISA 610, ISA 620, NBC TA 260 (R2) – Comunicação com os Responsáveis pela Governança, NBC TA 402 – Considerações de Auditoria para Entidade que Utiliza Organização Prestadora de Serviços (+6 more)

### Community 12 - "Patrimônio Líquido"
Cohesion: 0.26
Nodes (14): Área: Patrimônio Líquido, CPC 10 (R1), CPC 41, IAS 33, ICPC 07, ICPC 08 (R1), ICPC 16, IFRS 2 (+6 more)

### Community 13 - "Moeda e Câmbio"
Cohesion: 0.29
Nodes (13): Área: Moeda e Câmbio, CPC 02 (R2), CPC 42, IAS 21, IAS 29, ICPC 21, ICPC 23, ITG 21 – Transação em Moeda Estrangeira e Adiantamento (+5 more)

### Community 14 - "Serviços Correlatos"
Cohesion: 0.29
Nodes (13): Área: Serviços Correlatos, CPC 50, CTSC 02 – Procedimentos Previamente Acordados – Despacho ANEEL 514/12, CTSC 03 – Procedimentos Previamente Acordados – Termo de Verificação para Substituição da ECD, CTSC 04 – Procedimentos Previamente Acordados – Questionário de Riscos Susep, CTSC 05 – Procedimentos Previamente Acordados – Art. 242 da Circular Susep 517, CTSC 06 – Procedimentos Previamente Acordados – Circular Susep 574, IFRS 17 (+5 more)

### Community 15 - "Receitas"
Cohesion: 0.36
Nodes (11): Área: Receitas, CPC 07 (R1), CPC 47, IAS 20, IFRS 15, NBC TG 07 (R2) – Subvenção e Assistência Governamentais, NBC TG 47 – Receita de Contrato com Cliente, NBC TSP 01 – Receita de Transação sem Contraprestação (+3 more)

### Community 16 - "Mensuração e Valor Justo"
Cohesion: 0.36
Nodes (10): Área: Mensuração, CPC 12 (R1), CPC 46, IFRS 13, NBC TG 12 (R1) – Ajuste a Valor Presente, NBC TG 46 (R2) – Mensuração do Valor Justo, NBC TSP 31 (R1) – Instrumentos Financeiros: Reconhecimento e Mensuração, NBC TSP 38 – Mensuração (+2 more)

### Community 17 - "Tributos"
Cohesion: 0.39
Nodes (9): Área: Tributos, CPC 32, IAS 12, ICPC 19, ICPC 22, ITG 19 – Tributos, ITG 22 – Incerteza sobre Tratamento de Tributos sobre o Lucro, NBC TG 32 (R4) – Tributos sobre o Lucro (+1 more)

## Knowledge Gaps
- **74 isolated node(s):** `Área: Auditoria Interna`, `CPC 00 (R2)`, `CPC 09 (R1)`, `CPC 12 (R1)`, `CPC 43 (R1)` (+69 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 74 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Área: Normas Internacionais` connect `Ativos e Normas Internacionais` to `Demonstrações, Instrumentos Financeiros e Setor Público`, `Sustentabilidade, Asseguração, PMEs e Setores`, `Participações Societárias`, `Fundamentos e Estrutura Conceitual`, `Passivos e Provisões`, `Patrimônio Líquido`, `Moeda e Câmbio`, `Serviços Correlatos`, `Receitas`, `Mensuração e Valor Justo`, `Tributos`?**
  _High betweenness centrality (0.365) - this node is a cross-community bridge._
- **Why does `Área: Auditoria Independente` connect `Auditoria Independente: Relatório` to `Demonstrações, Instrumentos Financeiros e Setor Público`, `Sustentabilidade, Asseguração, PMEs e Setores`, `Revisão e Imobiliário`, `Fundamentos e Estrutura Conceitual`, `Passivos e Provisões`, `Ética, Profissão e Perícia`, `Auditoria: Evidência`, `Auditoria: Riscos e Planejamento`, `Auditoria Interna e Uso de Terceiros`, `Procedimentos Analíticos`?**
  _High betweenness centrality (0.324) - this node is a cross-community bridge._
- **Why does `Demonstrações contábeis e divulgação (balanço, DRE, DFC, DVA, DMPL, notas explicativas, IAS 1, IFRS 18)` connect `Demonstrações, Instrumentos Financeiros e Setor Público` to `Sustentabilidade, Asseguração, PMEs e Setores`, `Participações Societárias`, `Revisão e Imobiliário`, `Auditoria: Evidência`, `Auditoria Independente: Relatório`?**
  _High betweenness centrality (0.168) - this node is a cross-community bridge._
- **What connects `Área: Auditoria Interna`, `CPC 00 (R2)`, `CPC 09 (R1)` to the rest of the system?**
  _74 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Demonstrações, Instrumentos Financeiros e Setor Público` be split into smaller, more focused modules?**
  _Cohesion score 0.07179487179487179 - nodes in this community are weakly interconnected._
- **Should `Sustentabilidade, Asseguração, PMEs e Setores` be split into smaller, more focused modules?**
  _Cohesion score 0.06313497822931785 - nodes in this community are weakly interconnected._
- **Should `Ativos e Normas Internacionais` be split into smaller, more focused modules?**
  _Cohesion score 0.09856035437430787 - nodes in this community are weakly interconnected._