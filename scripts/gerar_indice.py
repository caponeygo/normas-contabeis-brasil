import sys
B1="https://www2.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo="
B0="https://www1.cfc.org.br/sisweb/sre/detalhes_sre.aspx?Codigo="
tg="""ESTRUTURA CONCEITUAL|Estrutura Conceitual para Relatório Financeiro|CPC 00 (R2)|Framework|2/2019/NBCTGEC&arquivo=NBCTGEC.doc
01 (R4)|Redução ao Valor Recuperável de Ativos|CPC 01 (R1)|IAS 36|2/2017/NBCTG01(R4)&arquivo=NBCTG01(R4).doc
02 (R3)|Efeitos das Mudanças nas Taxas de Câmbio e Conversão de Demonstrações Contábeis|CPC 02 (R2)|IAS 21|2/2017/NBCTG02(R3)&arquivo=NBCTG02(R3).doc
03 (R3)|Demonstração dos Fluxos de Caixa|CPC 03 (R2)|IAS 7|2/2016/NBCTG03(R3)&arquivo=NBCTG03(R3).doc
04 (R4)|Ativo Intangível|CPC 04 (R1)|IAS 38|2/2017/NBCTG04(R4)&arquivo=NBCTG04(R4).doc
05 (R3)|Divulgação sobre Partes Relacionadas|CPC 05 (R1)|IAS 24|1/2014/NBCTG05(R3)
06 (R3)|Arrendamentos|CPC 06 (R2)|IFRS 16|2/2017/NBCTG06(R3)&arquivo=NBCTG06(R3).doc
07 (R2)|Subvenção e Assistência Governamentais|CPC 07 (R1)|IAS 20|2/2017/NBCTG07(R2)&arquivo=NBCTG07(R2).doc
09 (R1)|Demonstração do Valor Adicionado (DVA)|CPC 09 (R1)|—|2/2024/NBCTG09(R1)&arquivo=NBCTG09(R1).doc
10 (R3)|Pagamento Baseado em Ações|CPC 10 (R1)|IFRS 2|2/2017/NBCTG10(R3)&arquivo=NBCTG10(R3).doc
12 (R1)|Ajuste a Valor Presente|CPC 12 (R1)|—|2/2023/NBCTG12(R1)
15 (R4)|Combinação de Negócios|CPC 15 (R1)|IFRS 3|2/2017/NBCTG15(R4)&arquivo=NBCTG15(R4).doc
16 (R2)|Estoques|CPC 16 (R1)|IAS 2|2/2017/NBCTG16(R2)&arquivo=NBCTG16(R2).doc
18 (R4)|Investimento em Coligada e em Empreendimento Controlado em Conjunto|CPC 18 (R2)|IAS 28|1/2024/NBCTG18(R4)&arquivo=NBCTG18(R4).doc
19 (R2)|Negócios em Conjunto|CPC 19 (R2)|IFRS 11|1/2015/NBCTG19(R2)
20 (R2)|Custos de Empréstimos|CPC 20 (R1)|IAS 23|2/2017/NBCTG20(R2)&arquivo=NBCTG20(R2).doc
21 (R4)|Demonstração Intermediária|CPC 21 (R1)|IAS 34|2/2017/NBCTG21(R4)&arquivo=NBCTG21(R4).doc
22 (R2)|Informações por Segmento|CPC 22|IFRS 8|1/2015/NBCTG22(R2)
23 (R2)|Políticas Contábeis, Mudança de Estimativa e Retificação de Erro|CPC 23|IAS 8|2/2017/NBCTG23(R2)&arquivo=NBCTG23(R2).doc
24 (R2)|Evento Subsequente|CPC 24|IAS 10|2/2017/NBCTG24(R2)&arquivo=NBCTG24(R2).doc
25 (R2)|Provisões, Passivos Contingentes e Ativos Contingentes|CPC 25|IAS 37|2/2017/NBCTG25(R2)&arquivo=NBCTG25(R2).doc
26 (R5)|Apresentação das Demonstrações Contábeis|CPC 26 (R1)|IAS 1|2/2017/NBCTG26(R5)&arquivo=NBCTG26(R5)%20_rev19.doc
27 (R4)|Ativo Imobilizado|CPC 27|IAS 16|2/2017/NBCTG27(R4)&arquivo=NBCTG27(R4)_rev18.doc
28 (R4)|Propriedade para Investimento|CPC 28|IAS 40|2/2017/NBCTG28(R4)&arquivo=NBCTG28(R4).doc
29 (R2)|Ativo Biológico e Produto Agrícola|CPC 29|IAS 41|1/2015/NBCTG29(R2)
31 (R4)|Ativo Não Circulante Mantido para Venda e Operação Descontinuada|CPC 31|IFRS 5|2/2017/NBCTG31(R4)&arquivo=NBCTG31(R4).doc
32 (R4)|Tributos sobre o Lucro|CPC 32|IAS 12|2/2017/NBCTG32(R4)&arquivo=NBCTG32(R4).doc
33 (R2)|Benefícios a Empregados|CPC 33 (R1)|IAS 19|1/2015/NBCTG33(R2)
35 (R2)|Demonstrações Separadas|CPC 35 (R2)|IAS 27|1/2014/NBCTG35(R2)
36 (R3)|Demonstrações Consolidadas|CPC 36 (R3)|IFRS 10|1/2015/NBCTG36(R3)
37 (R5)|Adoção Inicial das Normas Internacionais de Contabilidade|CPC 37 (R1)|IFRS 1|2/2017/NBCTG37(R5)&arquivo=NBCTG37(R5).doc
39 (R5)|Instrumentos Financeiros: Apresentação|CPC 39|IAS 32|2/2017/NBCTG39(R5)&arquivo=NBCTG39(R5).doc
40 (R3)|Instrumentos Financeiros: Evidenciação|CPC 40 (R1)|IFRS 7|2/2017/NBCTG40(R3)&arquivo=NBCTG40(R3).doc
41 (R2)|Resultado por Ação|CPC 41|IAS 33|2/2017/NBCTG41(R2)
42|Contabilidade em Economia Hiperinflacionária|CPC 42|IAS 29|2/2018/NBCTG42&arquivo=NBCTG42.doc
43|Adoção Inicial das NBC Ts Convergidas em 2009|CPC 43 (R1)|—|1/2010/001315
44|Demonstrações Combinadas|CPC 44|—|2/2013/NBCTG44
45 (R3)|Divulgação de Participações em Outras Entidades|CPC 45|IFRS 12|2/2017/NBCTG45(R3)&arquivo=NBCTG45(R3).doc
46 (R2)|Mensuração do Valor Justo|CPC 46|IFRS 13|2/2017/NBCTG46(R2)&arquivo=NBCTG46(R2).doc
47|Receita de Contrato com Cliente|CPC 47|IFRS 15|2/2016/NBCTG47&arquivo=NBCTG47.doc
48|Instrumentos Financeiros|CPC 48|IFRS 9|2/2016/NBCTG48&arquivo=NBCTG48.doc
49|Contabilização e Relatório Contábil de Planos de Benefícios de Aposentadoria|CPC 49|IAS 26|2/2018/NBCTG49&arquivo=NBCTG49.doc
50|Contratos de Seguro|CPC 50|IFRS 17|2/2021/NBCTG50&arquivo=NBCTG50.doc
51|Apresentação e Divulgação nas Demonstrações Contábeis|CPC 51|IFRS 18|2/2025/NBCTG51&arquivo=NBCTG51.docx
900|Entidades em Liquidação|CPC Liquidação|—|2/2021/NBCTG900&arquivo=NBCTG900..doc"""
itg="""ITG 01 (R1)|Contratos de Concessão|ICPC 01 (R1)|2/2017/ITG01(R1)&arquivo=ITG01(R1).doc
ITG 07 (R1)|Distribuição de Lucros in Natura|ICPC 07|1/2013/ITG07(R1)
ITG 08|Contabilização da Proposta de Pagamento de Dividendos|ICPC 08 (R1)|1/2012/001398
ITG 09 (R2)|Demonstrações Individuais, Separadas, Consolidadas e Método de Equivalência Patrimonial|ICPC 09 (R3)|2/2024/ITG09(R2)&arquivo=ITG09(R2).doc
ITG 10|Aplicação Inicial ao Ativo Imobilizado e à Propriedade para Investimento|ICPC 10|1/2009/001263
ITG 12|Mudanças em Passivos por Desativação, Restauração e Outros Passivos Similares|ICPC 12|1/2009/001265
ITG 13 (R2)|Direitos a Participações Decorrentes de Fundos de Desativação, Restauração e Reabilitação Ambiental|ICPC 13|2/2017/ITG13(R2)&arquivo=ITG13(R2).doc
ITG 15|Passivos Decorrentes de Participação em Mercado Específico – Resíduos de Equipamentos Eletroeletrônicos|ICPC 15|1/2010/001289
ITG 16 (R2)|Extinção de Passivos Financeiros com Instrumentos Patrimoniais|ICPC 16|2/2017/ITG16(R2)&arquivo=ITG16(R2).doc
ITG 17|Contratos de Concessão: Evidenciação|ICPC 17|1/2011/001375
ITG 18|Custos de Remoção de Estéril de Mina de Superfície – Fase de Produção|ICPC 18|2/2013/ITG18
ITG 19|Tributos|ICPC 19|1/2014/ITG19
ITG 20|Limite de Ativo de Benefício Definido, Requisitos de Custeio Mínimo e sua Interação|ICPC 20|1/2014/ITG20
ITG 21|Transação em Moeda Estrangeira e Adiantamento|ICPC 21|2/2017/ITG21&arquivo=ITG21.doc
ITG 22|Incerteza sobre Tratamento de Tributos sobre o Lucro|ICPC 22|2/2018/ITG22&arquivo=ITG22.doc
ITG 23|Aplicação da Abordagem de Atualização Monetária Prevista na NBC TG 42|ICPC 23|2/2018/ITG23&arquivo=ITG23.doc
CTG 01|Entidades de Incorporação Imobiliária|OCPC 01|1/2009/001154
CTG 04|Aplicação da ITG 02 – Contrato de Construção do Setor Imobiliário|OCPC 04|1/2010/001317
CTG 05|Contratos de Concessão|OCPC 05|1/2010/001318
CTG 06|Apresentação de Informações Financeiras Pro Forma|OCPC 06|2/2013/CTG06
CTG 07 (R1)|Evidenciação na Divulgação dos Relatórios Contábil-Financeiros de Propósito Geral|OCPC 07|2/2023/CTG07R1
CTG 08|Reconhecimento de Determinados Ativos e Passivos – Distribuidoras de Energia Elétrica|OCPC 08|1/2014/CTG08
CTG 09|Correlação à Estrutura Conceitual Básica do Relato Integrado|OCPC 09|2/2020/CTG09&arquivo=CTG09.doc
CTG 10|Créditos de Carbono (tCO2e), Permissões de Emissão (allowances) e CBIO|OCPC 10|2/2024/CTG10&arquivo=CTG10.doc
OTG 2003 (R1)|Orientações sobre a Aplicação da ITG 2003 (R1) – Entidade Desportiva|—|2/2024/OTG2003(R1)&arquivo=OTG2003(R1).doc"""
ta="""Estrutura Conceitual|Estrutura Conceitual para Trabalhos de Asseguração|2/2015/NBCTAESTRUTURACONCEITUAL
200 (R1)|Objetivos Gerais do Auditor Independente e a Condução da Auditoria em Conformidade com Normas de Auditoria|2/2016/NBCTA200(R1)
210 (R1)|Concordância com os Termos do Trabalho de Auditoria|2/2016/NBCTA210(R1)
220 (R3)|Gestão de Qualidade da Auditoria de Demonstrações Contábeis|2/2021/NBCTA220(R3)&arquivo=NBCTA220%20(R3).doc
230 (R1)|Documentação de Auditoria|2/2016/NBCTA230(R1)
240 (R2)|Responsabilidade do Auditor em Relação a Fraude|2/2026/NBCTA240(R2)&arquivo=NBCTA240(R2).docx
250|Consideração de Leis e Regulamentos na Auditoria de Demonstrações Contábeis|1/2019/NBCTA250
260 (R2)|Comunicação com os Responsáveis pela Governança|U/https://cfc.org.br/wp-content/uploads/2026/06/NBCTA260-R2-2.pdf
265|Comunicação de Deficiências de Controle Interno|2/2009/001210
300 (R1)|Planejamento da Auditoria de Demonstrações Contábeis|2/2016/NBCTA300(R1)
315 (R2)|Identificação e Avaliação dos Riscos de Distorção Relevante|2/2021/NBCTA315(R2)&arquivo=NBCTA315(R2).doc
320 (R1)|Materialidade no Planejamento e na Execução da Auditoria|1/2016/NBCTA320(R1)
330 (R1)|Resposta do Auditor aos Riscos Avaliados|2/2016/NBCTA330(R1)
402|Considerações de Auditoria para Entidade que Utiliza Organização Prestadora de Serviços|2/2009/001215
450 (R1)|Avaliação das Distorções Identificadas durante a Auditoria|2/2016/NBCTA450(R1)
500 (R1)|Evidência de Auditoria|2/2016/NBCTA500(R1)
501|Evidência de Auditoria – Considerações Específicas para Itens Selecionados|2/2009/001218
505|Confirmações Externas|2/2009/001219
510 (R1)|Trabalhos Iniciais – Saldos Iniciais|2/2016/NBCTA510(R1)
520|Procedimentos Analíticos|2/2009/001221
530|Amostragem em Auditoria|2/2009/001222
540 (R2)|Auditoria de Estimativas Contábeis, Inclusive do Valor Justo, e Divulgações Relacionadas|2/2019/NBCTA540(R2)&arquivo=NBCTA540(R2).doc
550|Partes Relacionadas|2/2009/001224
560 (R1)|Eventos Subsequentes|2/2016/NBCTA560(R1)
570 (R1)|Continuidade Operacional|2/2026/NBCTA570(R1)&arquivo=NBCTA570(R1).docx
580 (R1)|Representações Formais|2/2016/NBCTA580(R1)
600 (R2)|Auditorias de Demonstrações Contábeis de Grupos, Incluindo o Trabalho dos Auditores dos Componentes|2/2023/NBCTA600(R2)&arquivo=NBC%20TA%20600%20(R2).doc
610|Utilização do Trabalho de Auditoria Interna|2/2014/NBCTA610
620|Utilização do Trabalho de Especialistas|2/2009/001230
700|Formação da Opinião e Emissão do Relatório do Auditor Independente|U/https://cfc.org.br/wp-content/uploads/2026/06/NBCTA700.pdf
701|Comunicação dos Principais Assuntos de Auditoria (PAA)|2/2016/NBCTA701
705|Modificações na Opinião do Auditor Independente|2/2016/NBCTA705
706|Parágrafos de Ênfase e Parágrafos de Outros Assuntos|U/https://cfc.org.br/wp-content/uploads/2026/06/NBC-TA-706.pdf
710 (R1)|Informações Comparativas – Valores Correspondentes e Demonstrações Contábeis Comparativas|2/2016/NBCTA710(R1)
720|Responsabilidade do Auditor em Relação a Outras Informações|2/2016/NBCTA720
800|Auditorias de Demonstrações Elaboradas de Acordo com Estruturas Conceituais para Propósitos Especiais|2/2017/NBCTA800&arquivo=NBCTA800.doc
805|Auditoria de Quadros Isolados e de Elementos, Contas ou Itens Específicos das Demonstrações Contábeis|2/2017/NBCTA805&arquivo=NBCTA805.doc
810|Trabalhos para Emissão de Relatório sobre Demonstrações Contábeis Condensadas|2/2017/NBCTA810&arquivo=NBCTA810.doc"""

