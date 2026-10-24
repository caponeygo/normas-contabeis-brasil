# Teste de busca

Gerado por `scripts/testar_busca.py`: para cada pergunta de `testes/perguntas.json`, uma busca por palavras-chave (BM25) ranqueia os arquivos do repositório. Passa quando um arquivo esperado aparece entre os 3 primeiros e cita as normas esperadas.

**Acerto: 83/85 (98%)**

| | Pergunta | 3 primeiros arquivos | Arquivo esperado encontrado |
|---|---|---|---|
| ✅ | Como depreciar uma máquina da fábrica? | normas/ficha/nbc-tg-27-r4.md, setores/industrial/02-maquinas-e-fabrica.md, normas/ficha/itg-12.md | normas/ficha/nbc-tg-27-r4.md |
| ✅ | A ociosidade da fábrica entra no custo do produto? | setores/industrial/01-estoques-e-custo-de-producao.md, lancamentos/estoques-e-custos.md, setores/industrial/02-maquinas-e-fabrica.md | setores/industrial/01-estoques-e-custo-de-producao.md |
| ✅ | Aluguel de loja em shopping com aluguel percentual sobre vendas | setores/varejo/04-lojas-e-arrendamentos.md, setores/varejo/README.md, normas/ficha/nbc-tg-06-r3.md | setores/varejo/04-lojas-e-arrendamentos.md |
| ✅ | No marketplace a receita é o valor total ou só a comissão? | setores/varejo/02-vendas-e-receita.md, lancamentos/receitas.md, setores/varejo/README.md | setores/varejo/02-vendas-e-receita.md |
| ✅ | Vale-presente não utilizado vira receita? | setores/varejo/02-vendas-e-receita.md, setores/varejo/README.md, normas/ficha/nbc-tg-12-r1.md | setores/varejo/02-vendas-e-receita.md |
| ✅ | Antecipação de recebíveis de cartão baixa o contas a receber? | setores/varejo/03-cartoes-e-recebiveis.md, setores/varejo/README.md, lancamentos/README.md | setores/varejo/03-cartoes-e-recebiveis.md |
| ✅ | Quando reconhecer a receita de assinatura SaaS? | setores/servicos/02-saas-software-e-licencas.md, setores/servicos/README.md, normas/ficha/nbc-tg-47.md | setores/servicos/02-saas-software-e-licencas.md |
| ✅ | Comissão de vendas paga ao vendedor pode virar ativo? | lancamentos/receitas.md, setores/servicos/02-saas-software-e-licencas.md, setores/varejo/02-vendas-e-receita.md | setores/servicos/02-saas-software-e-licencas.md |
| ✅ | Provisão mensal de férias e 13º salário | lancamentos/pessoal-e-provisoes.md, setores/servicos/03-pessoal-e-beneficios.md, setores/servicos/README.md | lancamentos/pessoal-e-provisoes.md |
| ✅ | Gado em engorda fica a custo ou valor justo? | setores/agronegocio/01-ativo-biologico-e-colheita.md, lancamentos/agro.md, setores/agronegocio/README.md | setores/agronegocio/01-ativo-biologico-e-colheita.md |
| ✅ | Pé de café é ativo biológico ou imobilizado? | normas/ficha/ias-41.md, normas/ficha/nbc-tg-29-r2.md, setores/agronegocio/README.md | normas/ficha/ias-41.md |
| ✅ | Juros do crédito rural do Plano Safra abaixo do mercado | setores/agronegocio/03-credito-rural-hedge-e-cpr.md, setores/agronegocio/README.md, normas/ficha/nbc-tg-40-r3.md | setores/agronegocio/03-credito-rural-hedge-e-cpr.md |
| ✅ | Incorporadora reconhece receita na venda na planta ou na entrega das chaves? | setores/construcao/README.md, normas/ficha/nbc-tg-47.md, normas/ficha/ctg-01.md | setores/construcao/README.md |
| ✅ | Permuta de terreno por apartamentos a construir | setores/construcao/01-incorporacao-imobiliaria.md, setores/construcao/README.md, setores/construcao/02-contratos-de-construcao.md | setores/construcao/01-incorporacao-imobiliaria.md |
| ✅ | Contrato de obra com prejuízo previsto, contrato oneroso | setores/construcao/README.md, setores/construcao/02-contratos-de-construcao.md, setores/construcao/01-incorporacao-imobiliaria.md | setores/construcao/README.md |
| ✅ | ONG: doação recebida e trabalho voluntário | setores/terceiro-setor/README.md, setores/terceiro-setor/01-receitas-doacoes-e-subvencoes.md, setores/terceiro-setor/02-demonstracoes-e-patrimonio-social.md | setores/terceiro-setor/README.md |
| ✅ | Cooperativa: quotas-partes do cooperado que saiu | setores/terceiro-setor/03-cooperativas.md, setores/terceiro-setor/README.md, normas/ficha/itg-2004.md | setores/terceiro-setor/03-cooperativas.md |
| ✅ | Prestação de contas de partido político nas eleições | areas/contabilidade-eleitoral.md, normas/ficha/nbc-tpe-01.md, setores/terceiro-setor/04-partidos-e-eleicoes.md | areas/contabilidade-eleitoral.md |
| ✅ | Banco: perda esperada pela Resolução CMN 4.966 | setores/financeiro/README.md, lancamentos/bancos.md, setores/financeiro/02-perda-esperada-e-ativo-problematico.md | setores/financeiro/README.md |
| ✅ | Seguradora aplica IFRS 17 ou regra da SUSEP? | setores/financeiro/05-seguradoras-e-previdencia.md, setores/financeiro/README.md, normas/ficha/nbc-tg-50.md | setores/financeiro/05-seguradoras-e-previdencia.md |
| ✅ | O que muda com a IFRS 18 na DRE? | normas/ficha/ifrs-18.md, normas/ficha/nbc-tg-51.md, setores/industrial/07-dre-e-apresentacao.md | normas/ficha/ifrs-18.md |
| ✅ | IBS e CBS em 2026: devo reconhecer o passivo no período de teste? | normas/ficha/ot-cfc-01-2026.md, areas/reforma-tributaria.md, areas/tributos.md | normas/ficha/ot-cfc-01-2026.md |
| ✅ | Lançamento contábil do split payment | lancamentos/README.md, lancamentos/tributos-e-subvencoes.md, areas/reforma-tributaria.md | lancamentos/tributos-e-subvencoes.md |
| ✅ | O que significa VRL? | setores/varejo/01-mercadorias-e-cmv.md, setores/industrial/01-estoques-e-custo-de-producao.md, lancamentos/estoques-e-custos.md | setores/varejo/01-mercadorias-e-cmv.md |
| ✅ | O que é MPM medida de desempenho? | setores/servicos/01-receita-de-servicos.md, normas/ficha/ifrs-18.md, normas/ficha/nbc-tg-51.md | normas/ficha/ifrs-18.md |
| ✅ | Lançamento da provisão para garantia de produtos | lancamentos/receitas.md, setores/industrial/03-vendas-e-pos-venda.md, lancamentos/README.md | lancamentos/receitas.md |
| ✅ | Lançamento do direito de uso e passivo de arrendamento | lancamentos/imobilizado-e-arrendamentos.md, setores/varejo/04-lojas-e-arrendamentos.md, normas/ficha/ifrs-16.md | lancamentos/imobilizado-e-arrendamentos.md |
| ✅ | Quando o auditor emite opinião com ressalva? | normas/ficha/nbc-ta-705.md, normas/ficha/pcaob-as-3105.md, normas/ficha/pcaob-as-3101.md | normas/ficha/nbc-ta-705.md |
| ❌ | Prefeitura: como registrar o imobilizado de uma escola? | normas/ficha/nbc-tsp-09-r1.md, setores/construcao/01-incorporacao-imobiliaria.md, normas/ficha/ctg-01.md | — |
| ✅ | Teste de impairment do ágio goodwill | normas/ficha/ias-36.md, normas/ficha/nbc-tg-01-r4.md, normas/ficha/ifrs-3.md | normas/ficha/ias-36.md |
| ✅ | Imposto de renda diferido sobre prejuízo fiscal | normas/ficha/ias-12.md, normas/ficha/nbc-tg-32-r4.md, areas/tributos.md | normas/ficha/ias-12.md |
| ✅ | Microempresa deve usar qual norma contábil? | normas/nbc-tg-pequenas-e-medias-empresas-e-microentidades.md, setores/servicos/04-escritorios-tributos-e-pequenas.md, areas/pequenas-e-medias-empresas.md | setores/servicos/04-escritorios-tributos-e-pequenas.md |
| ✅ | Contabilização de créditos de carbono e CBIO | normas/ficha/ctg-10.md, setores/agronegocio/04-usinas-carbono-e-auditoria.md, areas/sustentabilidade.md | normas/ficha/ctg-10.md |
| ✅ | Perícia contábil: laudo de apuração de haveres | areas/pericia-contabil.md, normas/ficha/itp-01.md, normas/nbc-tp-pericia.md | areas/pericia-contabil.md |
| ✅ | Código de ética profissional do contador | normas/ficha/nbc-pg-01.md, normas/ficha/nbc-pg-200-r1.md, normas/ficha/nbc-pg-300-r1.md | normas/ficha/nbc-pg-01.md |
| ✅ | Hedge de preço de commodities agrícolas | setores/agronegocio/03-credito-rural-hedge-e-cpr.md, normas/ficha/nbc-tg-48.md, normas/ficha/nbc-tg-02-r3.md | setores/agronegocio/03-credito-rural-hedge-e-cpr.md |
| ✅ | Incentivo fiscal de ICMS crédito presumido e reserva de incentivos fiscais | lancamentos/tributos-e-subvencoes.md, setores/industrial/04-tributos-e-incentivos.md, normas/ficha/nbc-tg-07-r2.md | lancamentos/tributos-e-subvencoes.md |
| ✅ | Variação cambial de fornecedor estrangeiro na importação | lancamentos/instrumentos-financeiros-e-cambio.md, setores/industrial/06-commodities-cambio-e-hedge.md, normas/ficha/ias-21.md | lancamentos/instrumentos-financeiros-e-cambio.md |
| ✅ | Auditor acompanha o inventário físico dos estoques | setores/industrial/10-auditoria-na-industria.md, setores/varejo/01-mercadorias-e-cmv.md, normas/ficha/pcaob-as-2510.md | setores/industrial/10-auditoria-na-industria.md |
| ✅ | Consolidação de controladas e equivalência patrimonial | normas/ficha/itg-09-r2.md, areas/participacoes-societarias.md, normas/ficha/ias-28.md | areas/participacoes-societarias.md |
| ✅ | Quando um crédito de banco vira ativo problemático e para de reconhecer juros? | lancamentos/bancos.md, setores/financeiro/02-perda-esperada-e-ativo-problematico.md, setores/financeiro/README.md | lancamentos/bancos.md |
| ✅ | Banco: renegociação ou reestruturação de operação de crédito | setores/financeiro/03-renegociacao-reestruturacao-e-baixa.md, lancamentos/bancos.md, setores/financeiro/README.md | setores/financeiro/03-renegociacao-reestruturacao-e-baixa.md |
| ✅ | Lançamento de baixa a prejuízo em banco | lancamentos/bancos.md, lancamentos/README.md, setores/financeiro/02-perda-esperada-e-ativo-problematico.md | lancamentos/bancos.md |
| ✅ | A NBC TG 26 ainda vale ou foi substituída? | normas/ficha/pcaob-ei-1000.md, normas/ficha/nbc-tg-26-r5.md, normas/ficha/pcaob-qc-1000.md | normas/ficha/nbc-tg-26-r5.md |
| ✅ | Qual norma substitui a NBC TG 26 a partir de 2027? | normas/ficha/ias-1.md, normas/ficha/nbc-tg-26-r5.md, setores/industrial/07-dre-e-apresentacao.md | normas/ficha/nbc-tg-26-r5.md |
| ✅ | NBC TO 3410 gases de efeito estufa está em vigor? | normas/ficha/nbc-to-3410.md, areas/asseguracao.md, normas/nbc-to-asseguracao.md | normas/ficha/nbc-to-3410.md |
| ✅ | Qual a norma de arrendamento mercantil, o direito de uso? | lancamentos/imobilizado-e-arrendamentos.md, normas/ficha/nbc-tsp-35.md, normas/ficha/ifrs-16.md | lancamentos/imobilizado-e-arrendamentos.md |
| ❌ | Como contabilizar perda esperada de crédito em contas a receber? | setores/varejo/03-cartoes-e-recebiveis.md, lancamentos/bancos.md, lancamentos/README.md | — |
| ✅ | Quando o auditor emite opinião com ressalva? | normas/ficha/nbc-ta-705.md, normas/ficha/pcaob-as-3105.md, normas/ficha/pcaob-as-3101.md | normas/ficha/nbc-ta-705.md |
| ✅ | Qual norma trata de eventos subsequentes ao período? | normas/ficha/nbc-ta-560-r1.md, normas/ficha/nbc-tsp-25-r1.md, normas/ficha/ias-10.md | normas/ficha/ias-10.md |
| ✅ | Como tratar ativo biológico na colheita de cana? | normas/ficha/nbc-tg-29-r2.md, lancamentos/agro.md, setores/agronegocio/01-ativo-biologico-e-colheita.md | normas/ficha/nbc-tg-29-r2.md |
| ✅ | Plantas portadoras como laranjeiras e cafezais são imobilizado? | setores/agronegocio/02-terras-plantas-portadoras-e-arrendamentos.md, normas/ficha/nbc-tg-06-r3.md, setores/agronegocio/README.md | setores/agronegocio/02-terras-plantas-portadoras-e-arrendamentos.md |
| ✅ | CPR financeira e hedge de commodities no agro | normas/ficha/nbc-tg-48.md, normas/ficha/nbc-tg-40-r3.md, setores/agronegocio/03-credito-rural-hedge-e-cpr.md | normas/ficha/nbc-tg-48.md |
| ✅ | Venda de unidade na planta pela incorporadora, reconhecimento da receita | setores/construcao/01-incorporacao-imobiliaria.md, normas/ficha/ctg-01.md, setores/construcao/README.md | setores/construcao/01-incorporacao-imobiliaria.md |
| ✅ | Permuta de terreno por unidades da incorporação | setores/construcao/01-incorporacao-imobiliaria.md, setores/construcao/README.md, normas/ficha/ctg-01.md | setores/construcao/01-incorporacao-imobiliaria.md |
| ✅ | Contrato oneroso na construção, como provisionar? | setores/construcao/02-contratos-de-construcao.md, setores/construcao/README.md, normas/ficha/nbc-tg-25-r2.md | setores/construcao/02-contratos-de-construcao.md |
| ✅ | Doações com restrição em entidade sem fins lucrativos | normas/ficha/itg-2002-r1.md, setores/terceiro-setor/01-receitas-doacoes-e-subvencoes.md, setores/terceiro-setor/02-demonstracoes-e-patrimonio-social.md | normas/ficha/itg-2002-r1.md |
| ✅ | Cooperativa: ato cooperativo e sobras | setores/terceiro-setor/03-cooperativas.md, normas/ficha/itg-2004.md, setores/terceiro-setor/README.md | setores/terceiro-setor/03-cooperativas.md |
| ✅ | Prestação de contas de partido político | areas/contabilidade-eleitoral.md, normas/ficha/nbc-tpe-01.md, setores/terceiro-setor/04-partidos-e-eleicoes.md | areas/contabilidade-eleitoral.md |
| ✅ | Programa de fidelidade com pontos, como reconhecer a receita? | lancamentos/receitas.md, setores/varejo/02-vendas-e-receita.md, normas/ficha/nbc-tg-47.md | setores/varejo/02-vendas-e-receita.md |
| ✅ | CMV e perdas e quebras de estoque no varejo | normas/ficha/nbc-tg-16-r2.md, setores/varejo/01-mercadorias-e-cmv.md, normas/ficha/nbc-ta-501.md | normas/ficha/nbc-tg-16-r2.md |
| ✅ | ICMS-ST no varejo, substituição tributária | setores/varejo/05-tributos-no-varejo.md, setores/varejo/01-mercadorias-e-cmv.md, setores/varejo/README.md | setores/varejo/05-tributos-no-varejo.md |
| ✅ | SaaS: receita ao longo do tempo ou em um momento? | setores/servicos/02-saas-software-e-licencas.md, normas/ficha/nbc-tg-47.md, normas/ficha/ifrs-15.md | setores/servicos/02-saas-software-e-licencas.md |
| ✅ | Férias e 13º salário, provisão na folha | setores/servicos/03-pessoal-e-beneficios.md, lancamentos/pessoal-e-provisoes.md, setores/servicos/README.md | setores/servicos/03-pessoal-e-beneficios.md |
| ✅ | Stock options pagamento baseado em ações | normas/ficha/nbc-tg-10-r3.md, normas/ficha/ifrs-2.md, setores/servicos/03-pessoal-e-beneficios.md | normas/ficha/nbc-tg-10-r3.md |
| ✅ | Estágios de perda esperada na Resolução CMN 4.966 | lancamentos/bancos.md, setores/financeiro/02-perda-esperada-e-ativo-problematico.md, setores/financeiro/README.md | setores/financeiro/02-perda-esperada-e-ativo-problematico.md |
| ✅ | Seguradora, contrato de seguro e SUSEP | setores/financeiro/05-seguradoras-e-previdencia.md, setores/financeiro/README.md, normas/ficha/nbc-tg-50.md | setores/financeiro/05-seguradoras-e-previdencia.md |
| ✅ | Incentivos de ICMS na indústria são subvenção? | setores/industrial/04-tributos-e-incentivos.md, normas/ficha/nbc-tg-07-r2.md, lancamentos/tributos-e-subvencoes.md | setores/industrial/04-tributos-e-incentivos.md |
| ✅ | Gastos com pesquisa e desenvolvimento, capitalizar ou despesa? | setores/industrial/05-pesquisa-e-desenvolvimento.md, normas/ficha/nbc-tg-04-r4.md, normas/ficha/ias-38.md | setores/industrial/05-pesquisa-e-desenvolvimento.md |
| ✅ | Provisão de garantia de produto vendido | lancamentos/receitas.md, setores/industrial/03-vendas-e-pos-venda.md, setores/varejo/02-vendas-e-receita.md | setores/industrial/03-vendas-e-pos-venda.md |
| ✅ | Variação cambial e moeda funcional | normas/ficha/ias-21.md, normas/ficha/nbc-tg-02-r3.md, areas/moeda-e-cambio.md | normas/ficha/ias-21.md |
| ✅ | Equivalência patrimonial em coligada | normas/ficha/ias-28.md, normas/ficha/nbc-tg-18-r4.md, normas/ficha/nbc-tsp-18-r1.md | normas/ficha/ias-28.md |
| ✅ | Consolidação de demonstrações e controle | areas/participacoes-societarias.md, normas/ficha/ifrs-10.md, normas/ficha/nbc-tg-36-r3.md | areas/participacoes-societarias.md |
| ✅ | Imposto de renda diferido sobre prejuízo fiscal | normas/ficha/ias-12.md, normas/ficha/nbc-tg-32-r4.md, areas/tributos.md | normas/ficha/ias-12.md |
| ✅ | IBS e CBS da reforma tributária em 2026 | normas/ficha/ot-cfc-01-2026.md, lancamentos/tributos-e-subvencoes.md, areas/reforma-tributaria.md | normas/ficha/ot-cfc-01-2026.md |
| ✅ | Perícia judicial e laudo pericial | areas/pericia-contabil.md, normas/ficha/nbc-tp-01-r2.md, normas/ficha/itp-01.md | areas/pericia-contabil.md |
| ✅ | Contabilidade de prefeitura no setor público | areas/setor-publico.md, normas/ficha/nbc-tasp.md, normas/ficha/nbc-tsp-estrutura-conceitual-r1.md | areas/setor-publico.md |
| ✅ | Relatório de sustentabilidade IFRS S1 e S2 | areas/sustentabilidade.md, normas/nbc-tds-sustentabilidade.md, normas/ficha/nbc-tds-01.md | areas/sustentabilidade.md |
| ✅ | Pequena empresa usa qual norma contábil? | areas/pequenas-e-medias-empresas.md, normas/ficha/nbc-tg-1000-r1.md, normas/nbc-tg-pequenas-e-medias-empresas-e-microentidades.md | areas/pequenas-e-medias-empresas.md |
| ✅ | Revisão de informações trimestrais ITR | normas/ficha/ctr-01-r1.md, areas/revisao.md, normas/nbc-tr-revisao.md | areas/revisao.md |
| ✅ | Fraude na auditoria responsabilidade do auditor | normas/ficha/nbc-ta-240-r2.md, normas/ficha/pcaob-as-2401.md, areas/auditoria-independente.md | normas/ficha/nbc-ta-240-r2.md |
| ✅ | Qual padrão do PCAOB trata de fraude na auditoria? | normas/ficha/pcaob-as-2401.md, areas/auditoria-independente.md, normas/ficha/nbc-ta-240-r2.md | normas/ficha/pcaob-as-2401.md |
| ✅ | O que é a QC 1000 do PCAOB e quando começa a valer? | normas/ficha/pcaob-qc-1000.md, normas/ficha/pcaob-qc-30.md, normas/ficha/pcaob-qc-20.md | normas/ficha/pcaob-qc-1000.md |
| ✅ | PCAOB AS 2201 auditoria do controle interno sobre relatórios financeiros | normas/ficha/pcaob-as-2201.md, areas/padroes-pcaob-eua.md, areas/auditoria-independente.md | normas/ficha/pcaob-as-2201.md |
| ✅ | A AS 2901 do PCAOB vai mudar em dezembro de 2026? | normas/ficha/pcaob-as-2901-versao-ate-14-12-2026.md, normas/ficha/pcaob-as-2901-nova-a-partir-de-15-12-2026.md, areas/padroes-pcaob-eua.md | normas/ficha/pcaob-as-2901-versao-ate-14-12-2026.md |
