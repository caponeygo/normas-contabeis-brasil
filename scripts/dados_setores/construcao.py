# Setor: Construção e incorporação imobiliária. Formato: ver scripts/gerar_setores.py.
NOME = "Construção e Incorporação"
PASTA = "Construcao"
USE_PARA = ("incorporação imobiliária, venda na planta, POC, permuta de terreno, juros na obra, distratos, empreiteiras, "
            "contratos de construção, medição de obra, aditivos e pleitos, contrato oneroso, garantia de obra")
INTRO = ("Trechos das normas que importam para incorporadoras (que vendem unidades na planta) e construtoras/empreiteiras "
         "(que constroem para terceiros sob contrato).")

EXTERNAS = {
 "Ofício-Circular CVM/SNC/SEP 02/2018": (
  "Receita de incorporação imobiliária pela NBC TG 47 (POC)",
  "https://conteudo.cvm.gov.br/legislacao/oficios-circulares/snc-sep/oc-snc-sep-0218.html",
  "Orientação da CVM às companhias abertas incorporadoras sobre a aplicação do CPC 47 aos contratos de compra e venda de unidades imobiliárias não concluídas."),
 "Lei 10.931/2004": (
  "Patrimônio de afetação e RET na incorporação imobiliária",
  "https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.931.htm",
  ""),
 "Código Civil, art. 618": (
  "Garantia de solidez e segurança da obra (5 anos)",
  "https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm",
  ""),
}