SERIES = [
("NBC TG – Pequenas e médias empresas e microentidades", "", """
NBC TG 1000 (R1)|Contabilidade para Pequenas e Médias Empresas (CPC PME)|2/2016/NBCTG1000(R1)&arquivo=NBCTG1000(R1).doc
NBC TG 1001|Contabilidade para Pequenas Empresas|2/2021/NBCTG1001&arquivo=NBCTG1001.doc
NBC TG 1002|Contabilidade para Microentidades|2/2021/NBCTG1002&arquivo=NBCTG1002.doc
ITG 1000|Modelo Contábil para Microentidade e Pequena Empresa|2/2022/ITG1000&arquivo=ITG%201000.doc
CTG 1000|Adoção Plena da NBC TG 1000|2/2013/CTG1000
"""),
("Normas específicas (ITG 2000 e outras)", "", """
ITG 2000 (R1)|Escrituração Contábil|2/2014/ITG2000(R1)&arquivo=ITG2000(R1).doc
ITG 2001|Entidade Fechada de Previdência Complementar|2/2022/ITG2001&arquivo=ITG%202001.doc
ITG 2002 (R1)|Entidade sem Finalidade de Lucros|2/2015/ITG2002(R1)&arquivo=ITG2002(R1).doc
ITG 2003 (R2)|Entidade Desportiva|2/2023/ITG2003(R2)&arquivo=ITG2003_R2.doc
ITG 2004|Entidade Cooperativa|2/2017/ITG2004&arquivo=ITG2004.doc
CTG 2000|Ajustes das Novas Práticas Contábeis da Lei 11.638/07 e MP 449/08|2/2009/001159&arquivo=Res_1159.doc
CTG 2001 (R3)|Formalidades da Escrituração Contábil em Forma Digital para o SPED|2/2017/CTG2001(R3)
CTG 2002|Laudo de Avaliação Emitido por Contador|2/2018/CTG2002&arquivo=CTG2002.doc
NBC T 15|Informações de Natureza Social e Ambiental|2/2004/001003&arquivo=Res_1003.doc
"""),
("NBC TSP – Setor público", "Convergidas com as IPSAS (IPSASB).\n\n", """
NBC TSP Estrutura Conceitual (R1)|Estrutura Conceitual para Informação Contábil de Propósito Geral pelas Entidades do Setor Público|2/2025/NBCTSPEC(R1)&arquivo=NBCTSP_Estrutura(R1).docx
NBC TSP 01|Receita de Transação sem Contraprestação|2/2016/NBCTSP01&arquivo=NBCTSP01.doc
NBC TSP 02|Receita de Transação com Contraprestação|2/2016/NBCTSP02&arquivo=NBCTSP02.doc
NBC TSP 03 (R1)|Provisões, Passivos Contingentes e Ativos Contingentes|2/2025/NBCTSP03(R1)&arquivo=NBCTSP03(R1).docx
NBC TSP 04 (R1)|Estoques|2/2025/NBCTSP04(R1)&arquivo=NBCTSP04(R1).docx
NBC TSP 05 (R1)|Contratos de Concessão de Serviços Públicos: Concedente|2/2025/NBCTSP05(R1)&arquivo=NBCTSP05(R1).docx
NBC TSP 06 (R1)|Propriedade para Investimento|2/2025/NBCTSP06(R1)&arquivo=NBCTSP06(R1).docx
NBC TSP 08 (R1)|Ativo Intangível|2/2025/NBCTSP08(R1)&arquivo=NBCTSP08(R1).docx
NBC TSP 09 (R1)|Redução ao Valor Recuperável de Ativo Não Gerador de Caixa|2/2025/NBCTSP09(R1)&arquivo=NBCTSP09(R1).docx
NBC TSP 10 (R1)|Redução ao Valor Recuperável de Ativo Gerador de Caixa|2/2025/NBCTSP10(R1)&arquivo=NBCTSP10(R1).docx
NBC TSP 11 (R1)|Apresentação das Demonstrações Contábeis|2/2025/NBCTSP11(R1)&arquivo=NBCTSP11(R1).docx
NBC TSP 12 (R1)|Demonstração dos Fluxos de Caixa|2/2025/NBCTSP12(R1)&arquivo=NBCTSP12(R1).docx
NBC TSP 13 (R1)|Apresentação de Informação Orçamentária nas Demonstrações Contábeis|2/2025/NBCTSP13(R1)&arquivo=NBCTSP13(R1).docx
NBC TSP 14 (R1)|Custos de Empréstimos|2/2025/NBCTSP14(R1)&arquivo=NBCTSP14(R1).docx
NBC TSP 15 (R1)|Benefícios a Empregados|2/2025/NBCTSP15(R1)&arquivo=NBCTSP15(R1).docx
NBC TSP 16 (R1)|Demonstrações Contábeis Separadas|2/2025/NBCTSP16(R1)&arquivo=NBCTSP16(R1).docx
NBC TSP 17 (R1)|Demonstrações Contábeis Consolidadas|2/2025/NBCTSP17(R1)&arquivo=NBCTSP17(R1).docx
NBC TSP 18 (R1)|Investimento em Coligada e em Empreendimento Controlado em Conjunto|2/2025/NBCTSP18(R1)&arquivo=NBCTSP18(R1).docx
NBC TSP 19 (R1)|Acordos em Conjunto|2/2025/NBCTSP19(R1)&arquivo=NBCTSP19(R1).docx
NBC TSP 20 (R1)|Divulgação de Participações em Outras Entidades|2/2025/NBCTSP20(R1)&arquivo=NBCTSP20(R1).docx
NBC TSP 21 (R1)|Combinações no Setor Público|2/2025/NBCTSP21(R1)&arquivo=NBCTSP21(R1).docx
NBC TSP 22 (R1)|Divulgação sobre Partes Relacionadas|2/2025/NBCTSP22(R1)&arquivo=NBCTSP22(R1).docx
NBC TSP 23 (R1)|Políticas Contábeis, Mudança de Estimativa e Retificação de Erro|2/2025/NBCTSP23(R1)&arquivo=NBCTSP23(R1).docx
NBC TSP 24 (R1)|Efeitos das Mudanças nas Taxas de Câmbio e Conversão de Demonstrações Contábeis|2/2025/NBCTSP24(R1)&arquivo=NBCTSP24(R1).docx
NBC TSP 25 (R1)|Evento Subsequente|2/2025/NBCTSP25(R1)&arquivo=NBCTSP25(R1).docx
NBC TSP 26 (R1)|Ativo Biológico e Produto Agrícola|2/2025/NBCTSP26(R1)&arquivo=NBCTSP26(R1).docx
NBC TSP 27 (R1)|Informações por Segmento|2/2025/NBCTSP27(R1)&arquivo=NBCTSP27(R1).docx
NBC TSP 28 (R1)|Divulgação de Informação Financeira do Setor Governo Geral|2/2025/NBCTSP28(R1)&arquivo=NBCTSP28(R1).docx
NBC TSP 29 (R1)|Benefícios Sociais|2/2025/NBCTSP29(R1)&arquivo=NBCTSP29(R1).docx
NBC TSP 30 (R1)|Instrumentos Financeiros: Apresentação|2/2025/NBCTSP30(R1)&arquivo=NBCTSP30(R1).docx
NBC TSP 31 (R1)|Instrumentos Financeiros: Reconhecimento e Mensuração|2/2025/NBCTSP31(R1)&arquivo=NBCTSP31(R1).docx
NBC TSP 32 (R1)|Instrumentos Financeiros: Contabilidade de Hedge (Aplicação Residual)|2/2025/NBCTSP32(R1)&arquivo=NBCTSP32(R1).docx
NBC TSP 33 (R1)|Instrumentos Financeiros: Divulgações|2/2025/NBCTSP33(R1)&arquivo=NBCTSP33(R1).docx
NBC TSP 34|Custos no Setor Público|2/2021/NBCTSP34&arquivo=NBCTSP34.doc
NBC TSP 35|Arrendamentos|2/2026/NBCTSP35&arquivo=NBCTSP35.docx
NBC TSP 37|Ativo Imobilizado|2/2025/NBCTSP37&arquivo=NBC_TSP_37.docx
NBC TSP 38|Mensuração|2/2026/NBCTSP38&arquivo=NBCTSP38.docx
CTSP 01|Provisões, Passivos Contingentes e Ativos Contingentes|2/2023/CTSP01&arquivo=CTSP_01.doc
CTSP 02|Notas Explicativas|2/2024/CTSP02&arquivo=CTSP-02.doc
"""),
("NBC TDS – Sustentabilidade", "Correlatas às IFRS S1 e S2 (ISSB) e aos CBPS 01 e 02.\n\n", """
NBC TDS 01|Requisitos Gerais para Divulgação de Informações Financeiras Relacionadas à Sustentabilidade (IFRS S1)|2/2024/NBCTDS01&arquivo=NBCTDS_01.doc
NBC TDS 02|Divulgações Relacionadas ao Clima (IFRS S2)|2/2024/NBCTDS02&arquivo=NBCTDS_02.doc
NBC TAS 5000|Asseguração de Relatórios de Sustentabilidade (ISSA 5000)|2/2025/NBCTAS5000&arquivo=NBCTAS5000.docx
"""),
("NBC TR – Revisão", "", """
NBC TR 2400|Trabalhos de Revisão de Demonstrações Contábeis|2/2013/NBCTR2400
NBC TR 2410|Revisão de Informações Intermediárias Executada pelo Auditor da Entidade|2/2010/001274
CTR 01 (R1)|Relatório de Revisão sobre as Informações Trimestrais (ITR)|2/2019/CTR01(R1)
CTR 02|Relatório de Revisão das ITR e IFT de Instituições Autorizadas pelo Banco Central|2/2011/001353
CTR 03|Relatório de Revisão sobre ITR de Entidade de Incorporação Imobiliária|2/2018/NBCCTR03&arquivo=NBCCTR03.doc
CTR 04|Relatório de Revisão sobre ITR de Entidade de Incorporação Imobiliária|2/2019/NBCCTR04
"""),
("NBC TO – Asseguração", "", """
NBC TO 3000|Trabalhos de Asseguração Diferente de Auditoria e Revisão|2/2015/NBCTO3000
NBC TO 3402|Relatórios de Asseguração sobre Controles em Organização Prestadora de Serviços|1/2011/001354&arquivo=Res_1354.doc
NBC TO 3410|Trabalhos de Asseguração sobre Declarações de Gases de Efeito Estufa|2/2023/NBCTO%203410&arquivo=NBC%20TO%203410.doc
NBC TO 3420 (R1)|Asseguração sobre a Compilação de Informações Financeiras Pro Forma Incluídas em Prospecto|2/2015/NBCTO3420(R1)
CTO 01|Relatório de Asseguração sobre Sustentabilidade e Responsabilidade Social|2/2012/001407
CTO 02|Asseguração Razoável sobre Informações Financeiras Pro Forma (Instrução CVM 565)|2/2016/CTO02
CTO 03|Relatórios sobre Serviços de Depósito Centralizado, Custódia, Escrituração e Emissão de Certificados|2/2016/CTO03&arquivo=CTO03.doc
CTO 04 (R1)|Orientação aos Auditores (alteração da CTO 04)|2/2020/CTO04(R1)&arquivo=CTO04%20(R1).doc
CTO 05 (R2)|Asseguração Razoável sobre o Relatório de Dados Anuais (RDA)|U/https://cfc.org.br/wp-content/uploads/2023/09/CTO-05-R2.final_.docx
CTO 06|Asseguração Razoável na Relicitação de Contratos de Parceria Aeroportuária|2/2021/CTO06
CTO 07|Asseguração Limitada sobre Informações Não Financeiras do Relato Integrado|2/2022%20CTO%2007&arquivo=CTO%2007%20.doc
CTO 08|Asseguração Razoável na Relicitação de Contratos de Parceria Rodoviária|2/2022%20CTO%2008&arquivo=CTO08.doc
"""),
("NBC TSC – Serviços correlatos", "", """
NBC TSC 4400|Trabalhos de Procedimentos Previamente Acordados sobre Informações Contábeis (ISRS 4400)|2/2021/NBCTSC4400&arquivo=NBC-TSC_4400.doc
NBC TSC 4410|Trabalhos de Compilação de Demonstrações Contábeis (ISRS 4410)|2/2013/NBCTSC4410
CTSC 02|Procedimentos Previamente Acordados – Despacho ANEEL 514/12|2/2012/001400
CTSC 03|Procedimentos Previamente Acordados – Termo de Verificação para Substituição da ECD|2/2017/CTSC03&arquivo=CTSC03.doc
CTSC 04|Procedimentos Previamente Acordados – Questionário de Riscos Susep|2/2018/CTSC04&arquivo=CTSC04.doc
CTSC 05|Procedimentos Previamente Acordados – Art. 242 da Circular Susep 517|2/2020/CTSC05&arquivo=NBCCTSC05.doc
CTSC 06|Procedimentos Previamente Acordados – Circular Susep 574|2/2020/CTSC06&arquivo=NBCCTSC06.doc
"""),
("NBC TI – Auditoria interna", "", """
NBC TI 01|Da Auditoria Interna (Res. CFC 986/03)|2/2003/000986
"""),
("NBC TP – Perícia", "", """
NBC TP 01 (R2)|Perícia Contábil|2/2025/NBCTP01(R2)&arquivo=NBCTP01(R2).doc
ITP 01|Apuração de Haveres|2/2025/ITP01&arquivo=ITP_01_Apuracao%20de%20Haveres.docx
"""),
("NBC PG – Profissionais gerais (ética)", "", """
NBC PG 01|Código de Ética Profissional do Contador|2/2019/NBCPG01&arquivo=NBCPG01.doc
NBC PG 12 (R5)|Educação Profissional Continuada|2/2025/NBCPG12(R5)&arquivo=NBCPG12(R5).docx
NBC PG 100 (R1)|Cumprimento do Código, Princípios Fundamentais e Estrutura Conceitual|1/2019/NBCPG100(R1)&arquivo=NBCPG100(R1).doc
NBC PG 200 (R1)|Contadores que Prestam Serviços (Contadores Internos)|1/2019/NBCPG200(R1)&arquivo=NBCPG200(R1).doc
NBC PG 300 (R1)|Contadores que Prestam Serviços (Contadores Externos)|1/2019/NBCPG300(R1)&arquivo=NBCPG300(R1).doc
"""),
("NBC PA – Auditor independente", "", """
NBC PA 01|Gestão de Qualidade para Firmas de Auditores Independentes|2/2021/NBCPA01&arquivo=NBCPA01.doc
NBC PA 02|Revisão de Qualidade do Trabalho|2/2021/NBCPA02&arquivo=NBCPA02.doc
NBC PA 11|Revisão Externa de Qualidade pelos Pares|2/2017/NBCPA11&arquivo=NBCPA11.doc
NBC PA 13 (R4)|Exame de Qualificação Técnica|2/2025/NBCPA13(R4)&arquivo=NBCPA13(R4).docx
NBC PA 400|Independência para Trabalho de Auditoria e Revisão|2/2019/NBCPA400&arquivo=NBCPA400_Rev28.doc
NBC PO 900|Independência para Trabalho de Asseguração Diferente de Auditoria e Revisão|1/2019/NBCPO900&arquivo=NBCPO900.doc
Res. CFC 1.495/15|Cadastro Nacional de Auditores Independentes (CNAI)|1/2015/001495
"""),
("NBC PP – Perito contábil", "", """
NBC PP 01 (R2)|Perito Contábil|2/2025/NBCPP01(R2)&arquivo=NBCPP01(R2).doc
NBC PP 02 (R1)|Exame de Qualificação Técnica para Perito Contábil|2/2025/NBCPP02(R1)&arquivo=NBCPP02(R1).doc
"""),
]

