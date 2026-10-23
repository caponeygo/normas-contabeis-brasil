# Setor: Comércio e varejo. Formato: ver scripts/gerar_setores.py.
NOME = "Comércio e Varejo"
PASTA = "Comercio"
USE_PARA = ("estoque de mercadorias, CMV, perdas e quebras, vendas, marketplace, fidelidade, vale-presente, devoluções, "
            "cartões e antecipação de recebíveis, aluguel de lojas, ICMS-ST")
INTRO = ("Trechos das normas que importam para atacado, varejo, e-commerce e distribuidores: da compra da mercadoria "
         "até a venda no caixa ou no site, passando por loja alugada, cartões e tributos.")

TOPICOS = [
("01-mercadorias-e-cmv", "Mercadorias, CMV e perdas",
 "custo da mercadoria, frete, bonificação de fornecedor, ICMS-ST, PEPS/médio, método de varejo, obsolescência, quebras e furtos, inventário",
 "No comércio o estoque é o maior ativo circulante. A regra é a mesma da indústria, sem a parte de produção: custo de compra líquido de descontos e de tributos recuperáveis, avaliado pelo menor entre custo e valor realizável.",
 [
  ("NBC TG 16", "9", "Mercadoria fica pelo menor valor entre custo e valor realizável líquido (VRL)."),
  ("NBC TG 16", "11", "Custo de compra = preço + tributos não recuperáveis (ex.: ICMS-ST quando não há crédito) + frete, seguro e manuseio até o depósito. Descontos comerciais, abatimentos e bonificações recebidas de fornecedores reduzem o custo."),
  ("NBC TG 16", "16", "Armazenagem de mercadoria pronta, despesas administrativas e de venda (frete na entrega ao cliente, comissões) não entram no custo."),
  ("NBC TG 16", "21", "Método de varejo (preço de venda menos margem) é aceito por conveniência se o resultado se aproximar do custo; a margem usada deve considerar remarcações."),
  ("NBC TG 16", "25", "Fórmulas aceitas: PEPS ou custo médio ponderado; UEPS não."),
  ("NBC TG 16", "28–33", "Coleção passada, itens parados, avariados ou com preço de venda em queda: reduzir ao VRL, em geral item a item ou por grupo semelhante."),
  ("NBC TG 16", "34", "Na venda, o custo vira CMV. Perdas de estoque (quebras, furtos, vencimentos) e ajustes ao VRL são despesa do período em que ocorrem."),
  ("NBC TG 16", "36", "Divulgar política de custo, saldos, CMV, ajustes ao VRL e reversões."),
  ("NBC TA 501", "4–7", "Auditor acompanha a contagem física das lojas e centros de distribuição relevantes, inclusive quando o inventário é rotativo ou em outra data."),
 ],
 ["Bonificações e verbas de fornecedor tratadas como redução do custo (não como receita).",
  "ICMS-ST e outros tributos sem crédito incluídos no custo; os recuperáveis em tributos a recuperar.",
  "Provisão para perdas e obsolescência (coleção passada, vencidos).",
  "Inventário rotativo documentado e conciliado com o razão."]),

("02-vendas-e-receita", "Vendas, marketplace e fidelidade",
 "momento da venda, receita líquida, devoluções e trocas, marketplace (principal x agente), programas de pontos, vale-presente, garantia estendida, venda a prazo",
 "As regras de receita da NBC TG 47 que mais aparecem no varejo: quem é o vendedor de fato, o que fazer com pontos e vales não usados, e quanto reconhecer quando o cliente pode devolver.",
 [
  ("NBC TG 47", "47", "A receita exclui valores cobrados em nome de terceiros (ex.: tributos sobre a venda). A DRE brasileira parte da receita bruta e deduz os tributos sobre vendas para chegar à receita líquida."),
  ("NBC TG 47", "B34–B38", "Marketplace e intermediação: se a empresa não controla a mercadoria antes de ela chegar ao cliente, é agente e reconhece como receita só a comissão (receita líquida), não o valor total da venda."),
  ("NBC TG 47", "B20–B27", "Direito de devolução ou troca: reconhecer receita só pelo que se espera não voltar; passivo de reembolso e ativo pelo direito de recuperar a mercadoria."),
  ("NBC TG 47", "B39–B43", "Programa de pontos e cashback que dá direito material ao cliente: parte do preço vai para receita diferida e só vira receita quando os pontos são usados ou expiram."),
  ("NBC TG 47", "B44–B47", "Vale-presente e créditos pré-pagos: passivo no recebimento; a parte que se espera nunca ser usada (breakage) vira receita na proporção do uso dos demais, se não houver obrigação de repassar a terceiros."),
  ("NBC TG 47", "B28–B33", "Garantia estendida vendida no caixa é serviço separado; se a loja apenas intermedeia a garantia de uma seguradora, avaliar se é agente (receita = comissão)."),
  ("NBC TG 47", "60–65", "Venda parcelada com juros embutidos: separar o componente financeiro; avaliar junto com o AVP da NBC TG 12 (no Brasil não existe a dispensa de até 1 ano do item 63 da IFRS 15)."),
  ("NBC TG 12", "—", "Vendas e compras a prazo relevantes: ajuste a valor presente; os juros vão para o resultado financeiro."),
 ],
 ["Revisar contratos de marketplace: principal ou agente por categoria de produto.",
  "Provisão para devoluções baseada em histórico por canal (loja física, site).",
  "Receita diferida de pontos e vales-presente, com estimativa de breakage documentada.",
  "Separar juros de vendas parceladas sem juros aparentes."]),

("03-cartoes-e-recebiveis", "Cartões, recebíveis e antecipação",
 "contas a receber de cartão, taxa de desconto (MDR), antecipação de recebíveis, FIDC, perda esperada, PCLD",
 "O varejo vende muito a prazo no cartão e costuma antecipar os recebíveis. A questão contábil é se a antecipação baixa o recebível ou é um empréstimo.",
 [
  ("NBC TG 48", "5.1.3", "Contas a receber de clientes sem componente de financiamento significativo são reconhecidas pelo preço da transação."),
  ("NBC TG 48", "5.5.15", "Perda de crédito esperada pela abordagem simplificada (vida inteira) para contas a receber de clientes; matriz de provisão por faixa de atraso é aceita."),
  ("NBC TG 48", "3.2.3–3.2.6", "Antecipação de recebíveis (banco, adquirente, FIDC): só baixa o recebível se transferir substancialmente todos os riscos e benefícios; se a loja continua com o risco de inadimplência ou chargeback, mantém o recebível e registra um passivo (empréstimo)."),
  ("NBC TG 40", "31–42", "Divulgar risco de crédito, de liquidez e as operações de antecipação."),
 ],
 ["Taxa de administração do cartão (MDR) como despesa de vendas ou redução de receita, conforme política documentada.",
  "Analisar contratos de antecipação e de cessão a FIDC para decidir baixa x empréstimo.",
  "Matriz de perdas esperadas atualizada com histórico de inadimplência e chargeback."]),

("04-lojas-e-arrendamentos", "Lojas, aluguéis e impairment",
 "aluguel de loja, shopping, aluguel percentual sobre vendas, luvas, benfeitorias em imóvel de terceiros, impairment de loja, fechamento de loja",
 "Quase todo varejista aluga seus pontos. Com a NBC TG 06 o aluguel fixo vira ativo de direito de uso e passivo; cada loja costuma ser testada para impairment separadamente.",
 [
  ("NBC TG 06", "22–24", "Aluguel de loja: ativo de direito de uso e passivo de arrendamento. O direito de uso inclui pagamentos feitos antes do início (ex.: luvas/res sperata pagas ao locador), custos diretos iniciais e estimativa de restaurar o imóvel."),
  ("NBC TG 06", "27–28", "Entram no passivo os pagamentos fixos e os variáveis que dependem de índice ou taxa (ex.: aluguel corrigido pelo IGP-M ou IPCA)."),
  ("NBC TG 06", "38", "Aluguel percentual sobre o faturamento da loja não entra no passivo: é despesa no período em que a venda acontece."),
  ("NBC TG 06", "5–8", "Contratos de até 12 meses e ativos de baixo valor podem ficar como despesa de aluguel."),
  ("NBC TG 01", "66–73", "Cada loja que gera entradas de caixa independentes costuma ser uma unidade geradora de caixa: testar impairment da loja (direito de uso + benfeitorias) quando houver indício, como prejuízo recorrente."),
  ("NBC TG 27", "—", "Benfeitorias em imóvel alugado são imobilizado, depreciadas pela vida útil limitada ao prazo esperado do contrato."),
  ("NBC TG 25", "66–69", "Loja fechada com contrato ainda em vigor: avaliar contrato oneroso (custos inevitáveis maiores que os benefícios), além do impairment do direito de uso."),
 ],
 ["Inventário de contratos de aluguel (prazo, renovações, índices de correção, aluguel percentual).",
  "Teste de impairment por loja com plano de negócios.",
  "Política de depreciação de benfeitorias alinhada ao prazo dos contratos."]),

("05-tributos-no-varejo", "Tributos no varejo",
 "ICMS, ICMS-ST, PIS/COFINS monofásico, créditos, receita bruta x líquida, reforma tributária no varejo",
 "Tributos sobre vendas e compras afetam custo, receita líquida e tributos a recuperar.",
 [
  ("NBC TG 16", "11", "Tributos sem direito a crédito (ICMS-ST pago na compra, PIS/COFINS monofásico) compõem o custo da mercadoria; os recuperáveis não."),
  ("NBC TG 47", "47", "Tributos cobrados do cliente em nome do fisco não são receita: deduções da receita bruta na DRE."),
  ("NBC TG 25", "33–35", "Créditos tributários discutidos na Justiça (ex.: teses de PIS/COFINS) só viram ativo quando praticamente certos."),
  ("OT CFC 01/2026", "12", "Reforma tributária: créditos de IBS e CBS recuperáveis também ficam fora do custo da mercadoria."),
 ],
 ["Conciliar créditos de ICMS/PIS/COFINS e saldos de ICMS-ST a ressarcir.",
  "Mapear itens com tributação monofásica e substituição tributária.",
  "Preparar o ERP para IBS/CBS (ver areas/reforma-tributaria.md)."]),
]

