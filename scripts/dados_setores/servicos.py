# Setor: Serviços. Formato: ver scripts/gerar_setores.py.
NOME = "Serviços"
PASTA = "Servicos"
USE_PARA = ("receita de serviços e contratos, SaaS e licenças, comissões de venda, projetos, pessoal (férias, 13º, PLR), "
            "stock options, software, escritórios alugados, ISS, pequenas empresas de serviço")
INTRO = ("Trechos das normas que importam para prestadores de serviço: consultorias, escritórios, tecnologia e SaaS, "
         "saúde, educação, agências, logística e serviços em geral. O centro é a receita (NBC TG 47) e as pessoas (NBC TG 33).")

TOPICOS = [
("01-receita-de-servicos", "Receita de serviços e contratos",
 "contratos com clientes, obrigações de desempenho, receita ao longo do tempo, medição do progresso, pacotes de serviços, aditivos, multas e bônus",
 "Em serviços a receita costuma ser reconhecida ao longo do tempo. O ponto é identificar o que foi prometido e como medir o avanço.",
 [
  ("NBC TG 47", "22–30", "Separar o contrato em obrigações de desempenho: implantação, suporte e treinamento podem ser obrigações distintas, cada uma com sua receita."),
  ("NBC TG 47", "35", "Receita ao longo do tempo quando o cliente recebe e consome o serviço enquanto é prestado (ex.: suporte mensal, limpeza, vigilância) ou quando não há uso alternativo e há direito de receber pelo que foi feito (ex.: projeto sob medida)."),
  ("NBC TG 47", "39–45", "Medir o progresso por método de produto (entregas, marcos) ou de insumo (horas, custos incorridos), o que melhor representar a transferência do serviço."),
  ("NBC TG 47", "B16", "Expediente prático: se o direito a receber corresponde ao valor do serviço prestado até a data (ex.: horas faturáveis), reconhecer receita pelo valor faturável."),
  ("NBC TG 47", "50–59", "Bônus de desempenho, multas por SLA e descontos por volume são contraprestação variável: estimar e só reconhecer o que não tiver risco relevante de reversão."),
  ("NBC TG 47", "18–21", "Aditivos de escopo ou preço: modificação de contrato; pode virar contrato separado ou ajuste do contrato existente."),
  ("NBC TG 47", "B34–B38", "Agências e intermediadores (viagens, mídia, mão de obra terceirizada): se não controlam o serviço antes da entrega ao cliente, são agentes e a receita é a comissão."),
 ],
 ["Mapear obrigações de desempenho dos contratos padrão.",
  "Definir o método de medição do progresso por tipo de serviço.",
  "Provisionar multas por SLA como redução de receita."]),

("02-saas-software-e-licencas", "SaaS, software e licenças",
 "assinaturas SaaS, licenças de software, implantação, custo de comissão de vendas, desenvolvimento de software, custos de nuvem",
 "Empresas de tecnologia: quando a assinatura vira receita, o que fazer com a comissão do vendedor e quando o software desenvolvido internamente vira ativo.",
 [
  ("NBC TG 47", "B52–B63", "Licença de propriedade intelectual: direito de acessar (receita ao longo do tempo, típico de SaaS) ou direito de usar como está (receita no momento da entrega da licença)."),
  ("NBC TG 47", "B48–B51", "Taxa de implantação ou adesão não reembolsável: se não transfere um serviço distinto, é adiantamento e vira receita ao longo da assinatura."),
  ("NBC TG 47", "91–94", "Comissão de venda paga só quando o contrato é fechado (custo incremental) vira ativo e é amortizada pelo prazo esperado do cliente; pode ir direto para despesa se a amortização for de até 1 ano (item 94)."),
  ("NBC TG 47", "95–98", "Custos para cumprir o contrato (ex.: preparação de ambiente) viram ativo só se não estiverem no alcance de outra norma, gerarem recursos para cumprir o contrato e forem recuperáveis."),
  ("NBC TG 04", "57", "Software desenvolvido internamente: só a fase de desenvolvimento vira intangível, e só se cumprir os 6 critérios (viabilidade técnica, intenção, capacidade de usar/vender, benefícios, recursos e mensuração)."),
  ("NBC TG 04", "54–56", "Pesquisa, prova de conceito e avaliação de alternativas tecnológicas são despesa."),
 ],
 ["Classificar cada produto: acesso (SaaS) x uso (licença).",
  "Ativar comissões de venda incrementais e definir prazo de amortização.",
  "Controle de horas por projeto de software com marco do início da fase de desenvolvimento.",
  "Custos de configuração de software de terceiros em nuvem: em regra despesa, salvo se gerarem ativo controlado pela empresa."]),

("03-pessoal-e-beneficios", "Pessoal, férias, PLR e stock options",
 "folha, férias, 13º salário, encargos, PLR, bônus, plano de saúde, previdência privada, stock options, phantom shares",
 "Em serviços a folha é o principal custo. A NBC TG 33 manda provisionar no mês em que o empregado presta o serviço.",
 [
  ("NBC TG 33", "11", "Benefícios de curto prazo (salários, encargos, 13º) reconhecidos como despesa ou custo à medida que o serviço é prestado, com passivo do que ainda não foi pago."),
  ("NBC TG 33", "13–15", "Férias (ausências remuneradas acumuláveis): provisionar mês a mês, com encargos, conforme o empregado adquire o direito."),
  ("NBC TG 33", "19–24", "PLR e bônus: provisionar quando houver obrigação presente (legal, por acordo/convenção ou prática) e o valor puder ser estimado."),
  ("NBC TG 33", "—", "Planos de saúde pós-emprego e previdência com benefício definido exigem cálculo atuarial; contribuição definida é despesa do período."),
  ("NBC TG 10", "—", "Stock options e ações restritas: despesa pelo valor justo na outorga ao longo do período de aquisição; phantom shares pagas em dinheiro geram passivo remensurado."),
  ("NBC TG 25", "14", "Processos trabalhistas: provisão quando a perda for provável e estimável; possíveis só em nota."),
 ],
 ["Provisão mensal de férias e 13º com encargos.",
  "Provisão de PLR conforme acordo coletivo e metas do período.",
  "Planilha de stock options/phantom shares com valor justo e período de aquisição."]),

("04-escritorios-tributos-e-pequenas", "Escritórios, tributos e pequenas empresas",
 "aluguel de escritório e equipamentos, ISS, PIS/COFINS, Simples Nacional, microempresa, pequena empresa, NBC TG 1001/1002",
 "Muitos prestadores de serviço são pequenos e podem usar as normas simplificadas.",
 [
  ("NBC TG 06", "22–24", "Escritórios e equipamentos alugados por mais de 12 meses: direito de uso + passivo de arrendamento."),
  ("NBC TG 06", "5–8", "Isenção para contratos curtos (até 12 meses) e ativos de baixo valor (notebooks, celulares)."),
  ("NBC TG 47", "47", "ISS e demais tributos sobre o faturamento são deduções da receita bruta, não receita."),
  ("NBC TG 1002", "—", "Microentidade (receita bruta até R$ 4,8 milhões/ano): conjunto mínimo de demonstrações e regras simplificadas."),
  ("NBC TG 1001", "—", "Pequena empresa (receita bruta acima de R$ 4,8 milhões até R$ 78 milhões/ano): contabilidade simplificada."),
  ("ITG 2000", "—", "Escrituração contábil regular é obrigatória mesmo no Simples Nacional (livro Diário, documentação, guarda)."),
 ],
 ["Enquadrar a empresa na norma certa pelo faturamento (NBC TG 1002, 1001, 1000 ou completas).",
  "Escrituração completa mesmo no Simples Nacional.",
  "Levantar contratos de aluguel de escritório e equipamentos."]),
]

