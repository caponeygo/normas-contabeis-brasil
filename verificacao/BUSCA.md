# Teste de busca

Gerado por `scripts/testar_busca.py`: para cada pergunta de `testes/perguntas.json`, uma busca por palavras-chave (BM25) ranqueia os arquivos do repositório. Passa quando um arquivo esperado aparece entre os 3 primeiros e cita as normas esperadas.

**Acerto: 43/43 (100%)**

| | Pergunta | 3 primeiros arquivos | Arquivo esperado encontrado |
|---|---|---|---|
| ✅ | Como depreciar uma máquina da fábrica? | setores/Industrial/02-maquinas-e-fabrica.md, lancamentos/imobilizado-e-arrendamentos.md, setores/Industrial/README.md | setores/Industrial/02-maquinas-e-fabrica.md |
| ✅ | A ociosidade da fábrica entra no custo do produto? | setores/Industrial/01-estoques-e-custo-de-producao.md, lancamentos/estoques-e-custos.md, setores/Industrial/02-maquinas-e-fabrica.md | setores/Industrial/01-estoques-e-custo-de-producao.md |
| ✅ | Aluguel de loja em shopping com aluguel percentual sobre vendas | setores/Varejo/04-lojas-e-arrendamentos.md, setores/Varejo/README.md, lancamentos/imobilizado-e-arrendamentos.md | setores/Varejo/04-lojas-e-arrendamentos.md |
| ✅ | No marketplace a receita é o valor total ou só a comissão? | setores/Varejo/02-vendas-e-receita.md, setores/Varejo/README.md, lancamentos/receitas.md | setores/Varejo/02-vendas-e-receita.md |
| ✅ | Vale-presente não utilizado vira receita? | setores/Varejo/02-vendas-e-receita.md, setores/Varejo/README.md, lancamentos/receitas.md | setores/Varejo/02-vendas-e-receita.md |
| ✅ | Antecipação de recebíveis de cartão baixa o contas a receber? | setores/Varejo/03-cartoes-e-recebiveis.md, setores/Varejo/README.md, lancamentos/README.md | setores/Varejo/03-cartoes-e-recebiveis.md |
| ✅ | Quando reconhecer a receita de assinatura SaaS? | setores/Servicos/README.md, setores/Servicos/02-saas-software-e-licencas.md, setores/Construcao/01-incorporacao-imobiliaria.md | setores/Servicos/README.md |
| ✅ | Comissão de vendas paga ao vendedor pode virar ativo? | lancamentos/receitas.md, setores/Servicos/02-saas-software-e-licencas.md, setores/Servicos/README.md | setores/Servicos/02-saas-software-e-licencas.md |
| ✅ | Provisão mensal de férias e 13º salário | lancamentos/pessoal-e-provisoes.md, setores/Servicos/03-pessoal-e-beneficios.md, setores/Servicos/README.md | lancamentos/pessoal-e-provisoes.md |
| ✅ | Gado em engorda fica a custo ou valor justo? | setores/Agronegocio/01-ativo-biologico-e-colheita.md, setores/Agronegocio/README.md, lancamentos/agro.md | setores/Agronegocio/01-ativo-biologico-e-colheita.md |
| ✅ | Pé de café é ativo biológico ou imobilizado? | setores/Agronegocio/README.md, areas/ativos.md, setores/Agronegocio/02-terras-plantas-portadoras-e-arrendamentos.md | setores/Agronegocio/README.md |
| ✅ | Juros do crédito rural do Plano Safra abaixo do mercado | setores/Agronegocio/03-credito-rural-hedge-e-cpr.md, setores/Agronegocio/README.md, lancamentos/bancos.md | setores/Agronegocio/03-credito-rural-hedge-e-cpr.md |
| ✅ | Incorporadora reconhece receita na venda na planta ou na entrega das chaves? | setores/Construcao/README.md, setores/Construcao/01-incorporacao-imobiliaria.md, setores/Industrial/03-vendas-e-pos-venda.md | setores/Construcao/README.md |
| ✅ | Permuta de terreno por apartamentos a construir | setores/Construcao/01-incorporacao-imobiliaria.md, setores/Construcao/README.md, setores/Construcao/02-contratos-de-construcao.md | setores/Construcao/01-incorporacao-imobiliaria.md |
| ✅ | Contrato de obra com prejuízo previsto, contrato oneroso | setores/Construcao/README.md, setores/Construcao/02-contratos-de-construcao.md, setores/Varejo/04-lojas-e-arrendamentos.md | setores/Construcao/README.md |
| ✅ | ONG: doação recebida e trabalho voluntário | setores/TerceiroSetor/README.md, setores/TerceiroSetor/02-demonstracoes-e-patrimonio-social.md, setores/TerceiroSetor/01-receitas-doacoes-e-subvencoes.md | setores/TerceiroSetor/README.md |
| ✅ | Cooperativa: quotas-partes do cooperado que saiu | setores/TerceiroSetor/03-cooperativas.md, setores/TerceiroSetor/README.md, areas/setores-especificos.md | setores/TerceiroSetor/03-cooperativas.md |
| ✅ | Prestação de contas de partido político nas eleições | areas/contabilidade-eleitoral.md, setores/TerceiroSetor/04-partidos-e-eleicoes.md, setores/TerceiroSetor/README.md | areas/contabilidade-eleitoral.md |
| ✅ | Banco: perda esperada pela Resolução CMN 4.966 | setores/Financeiro/README.md, setores/Financeiro/02-perda-esperada-e-ativo-problematico.md, lancamentos/bancos.md | setores/Financeiro/README.md |
| ✅ | Seguradora aplica IFRS 17 ou regra da SUSEP? | setores/Financeiro/README.md, setores/Financeiro/05-seguradoras-e-previdencia.md, areas/setores-especificos.md | setores/Financeiro/README.md |
| ✅ | O que muda com a IFRS 18 na DRE? | setores/Industrial/07-dre-e-apresentacao.md, areas/setores-especificos.md, areas/apresentacao-e-divulgacao.md | setores/Industrial/07-dre-e-apresentacao.md |
| ✅ | IBS e CBS em 2026: devo reconhecer o passivo no período de teste? | areas/reforma-tributaria.md, areas/tributos.md, lancamentos/tributos-e-subvencoes.md | areas/reforma-tributaria.md |
| ✅ | Lançamento contábil do split payment | lancamentos/tributos-e-subvencoes.md, lancamentos/README.md, areas/reforma-tributaria.md | lancamentos/tributos-e-subvencoes.md |
| ✅ | O que significa VRL? | GLOSSARIO.md, setores/Industrial/01-estoques-e-custo-de-producao.md, setores/Varejo/01-mercadorias-e-cmv.md | GLOSSARIO.md |
| ✅ | O que é MPM medida de desempenho? | setores/Industrial/07-dre-e-apresentacao.md, setores/Servicos/01-receita-de-servicos.md, GLOSSARIO.md | setores/Industrial/07-dre-e-apresentacao.md |
| ✅ | Lançamento da provisão para garantia de produtos | lancamentos/receitas.md, lancamentos/README.md, setores/Industrial/03-vendas-e-pos-venda.md | lancamentos/receitas.md |
| ✅ | Lançamento do direito de uso e passivo de arrendamento | lancamentos/imobilizado-e-arrendamentos.md, setores/Varejo/04-lojas-e-arrendamentos.md, lancamentos/receitas.md | lancamentos/imobilizado-e-arrendamentos.md |
| ✅ | Quando o auditor emite opinião com ressalva? | GLOSSARIO.md, areas/auditoria-independente.md, normas/nbc-ta-auditoria-independente.md | GLOSSARIO.md |
| ✅ | Prefeitura: como registrar o imobilizado de uma escola? | areas/setor-publico.md, areas/ativos.md, setores/Construcao/01-incorporacao-imobiliaria.md | areas/setor-publico.md |
| ✅ | Teste de impairment do ágio goodwill | areas/ativos.md, areas/participacoes-societarias.md, GLOSSARIO.md | areas/ativos.md |
| ✅ | Imposto de renda diferido sobre prejuízo fiscal | areas/tributos.md, setores/Industrial/04-tributos-e-incentivos.md, areas/reforma-tributaria.md | areas/tributos.md |
| ✅ | Microempresa deve usar qual norma contábil? | setores/Servicos/04-escritorios-tributos-e-pequenas.md, areas/pequenas-e-medias-empresas.md, normas/nbc-tg-pequenas-e-medias-empresas-e-microentidades.md | setores/Servicos/04-escritorios-tributos-e-pequenas.md |
| ✅ | Contabilização de créditos de carbono e CBIO | setores/Agronegocio/04-usinas-carbono-e-auditoria.md, areas/sustentabilidade.md, setores/Industrial/08-meio-ambiente-e-clima.md | setores/Agronegocio/04-usinas-carbono-e-auditoria.md |
| ✅ | Perícia contábil: laudo de apuração de haveres | areas/pericia-contabil.md, normas/nbc-tp-pericia.md, areas/README.md | areas/pericia-contabil.md |
| ✅ | Código de ética profissional do contador | areas/etica-e-exercicio-profissional.md, normas/nbc-pg-profissionais-gerais-etica.md, normas/README.md | areas/etica-e-exercicio-profissional.md |
| ✅ | Hedge de preço de commodities agrícolas | setores/Agronegocio/03-credito-rural-hedge-e-cpr.md, setores/Agronegocio/02-terras-plantas-portadoras-e-arrendamentos.md, setores/Industrial/06-commodities-cambio-e-hedge.md | setores/Agronegocio/03-credito-rural-hedge-e-cpr.md |
| ✅ | Incentivo fiscal de ICMS crédito presumido e reserva de incentivos fiscais | lancamentos/tributos-e-subvencoes.md, setores/Industrial/04-tributos-e-incentivos.md, lancamentos/README.md | lancamentos/tributos-e-subvencoes.md |
| ✅ | Variação cambial de fornecedor estrangeiro na importação | setores/Industrial/06-commodities-cambio-e-hedge.md, lancamentos/instrumentos-financeiros-e-cambio.md, areas/moeda-e-cambio.md | setores/Industrial/06-commodities-cambio-e-hedge.md |
| ✅ | Auditor acompanha o inventário físico dos estoques | setores/Industrial/10-auditoria-na-industria.md, setores/Varejo/01-mercadorias-e-cmv.md, setores/Industrial/08-meio-ambiente-e-clima.md | setores/Industrial/10-auditoria-na-industria.md |
| ✅ | Consolidação de controladas e equivalência patrimonial | areas/participacoes-societarias.md, areas/normas-internacionais.md, normas/itg-ctg-otg-interpretacoes-e-comunicados.md | areas/participacoes-societarias.md |
| ✅ | Quando um crédito de banco vira ativo problemático e para de reconhecer juros? | lancamentos/bancos.md, setores/Financeiro/02-perda-esperada-e-ativo-problematico.md, setores/Financeiro/README.md | lancamentos/bancos.md |
| ✅ | Banco: renegociação ou reestruturação de operação de crédito | setores/Financeiro/03-renegociacao-reestruturacao-e-baixa.md, lancamentos/bancos.md, setores/Financeiro/README.md | setores/Financeiro/03-renegociacao-reestruturacao-e-baixa.md |
| ✅ | Lançamento de baixa a prejuízo em banco | lancamentos/bancos.md, lancamentos/README.md, setores/Financeiro/02-perda-esperada-e-ativo-problematico.md | lancamentos/bancos.md |