IFRS = """
IFRS 1|Adoção Inicial das IFRS|CPC 37|NBC TG 37
IFRS 2|Pagamento Baseado em Ações|CPC 10|NBC TG 10
IFRS 3|Combinação de Negócios|CPC 15|NBC TG 15
IFRS 5|Ativo Não Circulante Mantido para Venda e Operação Descontinuada|CPC 31|NBC TG 31
IFRS 6|Exploração e Avaliação de Recursos Minerais|—|—
IFRS 7|Instrumentos Financeiros: Evidenciação|CPC 40|NBC TG 40
IFRS 8|Segmentos Operacionais|CPC 22|NBC TG 22
IFRS 9|Instrumentos Financeiros|CPC 48|NBC TG 48
IFRS 10|Demonstrações Consolidadas|CPC 36|NBC TG 36
IFRS 11|Negócios em Conjunto|CPC 19|NBC TG 19
IFRS 12|Divulgação de Participações em Outras Entidades|CPC 45|NBC TG 45
IFRS 13|Mensuração do Valor Justo|CPC 46|NBC TG 46
IFRS 14|Contas Regulatórias Diferidas|—|—
IFRS 15|Receita de Contrato com Cliente|CPC 47|NBC TG 47
IFRS 16|Arrendamentos|CPC 06|NBC TG 06
IFRS 17|Contratos de Seguro|CPC 50|NBC TG 50
IFRS 18|Apresentação e Divulgação nas Demonstrações Financeiras|CPC 51|NBC TG 51
IFRS 19|Controladas sem Responsabilidade Pública: Divulgações|CPC 52|—
IAS 1|Apresentação das Demonstrações Contábeis (substituída pela IFRS 18 a partir de 2027)|CPC 26|NBC TG 26
IAS 2|Estoques|CPC 16|NBC TG 16
IAS 7|Demonstração dos Fluxos de Caixa|CPC 03|NBC TG 03
IAS 8|Políticas Contábeis, Mudança de Estimativa e Retificação de Erro|CPC 23|NBC TG 23
IAS 10|Evento Subsequente|CPC 24|NBC TG 24
IAS 12|Tributos sobre o Lucro|CPC 32|NBC TG 32
IAS 16|Ativo Imobilizado|CPC 27|NBC TG 27
IAS 19|Benefícios a Empregados|CPC 33|NBC TG 33
IAS 20|Subvenção e Assistência Governamentais|CPC 07|NBC TG 07
IAS 21|Efeitos das Mudanças nas Taxas de Câmbio|CPC 02|NBC TG 02
IAS 23|Custos de Empréstimos|CPC 20|NBC TG 20
IAS 24|Divulgação sobre Partes Relacionadas|CPC 05|NBC TG 05
IAS 26|Planos de Benefícios de Aposentadoria|CPC 49|NBC TG 49
IAS 27|Demonstrações Separadas|CPC 35|NBC TG 35
IAS 28|Investimento em Coligada e Empreendimento Controlado em Conjunto|CPC 18|NBC TG 18
IAS 29|Contabilidade em Economia Hiperinflacionária|CPC 42|NBC TG 42
IAS 32|Instrumentos Financeiros: Apresentação|CPC 39|NBC TG 39
IAS 33|Resultado por Ação|CPC 41|NBC TG 41
IAS 34|Demonstração Intermediária|CPC 21|NBC TG 21
IAS 36|Redução ao Valor Recuperável de Ativos|CPC 01|NBC TG 01
IAS 37|Provisões, Passivos Contingentes e Ativos Contingentes|CPC 25|NBC TG 25
IAS 38|Ativo Intangível|CPC 04|NBC TG 04
IAS 40|Propriedade para Investimento|CPC 28|NBC TG 28
IAS 41|Agricultura (Ativo Biológico e Produto Agrícola)|CPC 29|NBC TG 29
IFRS for SMEs|IFRS para Pequenas e Médias Empresas|CPC PME|NBC TG 1000
IFRS S1|Requisitos Gerais de Divulgação de Sustentabilidade|CBPS 01|NBC TDS 01
IFRS S2|Divulgações Relacionadas ao Clima|CBPS 02|NBC TDS 02
"""

