# Teste de busca

Gerado por `scripts/testar_busca.py`: para cada pergunta de `testes/perguntas.json`, uma busca por palavras-chave (BM25) ranqueia os arquivos do repositório. Passa quando um arquivo esperado aparece entre os 3 primeiros e cita as normas esperadas.

**Acerto: 40/40 (100%)**

| | Pergunta | 3 primeiros arquivos | Arquivo esperado encontrado |
|---|---|---|---|
| ✅ | Como depreciar uma máquina da fábrica? | Industrial/02-maquinas-e-fabrica.md, lancamentos/imobilizado-e-arrendamentos.md, Industrial/README.md | Industrial/02-maquinas-e-fabrica.md |
| ✅ | A ociosidade da fábrica entra no custo do produto? | Industrial/01-estoques-e-custo-de-producao.md, lancamentos/estoques-e-custos.md, Industrial/02-maquinas-e-fabrica.md | Industrial/01-estoques-e-custo-de-producao.md |
| ✅ | Aluguel de loja em shopping com aluguel percentual sobre vendas | Varejo/04-lojas-e-arrendamentos.md, Varejo/README.md, Varejo/02-vendas-e-receita.md | Varejo/04-lojas-e-arrendamentos.md |
| ✅ | No marketplace a receita é o valor total ou só a comissão? | Varejo/02-vendas-e-receita.md, Varejo/README.md, lancamentos/receitas.md | Varejo/02-vendas-e-receita.md |
| ✅ | Vale-presente não utilizado vira receita? | Varejo/02-vendas-e-receita.md, Varejo/README.md, areas/auditoria-independente.md | Varejo/02-vendas-e-receita.md |
| ✅ | Antecipação de recebíveis de cartão baixa o contas a receber? | Varejo/03-cartoes-e-recebiveis.md, Varejo/README.md, Financeiro/03-instrumentos-financeiros-fora-do-sistema-financeiro.md | Varejo/03-cartoes-e-recebiveis.md |
| ✅ | Quando reconhecer a receita de assinatura SaaS? | Servicos/README.md, Servicos/02-saas-software-e-licencas.md, Construcao/01-incorporacao-imobiliaria.md | Servicos/README.md |
| ✅ | Comissão de vendas paga ao vendedor pode virar ativo? | lancamentos/receitas.md, Servicos/02-saas-software-e-licencas.md, Servicos/README.md | Servicos/02-saas-software-e-licencas.md |
| ✅ | Provisão mensal de férias e 13º salário | lancamentos/pessoal-e-provisoes.md, Servicos/03-pessoal-e-beneficios.md, Servicos/README.md | lancamentos/pessoal-e-provisoes.md |
| ✅ | Gado em engorda fica a custo ou valor justo? | Agronegocio/01-ativo-biologico-e-colheita.md, Agronegocio/README.md, lancamentos/agro.md | Agronegocio/01-ativo-biologico-e-colheita.md |
| ✅ | Pé de café é ativo biológico ou imobilizado? | Agronegocio/README.md, areas/ativos.md, Agronegocio/02-terras-plantas-portadoras-e-arrendamentos.md | Agronegocio/README.md |
| ✅ | Juros do crédito rural do Plano Safra abaixo do mercado | Agronegocio/03-credito-rural-hedge-e-cpr.md, Agronegocio/README.md, GLOSSARIO.md | Agronegocio/03-credito-rural-hedge-e-cpr.md |
| ✅ | Incorporadora reconhece receita na venda na planta ou na entrega das chaves? | Construcao/README.md, Construcao/01-incorporacao-imobiliaria.md, Industrial/03-vendas-e-pos-venda.md | Construcao/README.md |
| ✅ | Permuta de terreno por apartamentos a construir | Construcao/01-incorporacao-imobiliaria.md, Construcao/README.md, Construcao/02-contratos-de-construcao.md | Construcao/01-incorporacao-imobiliaria.md |
| ✅ | Contrato de obra com prejuízo previsto, contrato oneroso | Construcao/README.md, Construcao/02-contratos-de-construcao.md, Varejo/04-lojas-e-arrendamentos.md | Construcao/README.md |
| ✅ | ONG: doação recebida e trabalho voluntário | TerceiroSetor/README.md, TerceiroSetor/02-demonstracoes-e-patrimonio-social.md, TerceiroSetor/01-receitas-doacoes-e-subvencoes.md | TerceiroSetor/README.md |
| ✅ | Cooperativa: quotas-partes do cooperado que saiu | TerceiroSetor/03-cooperativas.md, TerceiroSetor/README.md, areas/setores-especificos.md | TerceiroSetor/03-cooperativas.md |
| ✅ | Prestação de contas de partido político nas eleições | areas/contabilidade-eleitoral.md, TerceiroSetor/04-partidos-e-eleicoes.md, TerceiroSetor/README.md | areas/contabilidade-eleitoral.md |
| ✅ | Banco: perda esperada pela Resolução CMN 4.966 | Financeiro/01-bancos-e-instituicoes-do-bc.md, Financeiro/README.md, lancamentos/instrumentos-financeiros-e-cambio.md | Financeiro/01-bancos-e-instituicoes-do-bc.md |
| ✅ | Seguradora aplica IFRS 17 ou regra da SUSEP? | Financeiro/README.md, Financeiro/02-seguradoras-e-previdencia.md, areas/setores-especificos.md | Financeiro/README.md |
| ✅ | O que muda com a IFRS 18 na DRE? | Industrial/07-dre-e-apresentacao.md, areas/setores-especificos.md, areas/apresentacao-e-divulgacao.md | Industrial/07-dre-e-apresentacao.md |
| ✅ | IBS e CBS em 2026: devo reconhecer o passivo no período de teste? | areas/reforma-tributaria.md, areas/tributos.md, lancamentos/tributos-e-subvencoes.md | areas/reforma-tributaria.md |
| ✅ | Lançamento contábil do split payment | lancamentos/tributos-e-subvencoes.md, lancamentos/README.md, areas/reforma-tributaria.md | lancamentos/tributos-e-subvencoes.md |
| ✅ | O que significa VRL? | GLOSSARIO.md, Industrial/01-estoques-e-custo-de-producao.md, Varejo/01-mercadorias-e-cmv.md | GLOSSARIO.md |
| ✅ | O que é MPM medida de desempenho? | Industrial/07-dre-e-apresentacao.md, Servicos/01-receita-de-servicos.md, GLOSSARIO.md | Industrial/07-dre-e-apresentacao.md |
| ✅ | Lançamento da provisão para garantia de produtos | lancamentos/receitas.md, lancamentos/README.md, Industrial/03-vendas-e-pos-venda.md | lancamentos/receitas.md |
| ✅ | Lançamento do direito de uso e passivo de arrendamento | lancamentos/imobilizado-e-arrendamentos.md, Varejo/04-lojas-e-arrendamentos.md, lancamentos/receitas.md | lancamentos/imobilizado-e-arrendamentos.md |
| ✅ | Quando o auditor emite opinião com ressalva? | GLOSSARIO.md, areas/auditoria-independente.md, areas/README.md | GLOSSARIO.md |
| ✅ | Prefeitura: como registrar o imobilizado de uma escola? | areas/setor-publico.md, areas/ativos.md, Construcao/01-incorporacao-imobiliaria.md | areas/setor-publico.md |
| ✅ | Teste de impairment do ágio goodwill | areas/ativos.md, areas/participacoes-societarias.md, GLOSSARIO.md | areas/ativos.md |
| ✅ | Imposto de renda diferido sobre prejuízo fiscal | areas/tributos.md, Industrial/04-tributos-e-incentivos.md, areas/reforma-tributaria.md | areas/tributos.md |
| ✅ | Microempresa deve usar qual norma contábil? | Servicos/04-escritorios-tributos-e-pequenas.md, areas/pequenas-e-medias-empresas.md, Servicos/README.md | Servicos/04-escritorios-tributos-e-pequenas.md |
| ✅ | Contabilização de créditos de carbono e CBIO | Agronegocio/04-usinas-carbono-e-auditoria.md, areas/sustentabilidade.md, Industrial/08-meio-ambiente-e-clima.md | Agronegocio/04-usinas-carbono-e-auditoria.md |
| ✅ | Perícia contábil: laudo de apuração de haveres | areas/pericia-contabil.md, areas/README.md, areas/fundamentos.md | areas/pericia-contabil.md |
| ✅ | Código de ética profissional do contador | areas/etica-e-exercicio-profissional.md, areas/README.md, GLOSSARIO.md | areas/etica-e-exercicio-profissional.md |
| ✅ | Hedge de preço de commodities agrícolas | Agronegocio/03-credito-rural-hedge-e-cpr.md, Agronegocio/02-terras-plantas-portadoras-e-arrendamentos.md, Industrial/06-commodities-cambio-e-hedge.md | Agronegocio/03-credito-rural-hedge-e-cpr.md |
| ✅ | Incentivo fiscal de ICMS crédito presumido e reserva de incentivos fiscais | lancamentos/tributos-e-subvencoes.md, Industrial/04-tributos-e-incentivos.md, lancamentos/README.md | lancamentos/tributos-e-subvencoes.md |
| ✅ | Variação cambial de fornecedor estrangeiro na importação | Industrial/06-commodities-cambio-e-hedge.md, lancamentos/instrumentos-financeiros-e-cambio.md, areas/moeda-e-cambio.md | Industrial/06-commodities-cambio-e-hedge.md |
| ✅ | Auditor acompanha o inventário físico dos estoques | Industrial/10-auditoria-na-industria.md, Varejo/01-mercadorias-e-cmv.md, Industrial/08-meio-ambiente-e-clima.md | Industrial/10-auditoria-na-industria.md |
| ✅ | Consolidação de controladas e equivalência patrimonial | areas/participacoes-societarias.md, areas/normas-internacionais.md, areas/setor-publico.md | areas/participacoes-societarias.md |
