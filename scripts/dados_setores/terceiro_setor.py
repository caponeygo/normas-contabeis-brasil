# Setor: Terceiro setor (entidades sem finalidade de lucros), cooperativas e partidos. Formato: ver scripts/gerar_setores.py.
NOME = "Terceiro Setor"
PASTA = "TerceiroSetor"
USE_PARA = ("associações, fundações, ONGs, OSCIPs, entidades beneficentes, doações, subvenções e convênios, gratuidades, "
            "trabalho voluntário, superávit, patrimônio social, cooperativas, partidos políticos")
INTRO = ("Trechos das normas que importam para entidades sem finalidade de lucros (associações, fundações, institutos, "
         "entidades de saúde, educação e assistência social), cooperativas e partidos políticos.")

EXTERNAS = {
 "LC 187/2021": ("Certificação de entidades beneficentes (CEBAS) e imunidade de contribuições",
                 "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp187.htm", ""),
}

TOPICOS = [
("01-receitas-doacoes-e-subvencoes", "Doações, subvenções, convênios e gratuidades",
 "doações, contribuições, subvenções públicas, convênios e termos de parceria, recursos com restrição, gratuidades, imunidade e isenção, trabalho voluntário",
 "A ITG 2002 adapta as normas às entidades sem fins lucrativos. O ponto central é o regime de competência para doações e subvenções e a evidenciação das gratuidades.",
 [
  ("ITG 2002", "9", "Doações e subvenções recebidas para custeio e investimento são reconhecidas no resultado, observada a NBC TG 07 (confronto com as despesas que compensam)."),
  ("ITG 2002", "9A–9B", "Só subvenções concedidas em caráter particular entram na NBC TG 07. Imunidades tributárias não são subvenção e não viram receita."),
  ("ITG 2002", "11–12", "Enquanto não cumpridos os requisitos para ir ao resultado, a subvenção, contribuição ou incentivo registrado no ativo tem contrapartida em conta específica do passivo; receitas de convênios, parcerias e termos de fomento seguem esse controle."),
  ("ITG 2002", "10, 13, 16", "Receitas e despesas com e sem gratuidade são segregadas por atividade (educação, saúde, assistência social...); gratuidade concedida por prestação de serviço é registrada pelo valor efetivamente praticado."),
  ("ITG 2002", "19", "Trabalho voluntário é reconhecido pelo valor justo do serviço, como se tivesse havido o desembolso (receita e despesa)."),
  ("NBC TG 07", "12", "Subvenção governamental vai para o resultado ao longo do período em que a entidade incorre nas despesas que ela compensa."),
  ("LC 187/2021", "—", "Requisitos legais da certificação beneficente (CEBAS) e da imunidade de contribuições sociais: tema jurídico; a contabilidade deve evidenciar gratuidades e renúncia fiscal."),
 ],
 ["Controle por projeto/convênio: recursos recebidos, aplicados e a aplicar (passivo).",
  "Segregar receitas e despesas com e sem gratuidade por atividade.",
  "Mensurar e registrar o trabalho voluntário.",
  "Não registrar imunidade como receita; divulgar a renúncia fiscal em nota."]),

("02-demonstracoes-e-patrimonio-social", "Demonstrações, superávit e patrimônio social",
 "patrimônio social, superávit ou déficit, recursos com restrição, demonstração do resultado do período, DFC, notas explicativas",
 "As demonstrações seguem a estrutura comum com outra nomenclatura e mais divulgação sobre recursos e gratuidades.",
 [
  ("ITG 2002", "15", "Superávit ou déficit incorporado ao patrimônio social; a parte com restrição de aplicação fica em conta específica do patrimônio líquido."),
  ("ITG 2002", "18", "Doação patrimonial do instituidor (fundações) vai direto para o patrimônio social."),
  ("ITG 2002", "23", "No balanço, 'Capital' passa a ser 'Patrimônio Social'; nas demonstrações, 'lucro ou prejuízo' passa a ser 'superávit ou déficit'."),
  ("ITG 2002", "24", "Na demonstração do resultado, destacar as gratuidades concedidas e os serviços voluntários obtidos, com divulgação por atividade."),
  ("ITG 2002", "27", "Notas: contexto operacional, critérios de receitas e despesas (gratuidades, doações, subvenções), renúncia fiscal, subvenções recebidas e sua aplicação, recursos com restrição, entre outros."),
  ("NBC TG 1000", "—", "Entidades menores podem aplicar a NBC TG 1000 (PME) com as adaptações da ITG 2002."),
 ],
 ["Nomenclatura do terceiro setor nas demonstrações.",
  "Conciliação de recursos com restrição.",
  "Notas com subvenções, convênios e gratuidades por atividade."]),

("03-cooperativas", "Cooperativas",
 "ato cooperativo e não cooperativo, ingressos e dispêndios, sobras e perdas, quotas-partes, capital a restituir, reservas obrigatórias",
 "Cooperativas seguem a ITG 2004, com resultado segregado entre atos com cooperados e com terceiros.",
 [
  ("ITG 2004", "5–7", "Escrituração segregada em ato cooperativo e não cooperativo; a Demonstração de Sobras ou Perdas evidencia separadamente cada um, por atividade, produto ou serviço."),
  ("ITG 2004", "18–19", "Capital formado por quotas-partes; quotas de cooperados demitidos, eliminados ou excluídos vão para passivo (capital a restituir) assim que recebido o pedido ou deliberada a saída."),
  ("ITG 2004", "20–21", "Sobras à disposição da assembleia são conta de trânsito; distribuição prevista no estatuto é registrada no passivo no encerramento."),
  ("IFRIC 2", "—", "Referência internacional (ICPC 14): cotas são patrimônio só se a cooperativa puder recusar o resgate."),
 ],
 ["Segregar ato cooperativo e não cooperativo no plano de contas.",
  "Transferir para o passivo as quotas de cooperados que saíram."]),

("04-partidos-e-eleicoes", "Partidos políticos e eleições",
 "partidos políticos, campanhas eleitorais, candidatos, fundo partidário, FEFC, prestação de contas à Justiça Eleitoral",
 "Desde as eleições de 2026, a contabilidade de partidos e campanhas segue obrigatoriamente a NBC TPE 01.",
 [
  ("NBC TPE 01", "—", "Contabilidade aplicada a partidos políticos e eleições: escrituração, demonstrações e prestação de contas."),
  ("OT CFC 02/2026", "—", "Confirma a obrigatoriedade da NBC TPE 01 nos processos eleitorais a partir de 2026."),
 ],
 ["Aplicar a NBC TPE 01 na prestação de contas de campanha de 2026."]),
]

FAQ = [
 ("Doação recebida vai direto para o patrimônio?", "Em regra vai para o resultado (regime de competência); doação patrimonial do instituidor vai para o patrimônio social.", "ITG 2002", "9, 18"),
 ("Recurso de convênio ainda não aplicado é receita?", "Não; fica no passivo até cumprir os requisitos.", "ITG 2002", "11–12"),
 ("Imunidade tributária vira receita?", "Não; não é subvenção. Divulgar a renúncia fiscal.", "ITG 2002", "9B"),
 ("Trabalho voluntário é contabilizado?", "Sim, pelo valor justo do serviço.", "ITG 2002", "19"),
 ("Como se chama o lucro de uma ONG?", "Superávit (ou déficit), incorporado ao patrimônio social.", "ITG 2002", "15, 23"),
 ("Quota de cooperado que saiu continua no PL?", "Não; vai para capital a restituir no passivo.", "ITG 2004", "19"),
 ("Partido político segue qual norma?", "NBC TPE 01, obrigatória a partir das eleições de 2026.", "OT CFC 02/2026", "—"),
]
