# Partes das normas que importam para a INDÚSTRIA, organizadas pelo ciclo da fábrica.
# Gera a pasta Industrial/ e anota cada norma em normas.json (campo "industria").
# Os itens seguem a numeração do CPC, que acompanha a IAS/IFRS correspondente.
# Textos redigidos como orientação (não são cópia das normas): confira o texto oficial.
import re, shutil, unicodedata

AVISO = ("> Resumo orientativo dos trechos das normas aplicáveis à indústria; não substitui o texto oficial. "
         "Os números de item seguem o CPC (mesma numeração da IAS/IFRS). Confira sempre pelo link oficial.")

# (arquivo, título, use para, introdução, [(norma, itens, o que diz para a indústria)], [checklist])
TOPICOS = [
("01-estoques-e-custo-de-producao", "Estoques e custo de produção",
 "custo do produto fabricado, matéria-prima, produtos em elaboração e acabados, CIF, rateio, ociosidade, custo-padrão, PEPS/médio, obsolescência, inventário",
 "O coração da contabilidade industrial. O CPC 16 exige custeio por absorção: o produto carrega materiais, mão de obra direta e custos indiretos de fabricação (CIF) fixos e variáveis. Custeio variável serve para gestão, não para as demonstrações.",
 [
  ("NBC TG 16", "9", "Estoque fica pelo menor valor entre custo e valor realizável líquido (VRL)."),
  ("NBC TG 16", "10–11", "Custo de aquisição de insumos: preço + impostos de importação e outros tributos, exceto os recuperáveis perante o fisco + frete, seguro e manuseio na compra, menos descontos e abatimentos. ICMS, IPI, PIS/COFINS com direito a crédito ficam fora do custo (vão para tributos a recuperar)."),
  ("NBC TG 16", "12", "Custo de transformação = mão de obra direta + rateio sistemático dos CIF fixos (depreciação e manutenção da fábrica, gestão da fábrica) e variáveis (materiais indiretos, energia de produção)."),
  ("NBC TG 16", "13", "CIF fixos são alocados pela capacidade NORMAL de produção. Quando a fábrica produz abaixo do normal, a parcela não alocada (ociosidade) vai direto para despesa do período, sem inflar o estoque. Com produção anormalmente alta, o custo fixo por unidade diminui."),
  ("NBC TG 16", "14", "Produtos conjuntos: rateio do custo comum por base racional e consistente (ex.: valor de venda relativo). Subprodutos irrelevantes podem ser medidos pelo VRL e abatidos do custo do produto principal."),
  ("NBC TG 16", "16", "Ficam FORA do custo e vão para despesa: desperdício anormal de material, mão de obra ou outros; armazenagem (salvo se necessária entre fases da produção); despesas administrativas que não contribuem para a produção; despesas de venda (inclusive frete na venda)."),
  ("NBC TG 16", "18", "Compra a prazo com financiamento embutido: a diferença entre o preço a prazo e o à vista é despesa financeira ao longo do prazo, não custo do estoque."),
  ("NBC TG 16", "21", "Custo-padrão é aceito se o resultado se aproximar do custo real; os padrões devem ser revistos regularmente e as variações tratadas para que o estoque fique a custo real."),
  ("NBC TG 16", "25", "Fórmulas de custo permitidas: PEPS ou custo médio ponderado, a mesma para estoques de natureza e uso semelhantes. UEPS não é aceito."),
  ("NBC TG 16", "28–33", "Redução ao VRL por obsolescência, dano ou queda de preço, normalmente item a item. Matéria-prima não é baixada se o produto acabado em que será usada for vendido pelo custo ou acima (item 32)."),
  ("NBC TG 16", "34–35", "Na venda, o custo do estoque vira CPV. Perdas e ajustes ao VRL são despesa do período; reversões reduzem o CPV. Peças fabricadas para uso no próprio imobilizado vão para o ativo, não para o resultado."),
  ("NBC TG 16", "36", "Divulgar: política e fórmula de custo, saldo por classe (matéria-prima, em elaboração, acabados, almoxarifado), CPV, ajustes ao VRL e reversões, estoques dados em garantia."),
  ("NBC TG 27", "49", "Depreciação das máquinas da produção é CIF: entra no custo do estoque, não vai direto para a despesa."),
  ("NBC TG 12", "—", "Compras e vendas a prazo relevantes: ajuste a valor presente; o juro embutido sai do custo do insumo e da receita e vai para o resultado financeiro."),
 ],
 ["Custeio por absorção nas demonstrações (custeio variável só para gestão).",
  "Capacidade normal definida e documentada; ociosidade calculada e lançada como despesa.",
  "Créditos de ICMS, IPI, PIS e COFINS fora do custo.",
  "Frete na compra = custo; frete na venda = despesa de venda; armazenagem de produto acabado = despesa.",
  "Variações do custo-padrão apropriadas entre estoque e CPV no fechamento.",
  "Teste de VRL e provisão para obsolescência (itens parados, vencidos, sem giro).",
  "Inventário físico periódico e conciliação com o razão."]),

("02-maquinas-e-fabrica", "Máquinas, fábrica e imobilizado",
 "máquinas, linha de produção, construção de fábrica, componentização, manutenção, paradas programadas, peças de reposição, depreciação por unidades produzidas, impairment, leasing de equipamentos",
 "Na indústria, o imobilizado costuma ser o maior ativo. As decisões que mais mexem no resultado: o que capitalizar, como componentizar, o método e a vida útil da depreciação e quando testar impairment.",
 [
  ("NBC TG 27", "7–8", "Peças de reposição, sobressalentes e equipamentos de manutenção são imobilizado quando usados por mais de um período (ex.: peças estratégicas de uma linha); caso contrário, ficam em estoque (almoxarifado)."),
  ("NBC TG 27", "12–14", "Manutenção do dia a dia vai para o resultado (ou para o CIF). Grandes paradas, revisões gerais e inspeções relevantes podem ser capitalizadas como componente, baixando o valor da parada anterior."),
  ("NBC TG 27", "16–17", "Custo da máquina: preço + impostos não recuperáveis + frete, instalação, montagem, preparação do local, testes de funcionamento e honorários técnicos + estimativa de desmontagem e restauração do local."),
  ("NBC TG 27", "20A", "Produtos fabricados durante os testes, antes de a máquina ficar pronta para uso: a receita da venda e o custo deles vão para o resultado, sem reduzir o custo da máquina; o custo desses itens é medido pela NBC TG 16 (incluído pela Revisão NBC 12)."),
  ("NBC TG 27", "22", "Máquina ou fábrica construída pela própria empresa segue a mesma lógica; desperdícios anormais na construção não entram no custo."),
  ("NBC TG 27", "43–47", "Componentização: partes com custo relevante e vida útil diferente (ex.: forno e seu revestimento refratário, motor de uma prensa) são depreciadas separadamente."),
  ("NBC TG 27", "50–51", "Vida útil e valor residual revistos pelo menos uma vez ao ano; a mudança é estimativa (efeito prospectivo, NBC TG 23). Vida útil econômica, não a taxa fiscal."),
  ("NBC TG 27", "55", "A depreciação começa quando a máquina está disponível para uso e não para por ociosidade (exceto no método de unidades produzidas)."),
  ("NBC TG 27", "60–62A", "O método deve refletir o consumo dos benefícios: linear, saldos decrescentes ou unidades produzidas (comum em máquinas cujo desgaste depende do uso). Depreciação baseada em receita não é aceita."),
  ("NBC TG 20", "4–8", "Juros de empréstimos para construir uma fábrica ou instalar uma linha que leva tempo para ficar pronta são capitalizados no ativo. Estoques fabricados em grande quantidade de forma repetitiva estão dispensados da norma."),
  ("NBC TG 20", "14, 17–22", "Com dívida geral, usar a taxa média ponderada; capitalizar só durante a construção ativa, suspender em paralisações longas e parar quando o ativo estiver pronto."),
  ("NBC TG 01", "9, 12", "Indícios de impairment comuns na indústria: ociosidade relevante, obsolescência tecnológica, dano físico, queda de demanda ou de margem, plano de fechar ou reestruturar uma planta."),
  ("NBC TG 01", "66–73", "A unidade geradora de caixa costuma ser a planta ou a linha de produção que gera entradas de caixa independentes; o teste é feito no nível da UGC."),
  ("NBC TG 06", "9–11, B9–B31", "Verificar arrendamento embutido em contratos de fornecimento ou serviço com ativo dedicado (ex.: tanque, gerador ou equipamento exclusivo instalado pelo fornecedor). Empilhadeiras, galpões e máquinas alugadas viram direito de uso + passivo."),
  ("NBC TG 06", "5–8", "Isenções: contratos de até 12 meses e ativos de baixo valor podem ficar como despesa de aluguel."),
  ("ITG 12", "—", "Se mudar a estimativa da provisão de desmontagem ou restauração do local da fábrica, o ajuste vai para o custo do ativo e afeta a depreciação futura, não o resultado de uma vez."),
 ],
 ["Política de capitalização (valor mínimo, o que é peça de estoque x imobilizado).",
  "Inventário físico e plaqueta do imobilizado; laudo de vida útil (econômica) revisado todo ano.",
  "Componentização das máquinas relevantes e das grandes paradas programadas.",
  "Juros capitalizados em obras e instalações em andamento.",
  "Teste de impairment por planta ou linha quando houver ociosidade ou queda de margem.",
  "Diferença entre depreciação societária e fiscal controlada para o IR diferido (ver tópico 04).",
  "Contratos de aluguel de equipamentos e de fornecimento revisados para arrendamento embutido."]),

("03-vendas-e-pos-venda", "Vendas, garantia e pós-venda",
 "faturamento, momento da receita, Incoterms (FOB/CIF), bonificações, rebates, devoluções, consignação, bill-and-hold, produtos sob encomenda, garantia de produto, assistência técnica",
 "Quando e quanto reconhecer de receita na venda de produtos, e como tratar as obrigações que continuam depois da venda.",
 [
  ("NBC TG 47", "31–38", "Receita quando o CONTROLE do produto passa ao cliente. Os Incoterms ajudam: em FOB o controle passa na origem; em CIF/entrega no destino normalmente só na entrega. Frete e seguro prestados depois da transferência do controle podem ser uma obrigação separada."),
  ("NBC TG 47", "35", "Produção sob encomenda (bens de capital, moldes, equipamentos específicos) sem uso alternativo e com direito a receber pelo que já foi feito: receita ao longo da produção, pelo avanço."),
  ("NBC TG 47", "50–59", "Descontos, bonificações, rebates por volume, verbas comerciais e multas contratuais são contraprestação variável: reduzem a receita pela melhor estimativa, sem risco de reversão relevante."),
  ("NBC TG 47", "60–65", "Venda a prazo com juros embutidos: separar o componente de financiamento significativo. Atenção: no Brasil o item 63 (dispensa para prazos de até 1 ano, existente na IFRS 15) foi eliminado; avaliar junto com o AVP da NBC TG 12."),
  ("NBC TG 47", "B20–B27", "Direito de devolução: receita só pelo que se espera não voltar, com passivo de reembolso e ativo pelo produto a recuperar."),
  ("NBC TG 47", "B28–B33", "Garantia que só assegura que o produto funciona conforme especificado → provisão (NBC TG 25). Garantia estendida vendida à parte ou serviço adicional → obrigação de desempenho separada, com receita diferida."),
  ("NBC TG 47", "B77–B78", "Remessa em consignação: sem receita enquanto o consignatário não vender ou não obtiver o controle."),
  ("NBC TG 47", "B79–B82", "Bill-and-hold (fatura e o produto fica na fábrica a pedido do cliente): só é receita se o produto estiver identificado, pronto, separado e não puder ser usado para outro cliente."),
  ("NBC TG 25", "14, 24, 39", "Provisão de garantia: reconhecida na venda quando houver histórico de reparos, estimada para o conjunto de produtos (valor esperado pelo histórico de defeitos)."),
  ("ITG 15", "—", "Fabricantes de eletroeletrônicos: obrigação de custear o descarte (logística reversa) conforme a participação no mercado no período de mensuração."),
 ],
 ["Momento da receita conforme Incoterm e entrega efetiva; corte (cut-off) de notas emitidas e não entregues.",
  "Bonificações e rebates provisionados como redução da receita, não como despesa de venda.",
  "Provisão de garantia baseada em histórico de defeitos por linha de produto.",
  "Separar garantia estendida e serviços de instalação/assistência vendidos juntos.",
  "Tratar devoluções esperadas e remessas em consignação."]),

("04-tributos-e-incentivos", "Tributos e incentivos fiscais",
 "ICMS, IPI, PIS/COFINS, créditos tributários, crédito presumido, incentivos de ICMS, subvenção para investimento, financiamento subsidiado (BNDES, FINEP), IR diferido, teses tributárias",
 "Indústrias concentram créditos de tributos, incentivos estaduais e diferenças entre a contabilidade e o fisco. A regra contábil é separar o que é custo, o que é tributo a recuperar e o que é subvenção.",
 [
  ("NBC TG 16", "11", "Tributos recuperáveis (créditos de ICMS, IPI, PIS e COFINS) não compõem o custo do estoque; ficam como tributos a recuperar."),
  ("NBC TG 27", "16", "O mesmo vale para máquinas: só entram no custo os impostos não recuperáveis (ex.: crédito de ICMS sobre ativo apropriado em parcelas fica a recuperar)."),
  ("NBC TG 07", "12, 17", "Incentivos fiscais (crédito presumido e redução de base de ICMS, isenções) são subvenção governamental: reconhecidos no resultado à medida que compensam os custos a que se referem; os ligados a ativos (ex.: para comprar máquinas), ao longo da vida útil do ativo."),
  ("NBC TG 07", "10A", "Empréstimo subsidiado (juros abaixo do mercado, ex.: linhas BNDES/FINEP): a diferença entre o valor recebido e o valor justo do empréstimo é subvenção."),
  ("NBC TG 07", "—", "No Brasil, o valor da subvenção pode ser destinado à reserva de incentivos fiscais no PL (Lei 6.404, art. 195-A). O tratamento fiscal federal mudou com a Lei 14.789/2023 (crédito fiscal de subvenção para investimento): conferir com o tributário."),
  ("NBC TG 32", "15–24", "Diferenças temporárias típicas da indústria: depreciação contábil x fiscal, provisão para obsolescência de estoques, provisão de garantias, ajuste a valor presente e subvenções. Geram IR/CS diferido."),
  ("NBC TG 32", "24–31, 34–36", "Ativo fiscal diferido sobre prejuízo fiscal e diferenças só se houver lucro tributável futuro provável (projeção da planta)."),
  ("ITG 22", "—", "Teses de IR/CS com tratamento incerto: registrar o efeito se for provável que o fisco não aceite a posição."),
  ("NBC TG 25", "33–35", "Teses de outros tributos (PIS/COFINS, ICMS, IPI): crédito a recuperar por ação judicial é ativo contingente e só é reconhecido quando praticamente certo (em geral, após trânsito em julgado e com valor mensurável)."),
 ],
 ["Conciliação mensal dos créditos de ICMS, IPI, PIS e COFINS (e futuramente IBS/CBS da reforma tributária).",
  "Mapear cada incentivo estadual: natureza, contrapartidas, registro no resultado e destinação à reserva.",
  "Controle das diferenças temporárias para o IR diferido.",
  "Avaliar teses tributárias: ITG 22 para IR/CS, NBC TG 25 para os demais tributos."]),

("05-pesquisa-e-desenvolvimento", "Pesquisa e desenvolvimento de produtos",
 "P&D, novos produtos, protótipos, engenharia de produto, moldes e ferramentas, patentes, software industrial",
 "Quando o gasto com novos produtos ou processos pode virar ativo intangível e quando é despesa.",
 [
  ("NBC TG 04", "54–56", "Fase de pesquisa (buscar conhecimento, avaliar alternativas de materiais e processos): sempre despesa."),
  ("NBC TG 04", "57", "Fase de desenvolvimento vira intangível só se a empresa demonstrar TODOS: viabilidade técnica, intenção de concluir, capacidade de usar ou vender, geração de benefícios (mercado), recursos para terminar e mensuração confiável dos gastos."),
  ("NBC TG 04", "59", "Exemplos de desenvolvimento: projeto, construção e teste de protótipos e modelos; projeto de ferramentas, moldes e matrizes com nova tecnologia; planta-piloto."),
  ("NBC TG 04", "71", "O que já foi lançado como despesa não volta a ser ativo depois."),
  ("NBC TG 04", "97–106", "Desenvolvimento capitalizado é amortizado pela vida útil do produto ou processo, a partir de quando estiver disponível para uso."),
  ("NBC TG 27", "—", "Moldes, ferramentas e matrizes físicos usados na produção por mais de um período são imobilizado, não intangível."),
 ],
 ["Separar projetos em fase de pesquisa e de desenvolvimento, com documentação dos 6 critérios.",
  "Apropriar horas de engenharia por projeto.",
  "Incentivos fiscais de P&D (ex.: Lei do Bem) são tema fiscal; contabilmente seguem a NBC TG 07 quando forem subvenção."]),

("06-commodities-cambio-e-hedge", "Commodities, câmbio e hedge",
 "importação de insumos e máquinas, variação cambial, adiantamento a fornecedor estrangeiro, aço, cobre, alumínio, energia, derivativos, hedge de fluxo de caixa, contratos de compra para uso próprio",
 "Indústrias expostas a insumos cotados em dólar ou em bolsa precisam separar a variação cambial do custo e decidir se aplicam contabilidade de hedge.",
 [
  ("NBC TG 02", "21–23", "Insumo ou máquina importada entra pela taxa de câmbio à vista da data da transação (quando a compra se qualifica para reconhecimento, normalmente na transferência do controle). Por praticidade, aceita-se taxa média semanal ou mensal, salvo se o câmbio oscilar muito (item 22)."),
  ("NBC TG 02", "28", "A variação cambial do fornecedor estrangeiro a pagar depois da compra vai para o resultado financeiro; não altera o custo do estoque nem da máquina."),
  ("ITG 21", "—", "Adiantamento a fornecedor estrangeiro: o item comprado fica pela taxa do dia do adiantamento (não é atualizado depois)."),
  ("NBC TG 48", "2.4", "Contratos de compra de commodity para uso na própria produção (own use), liquidados com entrega física, ficam fora do tratamento de derivativo."),
  ("NBC TG 48", "cap. 6", "Hedge de fluxo de caixa de compras futuras de insumo ou de câmbio: a parte eficaz do derivativo fica no ORA e depois entra no custo do estoque comprado; a parte ineficaz vai para o resultado. Exige documentação formal na contratação."),
  ("NBC TG 40", "31–42", "Divulgar riscos de mercado (câmbio, commodities), análise de sensibilidade, liquidez e os hedges contratados."),
 ],
 ["Taxa de câmbio correta na entrada de importações; variação posterior no financeiro.",
  "Classificar contratos de commodity: uso próprio x derivativo.",
  "Se usar hedge accounting, documentar relação, objetivo e teste de eficácia antes de contratar.",
  "Notas com análise de sensibilidade a câmbio e commodities."]),

("07-dre-e-apresentacao", "DRE, CPV e apresentação",
 "DRE industrial, CPV, custo por função x natureza, margem bruta, ociosidade na DRE, IFRS 18 (2027), DVA, notas de estoques, segmentos por linha de produto",
 "Como a indústria apresenta custos e despesas e o que muda com a IFRS 18 a partir de 2027.",
 [
  ("NBC TG 26", "99–105", "Exercícios até 2026 (a NBC TG 26 foi revogada pela NBC TG 51 a partir de 2027): despesas por função (CPV, vendas, administrativas: padrão da indústria e exigido pela Lei 6.404, art. 187) ou por natureza. Quem apresenta por função divulga em nota a natureza, incluindo depreciação, amortização e benefícios a empregados (item 104)."),
  ("NBC TG 51", "69–74", "A partir de 1/1/2027 (IFRS 18): o CPV fica na categoria operacional e a DRE passa a ter os subtotais obrigatórios 'resultado operacional' e 'resultado antes de financiamentos e tributos sobre o lucro'."),
  ("NBC TG 51", "78–83", "Despesas operacionais agregadas por natureza ou por função (o custo das vendas é rubrica funcional que junta matéria-prima, pessoal, depreciação e amortização). Quem apresenta por função passa a divulgar em nota valores por natureza de despesas específicas."),
  ("NBC TG 51", "117–125", "Indicadores ajustados usados em comunicados ao mercado (EBITDA ajustado, margem ou lucro ajustado) são medidas de desempenho definidas pela administração (MPMs), com conciliação e explicação em nota. Não são MPM o lucro bruto e o resultado operacional antes de depreciação, amortização e impairment, o 'EBITDA' simples (item 118)."),
  ("NBC TG 16", "34, 36", "Ociosidade (item 13) e perdas anormais são despesas do período: apresentar de forma que a margem bruta não fique distorcida e divulgar quando relevantes."),
  ("NBC TG 09", "—", "DVA: insumos adquiridos de terceiros (matéria-prima, energia, serviços), retenções (depreciação) e distribuição do valor adicionado (pessoal, impostos, juros, acionistas)."),
  ("NBC TG 22", "—", "Companhias abertas: segmentos costumam ser linhas de produto ou plantas, conforme a gestão interna."),
 ],
 ["DRE por função com CPV; nota de despesas por natureza.",
  "Preparar a transição para a NBC TG 51 em 2027 (categorias, subtotais e MPMs); a NBC TG 51 exige conciliar a DRE do ano comparativo (Apêndice C).",
  "Nota de estoques por classe e de CPV."]),

("08-meio-ambiente-e-clima", "Meio ambiente, resíduos e clima",
 "passivo ambiental, área contaminada, licença ambiental, desmontagem de planta, resíduos, logística reversa, emissões, créditos de carbono, CBIO, IFRS S2, escopo 1, 2 e 3",
 "Obrigações ambientais da operação industrial e as novas divulgações de clima.",
 [
  ("NBC TG 25", "14, 19", "Provisão ambiental quando há obrigação presente por evento passado, legal ou não formalizada (ex.: recuperar área já contaminada, multas). Gastos futuros para continuar operando (ex.: instalar filtros) não são provisão: a empresa pode evitá-los mudando a operação."),
  ("NBC TG 27", "16(c)", "A estimativa de desmontagem da planta e de restauração do local entra no custo do ativo, em contrapartida à provisão."),
  ("ITG 12", "—", "Revisões da estimativa de desmontagem/restauração ajustam o ativo e a provisão; a atualização pelo tempo é despesa financeira."),
  ("ITG 13", "—", "Participação em fundos de desativação ou recuperação ambiental fica separada da provisão, sem compensação."),
  ("ITG 15", "—", "Resíduos de equipamentos eletroeletrônicos: obrigação de custear a destinação conforme a participação de mercado."),
  ("CTG 10", "—", "Créditos de carbono, permissões de emissão e CBIO: classificação conforme o uso (estoque, intangível ou instrumento financeiro) e passivo pela obrigação de emissão."),
  ("NBC TDS 02", "—", "IFRS S2 (companhias abertas desde 2026): emissões de escopo 1 (combustão e processos da fábrica), 2 (energia comprada) e 3, riscos físicos e de transição, metas e análise de cenários."),
 ],
 ["Levantamento de passivos ambientais por planta (licenças, TACs, áreas contaminadas).",
  "Provisão de desmontagem e restauração para plantas com obrigação contratual ou legal.",
  "Inventário de emissões (GHG Protocol) se for companhia aberta ou exigido por clientes.",
  "Acompanhar o mercado regulado de carbono (SBCE, Lei 15.042/2024) para grandes emissores."]),

("09-setores-industriais", "Particularidades por tipo de indústria",
 "agroindústria, frigorífico, usina, papel e celulose, mineração, siderurgia, química, farmacêutica, eletroeletrônicos, bens de capital sob encomenda, incorporação de equipamentos",
 "Normas que só aparecem em alguns segmentos industriais.",
 [
  ("NBC TG 29", "—", "Agroindústria (usinas, celulose, frigoríficos com criação própria): ativo biológico e produto agrícola a valor justo até a colheita; daí em diante o produto segue a NBC TG 16. Plantas portadoras (cana-de-açúcar, café, laranjais) são imobilizado."),
  ("ITG 18", "—", "Mineração a céu aberto: remoção de estéril na fase de produção vira ativo quando melhora o acesso ao minério."),
  ("IFRS 6", "—", "Exploração e avaliação de recursos minerais: sem CPC equivalente; empresas brasileiras costumam seguir a política anterior com teste de impairment."),
  ("NBC TG 47", "35", "Bens de capital sob encomenda (máquinas especiais, estruturas): receita ao longo do tempo quando não há uso alternativo e existe direito de receber pelo que foi executado."),
  ("NBC TG 04", "57", "Química e farmacêutica: desenvolvimento de produto só é ativo com os 6 critérios (na prática, raramente antes da aprovação regulatória)."),
  ("ITG 15", "—", "Eletroeletrônicos: obrigação de logística reversa de resíduos."),
 ],
 ["Identificar quais normas setoriais se aplicam à planta antes de fechar o balanço."]),

("10-auditoria-na-industria", "Auditoria na indústria",
 "inventário físico, contagem de estoques, estoque em poder de terceiros, industrialização por encomenda, provisão de obsolescência, custo de produção, laudos de máquinas",
 "Onde o auditor independente mais concentra trabalho numa indústria.",
 [
  ("NBC TA 501", "4–7", "Estoque relevante: o auditor acompanha a contagem física (observa procedimentos, faz contagens de teste, verifica itens obsoletos e o corte), inclusive quando a contagem não é na data do balanço."),
  ("NBC TA 501", "8", "Estoque em poder de terceiros (armazém geral, industrialização por encomenda, consignação): confirmação com o terceiro ou inspeção."),
  ("NBC TA 315", "—", "Entender o sistema de custeio, o ERP, os critérios de rateio e os controles de produção para avaliar riscos."),
  ("NBC TA 540", "—", "Estimativas mais auditadas: provisão para obsolescência e VRL, vida útil das máquinas, provisão de garantias, impairment da planta e provisões ambientais."),
  ("NBC TA 505", "—", "Confirmações externas de saldos com fornecedores, clientes e estoques de terceiros."),
  ("NBC TA 520", "—", "Procedimentos analíticos: margem por produto, giro de estoque, custo unitário x histórico, ociosidade."),
  ("NBC TA 620", "—", "Uso de especialistas: avaliadores de máquinas, engenheiros (vida útil, estágio de obras), atuários, especialistas ambientais."),
 ],
 ["Programar a contagem física com o auditor e preparar instruções de inventário.",
  "Documentar a capacidade normal, os rateios e as variações de custo-padrão.",
  "Base de cálculo da obsolescência e da provisão de garantia pronta para revisão."]),
]