def url(p):
    if p.startswith("U/"):
        u = p[2:]
    else:
        n, rest = p.split("/", 1)
        u = (B1 if n == "2" else B0) + rest
    return u.replace(' ', '%20')

# links oficiais do CPC (scripts/cpc.json, gerado por scripts/atualizar_cpc.py)
import json as _json, re as _re
from pathlib import Path as _P
def _ncpc(c):
    return _re.sub(r"\s*\(R\d+\)", "", c or "").replace(" ", "").upper()
_cpcj = _P(__file__).resolve().parent / "cpc.json"
CPC_URL = {_ncpc(x["codigo"]): x["url"] for x in _json.loads(_cpcj.read_text(encoding="utf-8"))} if _cpcj.exists() else {}
def link_cpc(c):
    u = CPC_URL.get(_ncpc(c))
    return f"[{c}]({u})" if u else (c or "—")

def link(p):
    return f"[abrir]({url(p)})"

HEAD = """# Normas Contábeis Brasileiras: CPC, NBC TG, ITG e NBC TA

Índice das normas contábeis e de auditoria do Brasil, com links para os textos oficiais:
pronunciamentos do **CPC** (Comitê de Pronunciamentos Contábeis), **NBC TG / ITG / CTG** (contabilidade)
e **NBC TA** (auditoria independente) do **CFC** (Conselho Federal de Contabilidade).

> **Aviso:** este repositório não hospeda o texto das normas. Os documentos têm direitos autorais
> (parte deriva das IFRS © IFRS Foundation e das ISA © IFAC) e são revisados com frequência.
> Os links levam ao texto no site do CFC. Confira sempre a versão vigente. Este índice não é aconselhamento profissional.

## Sumário
- [Fontes oficiais](#fontes-oficiais)
- [Como ler a numeração](#como-ler-a-numeração)
- [NBC TG (correlação CPC / IFRS)](#nbc-tg--normas-técnicas-gerais)
- [ITG / CTG / OTG (ICPC / OCPC)](#itg--ctg--otg--interpretações-e-comunicados)
- [NBC TA (auditoria independente)](#nbc-ta--auditoria-independente)
- PMEs (NBC TG 1000), normas específicas (ITG 2000), NBC TSP, NBC TDS, NBC TR, NBC TO, NBC TSC, NBC TI, NBC TP, NBC PG, NBC PA e NBC PP: logo após as NBC TA
- [IFRS e IAS (IASB)](#normas-internacionais--ifrs-e-ias-iasb)

## Fontes oficiais
- CFC, Normas Brasileiras de Contabilidade: <https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/>
- CFC, normas completas (NBC TG, ITG, CTG): <https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/normas-completas/>
- CFC, NBC TA: <https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/>
- CPC: <https://www.cpc.org.br>
- CVM: <https://www.gov.br/cvm>

- IFRS Foundation (IFRS, IAS, IFRS S): <https://www.ifrs.org/issued-standards/list-of-standards/>
- IAASB (ISA): <https://www.iaasb.org/standards-pronouncements>

## Como ler a numeração
`CPC 26 (R1)` é o pronunciamento do CPC. O CFC o torna obrigatório para os contadores como `NBC TG 26 (R5)`.
`(Rn)` indica a revisão. As interpretações `ICPC` correspondem às `ITG`, e as orientações `OCPC` correspondem aos `CTG`.
"""