TOPICOS = [
("01-incorporacao-imobiliaria", "Incorporação imobiliária",
 "unidades vendidas na planta, receita ao longo da obra (POC), custo do imóvel, estoque de imóveis, juros capitalizados, permuta de terreno, estande e apartamento decorado, distratos",
 "A incorporadora vende unidades antes de construí-las. No Brasil, as companhias abertas reconhecem a receita das unidades vendidas ao longo da obra (POC), com base na NBC TG 47 e na orientação da CVM.",
 [
  ("CTG 01", "2", "Custo do imóvel: terreno (com gastos de aquisição e regularização), projetos, custos de construção e encargos financeiros do financiamento da obra."),
  ("CTG 01", "6–8", "Encargos financeiros dos financiamentos diretamente associados à construção e à compra de terrenos do empreendimento são registrados no estoque de imóveis a comercializar; o valor capitalizado no período não pode exceder os encargos incorridos e é calculado por taxa de capitalização sobre os custos incorridos com o imóvel."),
  ("CTG 01", "20–22", "Permuta entre itens de mesma natureza e valor não gera ganho (item 20). Permuta de terreno por unidades a construir tem substância comercial: o terreno entra no estoque pelo valor justo, em contrapartida a adiantamento de clientes no passivo, na assinatura do contrato (itens 21 e 22)."),
  ("NBC TG 47", "35", "Receita ao longo do tempo quando a unidade não tem uso alternativo para a incorporadora e ela tem direito executável a receber pelo que já construiu (item 35(c))."),
  ("NBC TG 47", "39–45", "Medição do progresso da obra, em geral pelo custo incorrido sobre o custo total orçado (POC), excluindo custos que não refletem o avanço (ex.: terreno)."),
  ("Ofício-Circular CVM/SNC/SEP 02/2018", "—", "Para companhias abertas, a CVM orienta como aplicar a NBC TG 47 às vendas de unidades em construção, mantendo o reconhecimento ao longo da obra quando atendidos os critérios."),
  ("CTG 04", "—", "Orientação brasileira original sobre receita de unidades em construção (escrita para a antiga ITG 02/NBC TG 30, hoje revogadas): usar como histórico; a base atual é a NBC TG 47."),
  ("NBC TG 47", "B20–B27", "Distratos e devoluções esperadas: estimar cancelamentos e não reconhecer receita do que se espera reverter (Lei 13.786/2018 define multas e retenções)."),
 ],
 ["Orçamento de custo por empreendimento atualizado e aprovado (base do POC).",
  "Separar custo de terreno do avanço físico/financeiro da obra.",
  "Controle de juros capitalizados por empreendimento.",
  "Provisão para distratos baseada em histórico."]),

("02-contratos-de-construcao", "Construtoras e empreiteiras",
 "obras para terceiros, contrato de empreitada, medição, aditivos, pleitos (claims), multas, retenções contratuais, contrato oneroso",
 "Construtoras que executam obras sob contrato reconhecem receita ao longo da execução e precisam provisionar contratos com prejuízo.",
 [
  ("NBC TG 47", "35", "Obra no terreno do cliente: o cliente controla o ativo à medida que ele é construído, logo receita ao longo do tempo."),
  ("NBC TG 47", "39–45", "Medir o progresso por custo incorrido, medição física ou marcos, o que melhor refletir a execução."),
  ("NBC TG 47", "18–21", "Aditivos de escopo e preço são modificações de contrato: contabilizar quando aprovados pelas partes."),
  ("NBC TG 47", "50–59", "Pleitos (claims), multas por atraso e bônus de desempenho são contraprestação variável: só reconhecer o que for altamente provável de não reverter."),
  ("NBC TG 25", "66–69", "Contrato oneroso (custo inevitável maior que a receita): reconhecer a perda inteira como provisão assim que identificada."),
 ],
 ["Reavaliar a margem estimada de cada contrato a cada fechamento.",
  "Registrar aditivos só após aprovação; pleitos com critério conservador.",
  "Provisão para contratos onerosos."]),

("03-garantias-imobilizado-e-tributos", "Garantias, equipamentos e tributos",
 "garantia de obra de 5 anos, provisões, equipamentos de construção, gruas e formas, leasing de máquinas, patrimônio de afetação, RET",
 "Obrigações que continuam depois da entrega e particularidades de equipamentos e tributação do setor.",
 [
  ("NBC TG 25", "14, 24, 39", "Provisão para garantia de obra (vícios construtivos), estimada pelo histórico do conjunto de obras entregues."),
  ("Código Civil, art. 618", "—", "Construtor responde por 5 anos pela solidez e segurança da obra: base legal da obrigação de garantia."),
  ("NBC TG 27", "43–47", "Equipamentos de construção (gruas, formas, andaimes) com componentes de vida útil diferente: componentizar e depreciar pela vida útil econômica."),
  ("NBC TG 06", "22–24", "Equipamentos alugados por mais de 12 meses: direito de uso + passivo."),
  ("Lei 10.931/2004", "—", "Patrimônio de afetação e regime especial de tributação (RET) são temas jurídico-fiscais; contabilmente, manter controles e demonstrações por empreendimento afetado."),
 ],
 ["Provisão de garantia de obra por empreendimento entregue.",
  "Controle contábil separado por empreendimento com patrimônio de afetação."]),
]

FAQ = [
 ("Incorporadora reconhece receita na venda ou na entrega das chaves?", "No Brasil, em geral ao longo da obra (POC), se atendido o item 35(c).", "NBC TG 47", "35"),
 ("Como medir o avanço da obra?", "Em geral custo incorrido sobre custo orçado, sem o terreno.", "NBC TG 47", "39–45"),
 ("Juros do financiamento da obra entram no estoque?", "Sim, enquanto a obra está em andamento.", "CTG 01", "6–8"),
 ("Terreno recebido em permuta entra por quanto?", "Pelo valor justo, com adiantamento de clientes no passivo.", "CTG 01", "21–22"),
 ("Contrato de obra com prejuízo previsto?", "Provisionar a perda total assim que identificada (contrato oneroso).", "NBC TG 25", "66–69"),
 ("Pleito contra o cliente vira receita quando?", "Quando for altamente provável que não haverá reversão.", "NBC TG 47", "50–59"),
 ("Preciso provisionar garantia de obra?", "Sim, pelo histórico de reparos das obras entregues.", "NBC TG 25", "14, 24, 39"),
]
