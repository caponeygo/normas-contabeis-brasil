# Setor: Financeiro (bancos, instituições do Banco Central, seguradoras, fundos de pensão). Formato: ver scripts/gerar_setores.py.
NOME = "Financeiro"
PASTA = "Financeiro"
USE_PARA = ("bancos, cooperativas de crédito, fintechs, seguradoras, previdência complementar, Banco Central (COSIF, Res. CMN 4.966), "
            "SUSEP, CVM, perda esperada, instrumentos financeiros, contratos de seguro")
INTRO = ("Instituições financeiras, seguradoras e fundos de pensão seguem, nas demonstrações individuais, as regras do seu "
         "regulador (Banco Central, SUSEP, PREVIC), que convergem parcialmente com os CPCs. Esta pasta aponta onde cada "
         "regra está e o que muda em relação às NBC TG.")

BCB = "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo="
EXTERNAS = {
 "Res. CMN 4.966/2021": ("Instrumentos financeiros nas instituições autorizadas pelo Banco Central (conceitos da IFRS 9)",
                         BCB + "Resolu%C3%A7%C3%A3o%20CMN&numero=4966",
                         "Em vigor desde 1/1/2025. Substituiu, entre outras, a Res. CMN 2.682/1999 (provisão por níveis AA a H)."),
 "Res. BCB 352/2023": ("Procedimentos contábeis complementares à Res. CMN 4.966 (perda esperada, divulgações)",
                       BCB + "Resolu%C3%A7%C3%A3o%20BCB&numero=352", ""),
 "COSIF": ("Plano Contábil das Instituições do Sistema Financeiro Nacional",
           "https://www3.bcb.gov.br/aplica/cosif", ""),
 "Res. CVM 42/2021": ("Aprova o CPC 50 – Contratos de Seguro para companhias abertas",
                      "https://conteudo.cvm.gov.br/legislacao/resolucoes/resol042.html", ""),
 "SUSEP": ("Normas contábeis e de provisões técnicas das supervisionadas",
           "https://www.gov.br/susep/pt-br",
           "A SUSEP tem regime contábil próprio para as demonstrações individuais das supervisionadas. Confira no site da SUSEP a situação atual da recepção do CPC 50."),
}

TOPICOS = [
("01-bancos-e-instituicoes-do-bc", "Bancos e instituições do Banco Central",
 "COSIF, Res. CMN 4.966, modelo de negócios, custo amortizado, valor justo, perda esperada em estágios, ativo problemático, renegociação, hedge",
 "Desde 2025 as instituições do Banco Central aplicam a Res. CMN 4.966, que traz para o COSIF os conceitos da IFRS 9 (NBC TG 48), com regras próprias de perda esperada.",
 [
  ("Res. CMN 4.966/2021", "—", "Classificação de ativos financeiros pelo modelo de negócios e pelas características dos fluxos de caixa (custo amortizado, valor justo em outros resultados abrangentes, valor justo no resultado), perda esperada e contabilidade de hedge."),
  ("Res. BCB 352/2023", "—", "Detalha procedimentos da Res. CMN 4.966, como critérios e pisos de perda esperada e divulgações."),
  ("COSIF", "—", "Plano de contas e regras de escrituração obrigatórios para as instituições do sistema financeiro."),
  ("NBC TG 48", "5.5", "Referência IFRS 9 (perda esperada em 3 estágios) para as demonstrações consolidadas em IFRS e para empresas fora do sistema financeiro."),
  ("NBC TG 48", "4.1", "Classificação de ativos financeiros pelo modelo de negócios e pelos fluxos de caixa contratuais (teste de SPPI)."),
 ],
 ["Mapear diferenças entre as demonstrações COSIF (Res. CMN 4.966) e as consolidadas em IFRS.",
  "Documentar modelos de negócios e testes de fluxos de caixa por carteira.",
  "Modelo de perda esperada com estágios e pisos regulatórios."]),

("02-seguradoras-e-previdencia", "Seguradoras e previdência complementar",
 "contratos de seguro, IFRS 17, CPC 50, provisões técnicas, SUSEP, fundos de pensão, EFPC, planos de benefícios",
 "Seguros têm duas camadas: as regras da SUSEP nas demonstrações individuais e a NBC TG 50 (IFRS 17) nas companhias abertas.",
 [
  ("NBC TG 50", "—", "Contratos de seguro (IFRS 17): fluxos de caixa de cumprimento + margem contratual de serviço; obrigatório para companhias abertas desde 2023."),
  ("Res. CVM 42/2021", "—", "Aprovou o CPC 50 para as companhias abertas."),
  ("SUSEP", "—", "Demonstrações individuais das supervisionadas seguem as normas contábeis da SUSEP (provisões técnicas, teste de adequação de passivos)."),
  ("ITG 2001", "—", "Entidades fechadas de previdência complementar (fundos de pensão): demonstrações específicas por plano e gestão previdencial, assistencial e administrativa."),
  ("NBC TG 49", "—", "Demonstrações dos próprios planos de benefícios de aposentadoria."),
 ],
 ["Conciliar resultados SUSEP x NBC TG 50 nas seguradoras abertas.",
  "Fundos de pensão: demonstrações por plano conforme ITG 2001."]),

("03-instrumentos-financeiros-fora-do-sistema-financeiro", "Instrumentos financeiros nas empresas em geral",
 "aplicações financeiras, empréstimos, debêntures, perda esperada de clientes, antecipação de recebíveis, FIDC, derivativos, fintechs não reguladas pelo BC",
 "Empresas que não são instituições do Banco Central (inclusive muitas fintechs) seguem a NBC TG 48.",
 [
  ("NBC TG 48", "4.1", "Classificar aplicações e recebíveis pelo modelo de negócios e pelos fluxos de caixa contratuais."),
  ("NBC TG 48", "5.5.15", "Clientes e ativos contratuais: abordagem simplificada de perda esperada pela vida inteira."),
  ("NBC TG 48", "3.2.3–3.2.6", "Venda ou cessão de recebíveis só baixa o ativo se transferir substancialmente riscos e benefícios."),
  ("NBC TG 39", "—", "Separar passivo de patrimônio (ações resgatáveis, conversíveis) e regras de compensação."),
  ("NBC TG 40", "31–42", "Divulgar riscos de crédito, liquidez e mercado, com análise de sensibilidade."),
 ],
 ["Política de perda esperada para clientes (matriz por faixa de atraso).",
  "Análise de baixa x empréstimo em cessões de recebíveis e FIDC."]),
]

FAQ = [
 ("Banco usa a NBC TG 48 nas demonstrações individuais?", "Não diretamente: segue o COSIF e a Res. CMN 4.966 (com conceitos da IFRS 9).", "Res. CMN 4.966/2021", "—"),
 ("Desde quando vale a Res. CMN 4.966?", "1/1/2025.", "Res. CMN 4.966/2021", "—"),
 ("Seguradora aberta aplica IFRS 17?", "Sim, CPC 50/NBC TG 50 desde 2023 (Res. CVM 42/2021).", "Res. CVM 42/2021", "—"),
 ("Fintech sem autorização do BC segue o quê?", "As NBC TG (instrumentos financeiros pela NBC TG 48).", "NBC TG 48", "4.1"),
 ("Fundo de pensão segue qual norma?", "ITG 2001 (EFPC) e regras da PREVIC.", "ITG 2001", "—"),
]