out = [HEAD]
out.append("## NBC TG – Normas técnicas gerais\n\n| NBC TG | Título | CPC | IFRS/IAS | Texto |\n|---|---|---|---|---|")
for l in tg.splitlines():
    c, t, cpc, i, p = l.split("|")
    code = "NBC TG Estrutura Conceitual" if c == "ESTRUTURA CONCEITUAL" else "NBC TG " + c
    out.append(f"| {code} | {t} | {link_cpc(cpc) if cpc != '—' else cpc} | {i} | {link(p)} |")
out.append("\n## ITG / CTG / OTG – Interpretações e comunicados\n\n| Norma | Título | CPC equivalente | Texto |\n|---|---|---|---|")
for l in itg.splitlines():
    c, t, cpc, p = l.split("|")
    out.append(f"| {c} | {t} | {link_cpc(cpc) if cpc != '—' else cpc} | {link(p)} |")
out.append("\n## NBC TA – Auditoria independente\n\nNormas convergidas com as ISA (IAASB/IFAC).\n\n| NBC TA | Título | Texto |\n|---|---|---|")
for l in ta.splitlines():
    c, t, p = l.split("|")
    out.append(f"| NBC TA {c} | {t} | {link(p)} |")
for title, intro, data in SERIES:
    out.append(f"\n## {title}\n\n{intro}| Norma | Título | Texto |\n|---|---|---|")
    for l in data.strip().splitlines():
        c, t, p = l.split("|")
        out.append(f"| {c} | {t} | {link(p)} |")

out.append("\n## Normas internacionais – IFRS e IAS (IASB)\n\n"
           "Textos oficiais (em inglês, cadastro gratuito no site da IFRS Foundation): "
           "<https://www.ifrs.org/issued-standards/list-of-standards/>. "
           "A coluna CPC / NBC TG indica a norma brasileira convergida.\n\n"
           "| Norma | Título | CPC | NBC TG |\n|---|---|---|---|")
for l in IFRS.strip().splitlines():
    c, t, cpc, tgx = l.split("|")
    out.append(f"| {c} | {t} | {link_cpc(cpc) if cpc != '—' else cpc} | {tgx} |")
out.append("\nAs **NBC TA** seguem a mesma numeração das **ISA** do IAASB (ex.: NBC TA 700 = ISA 700). "
           "Textos das ISA: <https://www.iaasb.org/standards-pronouncements>.")

out.append("""
## Contribuir
Encontrou link quebrado, norma nova ou revisão? Abra uma *issue* ou um *pull request*.
Última conferência do índice: 2026-10-23.

## Licença
O índice (organização e metadados) está em domínio público sob [CC0 1.0](LICENSE).
Os textos das normas pertencem aos respectivos titulares.
""")
import json, re, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