FAQ = [
 ("A ociosidade da fábrica entra no custo do produto?", "Não. CIF fixos são rateados pela capacidade normal; o que sobra é despesa do período.", "NBC TG 16", "13"),
 ("Frete de compra de matéria-prima é custo?", "Sim, entra no custo do estoque. Frete na venda é despesa de venda.", "NBC TG 16", "11 e 16"),
 ("ICMS e IPI entram no custo do estoque?", "Só a parte não recuperável. Créditos ficam em tributos a recuperar.", "NBC TG 16", "11"),
 ("Posso usar custeio variável no balanço?", "Não. As demonstrações exigem absorção; custeio variável é só gerencial.", "NBC TG 16", "12–13"),
 ("Custo-padrão é aceito?", "Sim, se ficar próximo do real e os padrões forem revistos.", "NBC TG 16", "21"),
 ("Posso usar UEPS?", "Não. Só PEPS ou custo médio ponderado.", "NBC TG 16", "25"),
 ("Peça de reposição é estoque ou imobilizado?", "Imobilizado se usada por mais de um período (sobressalente estratégico); senão, almoxarifado.", "NBC TG 27", "8"),
 ("Grande parada de manutenção vai para despesa?", "Pode ser capitalizada como componente e depreciada até a próxima parada.", "NBC TG 27", "14"),
 ("Depreciação da máquina de produção é despesa?", "Não diretamente: é custo de produção (CIF) e passa pelo estoque.", "NBC TG 27", "49"),
 ("Posso usar a taxa de depreciação da Receita?", "Só se refletir a vida útil econômica; a diferença com o fiscal gera IR diferido.", "NBC TG 27", "50–51"),
 ("Juros do financiamento da fábrica nova?", "Capitalizados durante a construção.", "NBC TG 20", "8"),
 ("Quando reconhecer a receita de exportação FOB?", "Quando o controle passa ao cliente, em geral no embarque.", "NBC TG 47", "38"),
 ("Bonificação e rebate a cliente são despesa de venda?", "Não; reduzem a receita (contraprestação variável).", "NBC TG 47", "50–59"),
 ("Garantia do produto é provisão ou receita diferida?", "Garantia legal/padrão = provisão; garantia estendida vendida = receita diferida.", "NBC TG 47", "B28–B33"),
 ("Incentivo de ICMS (crédito presumido) vai para onde?", "Resultado como subvenção, com possível destinação à reserva de incentivos fiscais.", "NBC TG 07", "12"),
 ("Variação cambial da importação de insumo entra no custo?", "Não; vai para o resultado financeiro.", "NBC TG 02", "28"),
 ("Gasto com protótipo vira ativo?", "Só na fase de desenvolvimento e se cumprir os 6 critérios.", "NBC TG 04", "57"),
 ("Preciso provisionar área contaminada?", "Sim, se a obrigação já existe (legal ou não formalizada) e for provável o desembolso.", "NBC TG 25", "14, 19"),
]


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def gerar(root, REC, sem_rev):
    por_cod = {sem_rev(r["codigo"]): r for r in REC}
    falta = sorted({c for t in TOPICOS for c, _, _ in t[4] if c not in por_cod} |
                   {c for _, _, c, _ in FAQ if c not in por_cod})
    assert not falta, f"normas do tópico industrial não encontradas: {falta}"
    for r in REC:
        r["industria"] = []

    pasta = root / "Industrial"
    shutil.rmtree(pasta, ignore_errors=True)
    pasta.mkdir()

    def cab(r):
        cpc = f"[{r['cpc']}]({r['url_cpc']})" if r.get("url_cpc") else r["cpc"]
        refs = " · ".join(x for x in (cpc, r["internacional"]) if x)
        return f"### {r['codigo']} – {r['titulo']}" + (f" ({refs})" if refs else "") + f" · [texto oficial]({r['url']})"

    for arq, titulo, usar, intro, pontos, check in TOPICOS:
        md = [f"# Indústria: {titulo}\n", f"**Use para:** {usar}.\n", intro + "\n", AVISO + "\n"]
        ordem = []
        for c, _, _ in pontos:
            if c not in ordem:
                ordem.append(c)
        for c in ordem:
            r = por_cod[c]
            md.append("\n" + cab(r) + "\n\n| Item | O que diz para a indústria |\n|---|---|")
            for c2, itens, txt in pontos:
                if c2 == c:
                    md.append(f"| {itens} | {txt} |")
                    r["industria"].append({"topico": titulo, "arquivo": f"Industrial/{arq}.md", "itens": itens, "ponto": txt})
        md.append("\n## Checklist na prática\n")
        md += [f"- [ ] {x}" for x in check]
        md.append("\n[← Índice da indústria](README.md) · [Todas as áreas](../areas/README.md)")
        (pasta / f"{arq}.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    idx = ["# Normas para a indústria\n",
           "Trechos das normas contábeis e de auditoria que importam para empresas industriais, "
           "organizados pelo ciclo da fábrica: compra de insumos → produção → estoque → venda → pós-venda. "
           "Cada arquivo traz, por norma, os itens relevantes e o que eles dizem na prática, mais um checklist.\n",
           AVISO + "\n",
           "## Por etapa do ciclo industrial\n\n| Tópico | Use para | Normas |\n|---|---|---|"]
    for arq, titulo, usar, _, pontos, _ in TOPICOS:
        cods = []
        for c, _, _ in pontos:
            if por_cod[c]["codigo"] not in cods:
                cods.append(por_cod[c]["codigo"])
        idx.append(f"| [{titulo}]({arq}.md) | {usar} | {', '.join(cods)} |")
    idx.append("\n## Perguntas frequentes\n\n| Pergunta | Resposta curta | Norma (item) |\n|---|---|---|")
    for p, resp, c, it in FAQ:
        r = por_cod[c]
        rotulo = "itens" if re.search(r"[–,]| e ", it) else "item"
        idx.append(f"| {p} | {resp} | [{r['codigo']}]({r['url']}) ({rotulo} {it}) |")
    idx.append("\n[Todas as áreas](../areas/README.md) · [Índice geral](../README.md)")
    (pasta / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    return [(arq, titulo) for arq, titulo, *_ in TOPICOS]
