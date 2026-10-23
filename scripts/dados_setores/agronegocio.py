# Setor: Agronegócio. Formato: ver scripts/gerar_setores.py.
NOME = "Agronegócio"
PASTA = "Agronegocio"
USE_PARA = ("rebanho, lavouras, florestas, cana, café, ativo biológico a valor justo, colheita, terras, plantas portadoras, "
            "arrendamento e parceria rural, crédito rural subsidiado, hedge de commodities, CPR, CBIO")
INTRO = ("Trechos das normas que importam para produtores rurais, usinas, cooperativas agropecuárias, frigoríficos com "
         "criação própria e empresas florestais: do ativo biológico na fazenda até o produto colhido no estoque.")

TOPICOS = [
("01-ativo-biologico-e-colheita", "Ativo biológico e produto colhido",
 "gado, aves, lavouras em formação, florestas para corte, valor justo menos despesa de venda, ganho na valorização, colheita, produto agrícola em estoque",
 "A NBC TG 29 é a norma central do agro: animais e plantas vivos ficam a valor justo e a valorização vai para o resultado, até a colheita. Depois da colheita, o produto vira estoque (NBC TG 16).",
 [
  ("NBC TG 29", "1–2", "Alcance: ativos biológicos (exceto plantas portadoras), produto agrícola no ponto de colheita e subvenções ligadas a eles. Terras e plantas portadoras ficam fora (vão para a NBC TG 27)."),
  ("NBC TG 29", "5A", "Não são plantas portadoras as plantas cultivadas para serem colhidas como produto (ex.: árvores para madeira) nem culturas anuais (milho, trigo): seguem a NBC TG 29."),
  ("NBC TG 29", "12", "Ativo biológico mensurado ao valor justo menos a despesa de venda no reconhecimento inicial e em cada fechamento."),
  ("NBC TG 29", "13", "Produto agrícola colhido mensurado ao valor justo menos a despesa de venda no momento da colheita; esse valor é o custo para a NBC TG 16."),
  ("NBC TG 29", "26–29", "Ganhos e perdas na variação do valor justo (crescimento do rebanho, engorda, desenvolvimento da lavoura, preço) vão para o resultado do período."),
  ("NBC TG 29", "30–33", "Se o valor justo não puder ser mensurado de forma confiável no reconhecimento inicial, usar custo menos depreciação e perdas, até que se torne mensurável."),
  ("NBC TG 16", "20", "Estoque de produto agrícola colhido: custo inicial = valor justo menos despesa de venda na colheita (NBC TG 29)."),
  ("NBC TG 16", "3", "Produtores e tradings que mensuram estoques de produtos agrícolas pelo valor realizável líquido ou valor justo, conforme prática do setor, ficam fora das regras de mensuração da NBC TG 16."),
 ],
 ["Laudo ou modelo de valor justo por classe de ativo biológico (rebanho por categoria, lavoura por estágio).",
  "Separar despesas de venda (frete, comissões) na mensuração.",
  "Registrar a colheita: baixa do ativo biológico e entrada no estoque pelo valor justo."]),

("02-terras-plantas-portadoras-e-arrendamentos", "Terras, plantas portadoras e arrendamentos",
 "terra nua, benfeitorias, máquinas agrícolas, cana-de-açúcar (soqueira), café, laranja, arrendamento rural, parceria agrícola",
 "Terra, máquinas e plantas que só servem para produzir frutos ficam no imobilizado; terras de terceiros podem gerar arrendamento.",
 [
  ("NBC TG 27", "58", "Terrenos e edifícios são contabilizados separadamente; a terra em geral tem vida ilimitada e não é depreciada."),
  ("NBC TG 29", "2", "Plantas portadoras (que produzem por vários períodos e não são vendidas como produto, ex.: cana em soqueira, café, laranjais) seguem a NBC TG 27; o produto que crescer nelas segue a NBC TG 29."),
  ("NBC TG 06", "9–11", "Arrendamento rural de terra por prazo determinado: em regra arrendamento (direito de uso + passivo). Parceria agrícola com divisão de risco da produção: avaliar se transfere o direito de controlar o uso da terra."),
  ("NBC TG 06", "38", "Pagamentos variáveis que dependem da produção ou do preço da commodity (ex.: sacas por hectare a preço de mercado) não entram no passivo, salvo se fixos em substância."),
 ],
 ["Separar terra nua de benfeitorias e de plantas portadoras.",
  "Revisar contratos de arrendamento e parceria rural.",
  "Vida útil das plantas portadoras (ex.: número de cortes da cana) documentada."]),

("03-credito-rural-hedge-e-cpr", "Crédito rural, hedge e CPR",
 "Plano Safra, crédito rural com juros subsidiados, subvenção, contratos de venda futura, hedge de soja, milho e boi, CPR, barter",
 "O agro se financia com crédito subsidiado e protege preço com contratos futuros e derivativos.",
 [
  ("NBC TG 07", "10A", "Crédito rural com juros abaixo do mercado: o benefício (diferença para o valor justo do empréstimo) é subvenção governamental."),
  ("NBC TG 29", "34–35", "Subvenção incondicional ligada a ativo biológico a valor justo vai para o resultado quando se torna recebível; se condicional, quando as condições forem cumpridas."),
  ("NBC TG 48", "2.4", "Contrato de venda futura com entrega física da própria produção (uso próprio) fica fora do tratamento de derivativo; contratos liquidados pelo líquido ou para especulação são derivativos a valor justo."),
  ("NBC TG 48", "cap. 6", "Hedge de preço de commodities agrícolas ou de câmbio de exportação: contabilidade de hedge exige documentação formal; a parte eficaz do hedge de fluxo de caixa fica no ORA até a venda."),
  ("NBC TG 40", "31–42", "Divulgar riscos de preço, câmbio, crédito e liquidez e os hedges contratados."),
 ],
 ["Calcular subvenção nos financiamentos rurais com taxa abaixo do mercado.",
  "Classificar CPRs e contratos a termo: entrega física (uso próprio) x derivativo.",
  "Documentar relações de hedge antes de contratar."]),

("04-usinas-carbono-e-auditoria", "Usinas, CBIO e auditoria no agro",
 "usina de açúcar e etanol, CBIO, créditos de carbono, contagem de rebanho, valor justo de ativos biológicos, especialistas agronômicos",
 "Particularidades de usinas e pontos que o auditor mais examina no agro.",
 [
  ("CTG 10", "—", "CBIO emitido por produtor de biocombustível e créditos de carbono: classificação conforme o uso (estoque, intangível ou instrumento financeiro); obrigação de emissão gera passivo."),
  ("NBC TA 540", "—", "Valor justo de ativos biológicos é estimativa: o auditor avalia premissas (preço, produtividade, taxa de desconto) e o viés da administração."),
  ("NBC TA 501", "4–7", "Contagem física de estoques de grãos e insumos e verificação de existência de rebanho."),
  ("NBC TA 620", "—", "Uso de especialistas (agrônomos, avaliadores) para laudos de ativos biológicos e terras."),
 ],
 ["Inventário de rebanho e estoques de grãos no fechamento.",
  "Documentar premissas do valor justo (preços de mercado, produtividade).",
  "Controle de CBIOs emitidos e vendidos."]),
]

FAQ = [
 ("Gado em engorda fica a custo ou valor justo?", "Valor justo menos despesa de venda, com a variação no resultado.", "NBC TG 29", "12"),
 ("Pé de café é ativo biológico?", "Não; é planta portadora, vai para o imobilizado. O café que cresce nele é ativo biológico.", "NBC TG 29", "2"),
 ("Eucalipto para madeira é planta portadora?", "Não; árvore cultivada para ser colhida como produto segue a NBC TG 29.", "NBC TG 29", "5A"),
 ("Grão colhido entra no estoque por quanto?", "Valor justo menos despesa de venda na colheita.", "NBC TG 16", "20"),
 ("E se não der para medir o valor justo?", "Custo menos depreciação e perdas, até ser mensurável.", "NBC TG 29", "30–33"),
 ("Terra se deprecia?", "Em geral não.", "NBC TG 27", "58"),
 ("Juros do Plano Safra abaixo do mercado têm efeito contábil?", "Sim: a diferença para o valor justo é subvenção.", "NBC TG 07", "10A"),
 ("Venda futura da safra é derivativo?", "Não, se for para entrega física da própria produção (uso próprio).", "NBC TG 48", "2.4"),
]