# ---------- registros estruturados ----------
REC = []
def add(codigo, titulo, serie, link_url=None, cpc=None, internacional=None):
    REC.append({"codigo": codigo, "titulo": titulo, "serie": serie, "url": link_url,
                "cpc": None if cpc in (None, "—") else cpc,
                "internacional": None if internacional in (None, "—", "Framework") else internacional})

for l in tg.splitlines():
    c, t, cpc, i, p = l.split("|")
    add("NBC TG Estrutura Conceitual" if c == "ESTRUTURA CONCEITUAL" else "NBC TG " + c, t, "NBC TG", url(p), cpc, i)
for l in itg.splitlines():
    c, t, cpc, p = l.split("|")
    add(c, t, c.split()[0], url(p), cpc)
for l in ta.splitlines():
    c, t, p = l.split("|")
    num = c.split()[0]
    add("NBC TA " + c, t, "NBC TA", url(p), None, f"ISA {num}" if num.isdigit() else None)
SERIE_DE = {"NBC TG – Pequenas": "PME", "Normas específicas": "Específicas"}
for title, _, data in SERIES:
    for l in data.strip().splitlines():
        c, t, p = l.split("|")
        serie = next((v for k, v in SERIE_DE.items() if title.startswith(k)), title.split(" –")[0])
        add(c, t, serie, url(p))
for l in IFRS.strip().splitlines():
    c, t, cpc, tgx = l.split("|")
    add(c, t, "IFRS/IAS", "https://www.ifrs.org/issued-standards/list-of-standards/", None if cpc == "—" else cpc, tgx if tgx != "—" else None)

# ---------- o que cada norma trata e afeta (scripts/resumos.py) ----------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from resumos import R as RESUMOS
def sem_rev(c):
    return re.sub(r"\s*\(R\d+\)", "", c).strip()
faltando = []
for r in REC:
    txt = RESUMOS.get(sem_rev(r["codigo"])) or (r["internacional"] and RESUMOS.get(sem_rev(r["internacional"])))
    if not txt:
        faltando.append(r["codigo"]); txt = "|"
    r["resumo"], r["afeta"] = txt.split("|", 1)
    r["url_cpc"] = CPC_URL.get(_ncpc(r["cpc"])) if r["cpc"] else None
assert not faltando, f"sem resumo: {faltando}"

# ---------- situação: normas que o CFC revogou (conferido em scripts/verificar_links.py) ----------
REVOGADAS = {
 "NBC TG 26": "Revogada pela NBC TG 51 (aprovada em 13/11/2025, DOU 25/02/2026), que se aplica aos exercícios iniciados a partir de 1/1/2027. Use a NBC TG 26 só para exercícios anteriores.",
 "CTR 03": "Revogada pela CTR 04 (2019).",
 "NBC TO 3410": "Revogada pela NBC TAS 5000 (DOU 18/12/2025).",
 "CTO 01": "Revogada pela CTO 07 (2022).",
}
for r in REC:
    r["situacao"] = REVOGADAS.get(sem_rev(r["codigo"]), "vigente")
    if r["situacao"] != "vigente":
        r["resumo"] = "⚠ " + r["situacao"] + " " + r["resumo"]

# ---------- áreas por série ----------
AREA_SERIE = {
    "NBC TA": "Auditoria Independente", "NBC TR": "Revisão", "NBC TO": "Asseguração",
    "NBC TSC": "Serviços Correlatos", "NBC TI": "Auditoria Interna", "NBC TP": "Perícia Contábil",
    "NBC PP": "Perícia Contábil", "NBC PG": "Ética e Exercício Profissional",
    "NBC PA": "Ética e Exercício Profissional", "NBC TSP": "Setor Público",
    "NBC TDS": "Sustentabilidade", "PME": "Pequenas e Médias Empresas", "IFRS/IAS": "Normas Internacionais",
}

# ---------- temas (palavra de busca -> regex no título + sinônimos) ----------
# (tema, área contábil, regex, sinônimos para busca)
TEMAS = [
 ("Imobilizado", "Ativos", r"imobilizad", "ativo fixo, depreciação, vida útil, PP&E, máquinas, edificações, IAS 16"),
 ("Intangível", "Ativos", r"intang", "ágio, goodwill, software, marcas, patentes, amortização, IAS 38"),
 ("Estoques", "Ativos", r"estoque", "inventário, custo de produção, CMV, IAS 2"),
 ("Propriedade para investimento", "Ativos", r"propriedade para investimento", "imóveis para renda, IAS 40"),
 ("Ativo biológico", "Ativos", r"biológic|agricultura", "agronegócio, rebanho, safra, IAS 41"),
 ("Redução ao valor recuperável (impairment)", "Ativos", r"valor recuperável", "impairment, teste de recuperabilidade, IAS 36"),
 ("Arrendamentos", "Ativos", r"arrendament", "leasing, aluguel, direito de uso, IFRS 16"),
 ("Ativo mantido para venda", "Ativos", r"mantido para venda|descontinuad", "operação descontinuada, IFRS 5"),
 ("Instrumentos financeiros", "Instrumentos Financeiros", r"instrumentos? financeir|passivos financeiros|hedge", "derivativos, hedge, perda esperada, PCLD, aplicações, IFRS 9"),
 ("Valor justo e mensuração", "Mensuração", r"valor justo|mensuração", "fair value, IFRS 13"),
 ("Ajuste a valor presente", "Mensuração", r"valor presente", "AVP, desconto"),
 ("Receita", "Receitas", r"receita", "faturamento, contrato com cliente, obrigação de desempenho, IFRS 15"),
 ("Subvenção governamental", "Receitas", r"subvenç", "incentivo fiscal, subsídio, IAS 20"),
 ("Provisões e contingências", "Passivos", r"provis|conting", "processos judiciais, passivo contingente, IAS 37"),
 ("Benefícios a empregados", "Passivos", r"empregados|aposentadoria|benefício definido|previdência|benefícios sociais", "plano de pensão, previdência, IAS 19"),
 ("Custos de empréstimos", "Passivos", r"custos de empréstimos", "juros capitalizados, IAS 23"),
 ("Tributos sobre o lucro", "Tributos", r"tribut", "IR, CSLL, imposto diferido, IAS 12"),
 ("Patrimônio, dividendos e ações", "Patrimônio Líquido", r"dividend|lucros in natura|resultado por ação|baseado em ações|instrumentos patrimoniais", "stock options, lucro por ação, JCP"),
 ("Câmbio e inflação", "Moeda e Câmbio", r"câmbio|moeda estrangeira|hiperinflac|atualização monetária", "conversão, moeda funcional, IAS 21, IAS 29"),
 ("Consolidação e participações", "Participações Societárias", r"consolidad|coligada|em conjunto|combinaç|separadas|participações em outras|equivalência|combinadas|grupos", "MEP, controladas, coligadas, joint venture, fusão e aquisição, IFRS 3, IFRS 10"),
 ("Demonstrações contábeis e divulgação", "Apresentação e Divulgação", r"apresentação|divulgaç|fluxos de caixa|valor adicionado|intermediári|segmento|partes relacionadas|subsequente|notas explicativas|evidenciação|orçamentária|pro forma|comparativas|condensadas|quadros isolados", "balanço, DRE, DFC, DVA, DMPL, notas explicativas, IAS 1, IFRS 18"),
 ("Políticas contábeis e erros", "Apresentação e Divulgação", r"políticas contábeis|estimativa|retificação", "mudança de estimativa, retificação de erro, IAS 8"),
 ("Estrutura conceitual", "Fundamentos", r"estrutura conceitual", "princípios, framework, características qualitativas"),
 ("Adoção inicial", "Fundamentos", r"adoção inicial|adoção plena|aplicação inicial|novas práticas|convergidas", "first-time adoption, Lei 11.638, IFRS 1"),
 ("Escrituração contábil", "Fundamentos", r"escrituração|sped|plano de contas|modelo contábil", "livros, SPED, ECD, plano de contas"),
 ("Seguros", "Setores Específicos", r"seguro|susep", "seguradoras, IFRS 17, SUSEP"),
 ("Concessões e infraestrutura", "Setores Específicos", r"concess|aeroportu|rodoviári|aneel|energia elétrica", "concessão pública, energia, rodovias, aeroportos"),
 ("Incorporação imobiliária", "Setores Específicos", r"imobiliári", "construtoras, incorporadoras"),
 ("Mineração e meio ambiente", "Setores Específicos", r"minera|estéril|desativação|ambiental|eletroeletrônic|recursos minerais", "mineração, descomissionamento, IFRS 6"),
 ("Entidades específicas", "Setores Específicos", r"sem finalidade|cooperativa|desportiv|previdência complementar|liquidação", "terceiro setor, ONG, cooperativas, clubes, fundos de pensão"),
 ("Sustentabilidade e clima", "Sustentabilidade", r"sustentabilidade|clima|carbono|gases de efeito|relato integrado|social e ambiental|responsabilidade social", "ESG, ISSB, IFRS S1, IFRS S2, créditos de carbono"),
 ("Custos no setor público", "Setor Público", r"custos no setor", "custos governamentais"),
 ("Fraude", "Auditoria Independente", r"fraude", "erro, distorção intencional, ISA 240"),
 ("Riscos, materialidade e planejamento", "Auditoria Independente", r"risco|materialidade|planejamento|distorç|controle interno|termos do trabalho|leis e regulamentos", "avaliação de risco, materialidade, planejamento de auditoria"),
 ("Evidência de auditoria", "Auditoria Independente", r"\bevidência|confirmaç|amostragem|analític|saldos iniciais|representações|documentação|estimativas contábeis|continuidade", "procedimentos de auditoria, circularização, amostragem"),
 ("Relatório do auditor", "Auditoria Independente", r"relatório|opinião|ênfase|principais assuntos|outras informações", "parecer, opinião modificada, PAA, ressalva"),
 ("Qualidade e independência", "Ética e Exercício Profissional", r"qualidade|independência|ética|código|educação profissional|qualificação técnica|cadastro|contadores que", "ética profissional, EPC, CNAI, revisão pelos pares"),
 ("Perícia contábil", "Perícia Contábil", r"períci|perito|haveres", "laudo pericial, perito judicial, apuração de haveres"),
 ("Uso do trabalho de terceiros", "Auditoria Independente", r"especialistas|auditoria interna|prestadora de serviços|governança|auditores dos componentes", "especialistas, auditoria interna, organização prestadora de serviços"),
 ("Procedimentos previamente acordados e compilação", "Serviços Correlatos", r"previamente acordados|compilação", "PPA, compilação, ISRS 4400, ISRS 4410"),
 ("Laudo de avaliação", "Fundamentos", r"laudo de avaliação", "avaliação patrimonial por contador"),
]