FAQ = [
 ("Bonificação recebida do fornecedor é receita?", "Não; reduz o custo da mercadoria.", "NBC TG 16", "11"),
 ("ICMS-ST pago na compra entra no custo?", "Sim, quando não há direito a crédito.", "NBC TG 16", "11"),
 ("Furto e quebra de estoque vão para onde?", "Despesa do período em que ocorrem.", "NBC TG 16", "34"),
 ("Posso usar o método de varejo?", "Sim, se o resultado se aproximar do custo.", "NBC TG 16", "21"),
 ("No marketplace, a receita é o valor total da venda?", "Só se a empresa for principal; se for agente, só a comissão.", "NBC TG 47", "B34–B38"),
 ("Pontos de fidelidade viram receita quando?", "Quando usados ou expirados; até lá, receita diferida.", "NBC TG 47", "B39–B43"),
 ("Vale-presente não usado vira receita?", "Sim, a parte que se espera nunca ser usada, proporcionalmente ao uso.", "NBC TG 47", "B44–B47"),
 ("Antecipação de recebíveis de cartão baixa o recebível?", "Só se transferir substancialmente riscos e benefícios.", "NBC TG 48", "3.2.6"),
 ("Aluguel sobre % das vendas entra no passivo de arrendamento?", "Não; é despesa do período.", "NBC TG 06", "38"),
 ("Cada loja é testada para impairment separadamente?", "Em geral sim: cada loja costuma ser uma UGC.", "NBC TG 01", "66–73"),
]