FAQ = [
 ("Contrato mensal de suporte: receita quando?", "Ao longo do tempo, à medida que o serviço é prestado.", "NBC TG 47", "35"),
 ("Projeto de consultoria por horas: posso reconhecer pelo faturável?", "Sim, se o direito a receber corresponder ao serviço prestado até a data.", "NBC TG 47", "B16"),
 ("Assinatura SaaS é receita na venda?", "Não; é direito de acesso, receita ao longo da assinatura.", "NBC TG 47", "B52–B63"),
 ("Taxa de implantação vira receita na hora?", "Só se transferir um serviço distinto; senão, ao longo do contrato.", "NBC TG 47", "B48–B51"),
 ("Comissão do vendedor pode virar ativo?", "Sim, se incremental e recuperável; pode ir para despesa se amortizaria em até 1 ano.", "NBC TG 47", "91–94"),
 ("Software próprio vira intangível?", "Só na fase de desenvolvimento e cumprindo os 6 critérios.", "NBC TG 04", "57"),
 ("Preciso provisionar férias todo mês?", "Sim, conforme o empregado adquire o direito, com encargos.", "NBC TG 33", "13–15"),
 ("PLR é provisionada quando?", "Quando houver obrigação presente e valor estimável.", "NBC TG 33", "19–24"),
 ("ISS é receita?", "Não; deduz a receita bruta.", "NBC TG 47", "47"),
 ("Empresa do Simples precisa de contabilidade?", "Sim, escrituração regular conforme ITG 2000.", "ITG 2000", "—"),
]