# temas que o título não revela (ex.: IFRS 18 "Apresentação e Divulgação" muda na prática a DRE)
TEMAS += [
 ("Demonstração do resultado (DRE)", "Apresentação e Divulgação", None, "DRE, lucro, resultado operacional, EBITDA, MPM, IFRS 18, lucro por ação"),
 ("Fluxo de caixa (DFC)", "Apresentação e Divulgação", None, "DFC, método direto, método indireto, caixa e equivalentes, IAS 7"),
 ("Valor adicionado (DVA)", "Apresentação e Divulgação", None, "DVA, riqueza gerada, distribuição do valor adicionado"),
 ("Pequenas e médias empresas", "Pequenas e Médias Empresas", r"pequena|microentidade|\bpme\b|smes", "PME, ME, EPP, pequena empresa, microentidade, IFRS for SMEs, CPC PME"),
]
TEMA_COD = {
 "Demonstração do resultado (DRE)": ["NBC TG 51", "IFRS 18", "NBC TG 26", "IAS 1", "NBC TG 41", "IAS 33", "NBC TG 31", "IFRS 5"],
 "Fluxo de caixa (DFC)": ["NBC TG 03", "IAS 7", "NBC TSP 12"],
 "Valor adicionado (DVA)": ["NBC TG 09"],
}
# temas de auditoria/profissão só valem para normas dessas séries (evita "Relatório Financeiro" virar relatório do auditor)
TEMAS_AUDITORIA = {"Fraude", "Riscos, materialidade e planejamento", "Evidência de auditoria", "Relatório do auditor",
                   "Qualidade e independência", "Uso do trabalho de terceiros", "Procedimentos previamente acordados e compilação"}
SERIES_CONTABEIS = {"NBC TG", "ITG", "CTG", "OTG", "Específicas", "PME", "NBC TSP", "IFRS/IAS"}

def norm(s):
    return unicodedata.normalize("NFC", s.lower())

CONTABIL_FALLBACK = "Contabilidade Geral"
for r in REC:
    t = norm(r["titulo"])
    cod = re.sub(r"\s*\(R\d+\)", "", r["codigo"]).strip()
    r["temas"] = [nome for nome, _, rx, _ in TEMAS
                  if (rx and re.search(rx, t) or cod in TEMA_COD.get(nome, []))
                  and not (nome in TEMAS_AUDITORIA and (r["serie"] in SERIES_CONTABEIS or r["serie"].startswith("CTSP")))]
    areas = []
    if r["serie"] in AREA_SERIE:
        areas.append(AREA_SERIE[r["serie"]])
    for nome, area, _, _ in TEMAS:
        if nome in r["temas"] and area not in areas and r["serie"] not in ("NBC TA", "NBC TR", "NBC TO", "NBC TSC", "NBC PA", "NBC PG", "NBC PP", "NBC TP", "NBC TI"):
            areas.append(area)
    r["areas"] = areas or [CONTABIL_FALLBACK]

SINONIMOS = {nome: sin for nome, _, _, sin in TEMAS}
AREA_DO_TEMA = {nome: area for nome, area, _, _ in TEMAS}

# ---------- pasta Industrial/ (trechos das normas para a indústria) ----------
import industrial
TOPICOS_IND = industrial.gerar(ROOT, REC, sem_rev)

(ROOT / "normas.json").write_text(json.dumps({
    "descricao": "Índice das normas contábeis e de auditoria brasileiras (CFC/CPC) e internacionais (IFRS/IAS), por área e tema.",
    "atualizado_em": "2026-10-23",
    "temas": [{"tema": n, "area": a, "sinonimos": s} for n, a, _, s in TEMAS],
    "normas": REC,
}, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- pasta areas/ (um arquivo por área) ----------
from collections import defaultdict
por_area = defaultdict(list)
for r in REC:
    for a in r["areas"]:
        por_area[a].append(r)
ordem = sorted(por_area, key=lambda a: (a == "Normas Internacionais", a))

DEMOS = [("BP", "Balanço patrimonial"), ("DRE", "Demonstração do resultado"), ("DRA", "Resultado abrangente / ORA"),
         ("DMPL", "Mutações do patrimônio líquido"), ("DFC", "Fluxos de caixa"), ("DVA", "Valor adicionado"),
         ("NE", "Notas explicativas"), ("DVP", "Variações patrimoniais (setor público)")]

# quando usar cada área (vai no topo do arquivo da área e no índice)
QUANDO = {
 "Ativos": "imobilizado, intangível, estoques, arrendamento, impairment, ativo biológico, propriedade para investimento, ativo à venda",
 "Passivos": "provisões, contingências, processos, benefícios a empregados, previdência, custos de empréstimos",
 "Receitas": "reconhecimento de receita, contrato com cliente, subvenções e incentivos fiscais",
 "Tributos": "IR e CSLL, imposto diferido, incerteza fiscal, taxas e tributos",
 "Patrimônio Líquido": "dividendos, JCP, ações, stock options, lucro por ação",
 "Instrumentos Financeiros": "aplicações, empréstimos, derivativos, hedge, PCLD/perda esperada",
 "Mensuração": "valor justo, ajuste a valor presente",
 "Moeda e Câmbio": "variação cambial, moeda funcional, conversão, hiperinflação",
 "Participações Societárias": "consolidação, equivalência patrimonial, coligadas, joint venture, combinação de negócios, ágio",
 "Apresentação e Divulgação": "balanço, DRE, DFC, DVA, notas explicativas, IFRS 18, políticas e erros, eventos subsequentes, segmentos",
 "Fundamentos": "estrutura conceitual, adoção inicial, escrituração, SPED, laudo de avaliação",
 "Setores Específicos": "seguros, concessões, energia, incorporação imobiliária, mineração, terceiro setor, cooperativas, clubes",
 "Pequenas e Médias Empresas": "PME, pequena empresa, microentidade, NBC TG 1000",
 "Setor Público": "governo, prefeituras, autarquias, NBC TSP, IPSAS",
 "Sustentabilidade": "ESG, clima, IFRS S1/S2, carbono, relato integrado",
 "Auditoria Independente": "auditoria de demonstrações, NBC TA, ISA, relatório/parecer do auditor, riscos, evidência",
 "Revisão": "revisão de ITR e demonstrações (segurança limitada)",
 "Asseguração": "asseguração de controles, sustentabilidade, pro forma, relatórios regulatórios",
 "Serviços Correlatos": "procedimentos previamente acordados, compilação",
 "Auditoria Interna": "auditor interno",
 "Perícia Contábil": "perícia judicial, laudo pericial, apuração de haveres",
 "Ética e Exercício Profissional": "código de ética, independência, educação continuada, CNAI, qualidade de firmas",
 "Normas Internacionais": "IFRS, IAS, IFRS for SMEs, IFRS S1/S2 e correlação com CPC",
}

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

import shutil
pasta = ROOT / "areas"
shutil.rmtree(pasta, ignore_errors=True); pasta.mkdir()
(ROOT / "AREAS.md").unlink(missing_ok=True)

def linha(r):
    refs = " · ".join(x for x in ((link_cpc(r["cpc"]) if r["cpc"] else None), r["internacional"]) if x) or "—"
    return f"| **{r['codigo']}** – {r['titulo']} | {r['resumo']} | {r['afeta']} | {refs} | [abrir]({r['url']}) |"

for a in ordem:
    temas_a = [(n, s) for n, ar, _, s in TEMAS if ar == a and any(n in r["temas"] for r in por_area[a])]
    md = [f"# Área: {a}\n",
          f"**Use esta área para:** {QUANDO.get(a, a)}.\n",
          f"{len(por_area[a])} normas. Índice de todas as áreas: [areas/README.md](README.md).\n"]
    if temas_a:
        md.append("## Temas desta área\n\n| Tema | Também chamado de | Normas |\n|---|---|---|")
        for n, sin in temas_a:
            md.append(f"| {n} | {sin} | {', '.join(r['codigo'] for r in por_area[a] if n in r['temas'])} |")
    md.append("\n## Normas\n\n| Norma | O que trata | Afeta | CPC / Internacional | Texto |\n|---|---|---|---|---|")
    md += [linha(r) for r in por_area[a]]
    (pasta / f"{slug(a)}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

idx = ["# Índice por área\n",
       "Cada área tem um arquivo com o resumo de cada norma, o que ela afeta e o link oficial. "
       "Comece pela tabela abaixo; se souber só o assunto, use a busca por tema.\n",
       "## Áreas\n\n| Área | Use para | Normas | Arquivo |\n|---|---|---|---|"]
for a in ordem:
    idx.append(f"| **{a}** | {QUANDO.get(a, '')} | {len(por_area[a])} | [{slug(a)}.md]({slug(a)}.md) |")
idx.append("\n## Por setor\n\n| Setor | Use para | Pasta |\n|---|---|---|\n"
           "| **Indústria** | custo de produção, estoques, máquinas, vendas e garantia, incentivos de ICMS, P&D, commodities, meio ambiente, auditoria de estoques "
           "| [Industrial/README.md](../Industrial/README.md) |")
idx.append("\n## Busca por tema\n\n| Tema | Também chamado de | Área | Normas |\n|---|---|---|---|")
for nome, area, _, sin in TEMAS:
    cods = [r["codigo"] for r in REC if nome in r["temas"]]
    if cods:
        idx.append(f"| **{nome}** | {sin} | [{area}]({slug(area)}.md) | {', '.join(cods)} |")
idx.append("\n## Busca por demonstração afetada\n\nNormas contábeis brasileiras que mudam cada demonstração.\n\n"
           "| Demonstração | Normas |\n|---|---|")
for sig, nome in DEMOS:
    cods = [r["codigo"] for r in REC if r["serie"] != "IFRS/IAS" and re.search(rf"\b{sig}\b", r["afeta"])]
    idx.append(f"| **{sig}** – {nome} | {', '.join(cods)} |")
(pasta / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

i = out.index(next(x for x in out if x.startswith("## NBC TG – Normas técnicas gerais")))
out.insert(i, "## Encontrar por área\n\n"
           "Índice completo, busca por tema e por demonstração: **[areas/README.md](areas/README.md)**. "
           "Mapa interativo: **[graph.html](https://ygordesouzagaspar-eng.github.io/normas-contabeis-brasil/graphify-out/graph.html)**. "
           "Dados: **[normas.json](normas.json)**. Instruções para IA (Copilot, Claude etc.): **[AGENTS.md](AGENTS.md)**.\n\n"
           "**Empresa industrial?** Os trechos das normas para a indústria (custo de produção, estoques, máquinas, vendas, incentivos, meio ambiente) "
           "estão em **[Industrial/](Industrial/README.md)**.\n\n"
           "| Área | Use para | Normas |\n|---|---|---|\n" +
           "\n".join(f"| [{a}](areas/{slug(a)}.md) | {QUANDO.get(a, '')} | {len(por_area[a])} |" for a in ordem) + "\n")
(ROOT / "README.md").write_text("\n".join(out), encoding="utf-8")

# instruções para IA: mesmo texto para Copilot, Claude e outros agentes
ag = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
(ROOT / "CLAUDE.md").write_text(ag, encoding="utf-8")
(ROOT / ".github").mkdir(exist_ok=True)
(ROOT / ".github" / "copilot-instructions.md").write_text(ag, encoding="utf-8")

# ---------- extração para o graphify (determinística, sem LLM) ----------
SRC = "normas.json"
def nid(prefix, s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return prefix + "_" + re.sub(r"[^a-z0-9]+", "_", s).strip("_")
nodes, edges, seen = [], [], set()
def node(i, label, kind):
    if i not in seen:
        seen.add(i)
        nodes.append({"id": i, "label": label, "file_type": "concept" if kind != "norma" else "document",
                      "source_file": SRC, "source_location": None, "source_url": None, "captured_at": None,
                      "author": None, "contributor": None, "kind": kind})
    return i
def edge(a, b, rel, conf="EXTRACTED", score=1.0):
    edges.append({"source": a, "target": b, "relation": rel, "confidence": conf,
                  "confidence_score": score, "source_file": SRC, "source_location": None, "weight": 1.0})
def code_id(c):
    return nid("norma", re.sub(r"\s*\(R\d+\)", "", c))
for a in ordem:
    node(nid("area", a), f"Área: {a}", "area")
for nome, area, _, sin in TEMAS:
    t = node(nid("tema", nome), f"{nome} ({sin})", "tema")
    edge(t, node(nid("area", area), f"Área: {area}", "area"), "parte_da_area")
for r in REC:
    n = node(code_id(r["codigo"]), f"{r['codigo']} – {r['titulo']}", "norma")
    for a in r["areas"]:
        edge(n, nid("area", a), "pertence_a_area")
    for t in r["temas"]:
        edge(n, nid("tema", t), "trata_de")
    for ref in (r["cpc"], r["internacional"]):
        if ref:
            edge(n, node(code_id(ref), ref, "norma"), "equivale_a")
    if r["serie"] != "IFRS/IAS":
        for sig, nome in DEMOS:
            if re.search(rf"\b{sig}\b", r["afeta"]):
                edge(n, node(nid("demo", sig), f"Demonstração: {sig} ({nome})", "demonstracao"), "afeta")
setor = node("setor_industria", "Setor: Indústria (fábrica, produção, custo industrial)", "setor")
for arq, titulo in TOPICOS_IND:
    t = node(nid("industria", titulo), f"Indústria: {titulo}", "topico_industrial")
    edge(t, setor, "parte_do_setor")
for r in REC:
    for tp in {x["topico"] for x in r["industria"]}:
        edge(code_id(r["codigo"]), nid("industria", tp), "aplica_na_industria")
(ROOT / "graphify-out").mkdir(exist_ok=True)
(ROOT / "graphify-out" / ".graphify_extract.json").write_text(json.dumps(
    {"nodes": nodes, "edges": edges, "hyperedges": [], "input_tokens": 0, "output_tokens": 0}, ensure_ascii=False), encoding="utf-8")
print(f"{len(REC)} normas, {len(TEMAS)} temas, {len(ordem)} áreas; grafo: {len(nodes)} nós, {len(edges)} arestas")
sem = [r["codigo"] for r in REC if not r["temas"]]
print("sem tema:", sem)
