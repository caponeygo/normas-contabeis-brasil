# Planilhas de dados

Tudo o que aparece no índice (README, `areas/`, pastas por setor, `normas.json`, grafo e mapa) é gerado a partir
destas planilhas. **Para corrigir ou acrescentar algo, edite aqui** e não nos arquivos gerados.

## Como editar

1. Abra o arquivo `.csv` no Excel (ou LibreOffice). As colunas são separadas por **ponto e vírgula** e o arquivo está
   em UTF-8, então os acentos aparecem corretos.
2. Edite e salve mantendo o formato **CSV UTF-8 (delimitado por ponto e vírgula)**. No Excel: *Salvar como → CSV UTF-8*.
   Se o Excel salvar com vírgula, confira em *Configurações regionais* que o separador de lista é `;`.
3. Envie a alteração para o GitHub (pelo site: abra o arquivo → ícone de lápis, ou *Add file → Upload files*).
4. O GitHub Actions regenera tudo sozinho em 1 ou 2 minutos (workflow **Gerar índice**). Para gerar no seu computador:
   `python graphify-out/rebuild_graph.py`.

Uma célula pode ter várias linhas (ex.: `checklist`): no Excel use **Alt+Enter** para quebrar a linha.

## Arquivos

| Planilha | Uma linha por… | Colunas |
|---|---|---|
| `normas.csv` | norma | `codigo`, `titulo`, `secao` (ver `secoes.csv`), `cpc`, `internacional` (IFRS/IAS/ISA; nas IFRS, a NBC TG equivalente), `url` (link oficial), `situacao` (vazio = vigente; texto = motivo da revogação), `resumo` (o que trata), `afeta` (BP, DRE, DFC… ou o tipo de trabalho). IFRS/IAS sem resumo herdam o da NBC TG equivalente. |
| `secoes.csv` | seção do README | `secao` (código curto), `titulo`, `formato` (`tg`, `itg`, `ta`, `simples` ou `ifrs`: define as colunas da tabela), `serie` (série atribuída às normas da seção; `(prefixo do código)` usa a primeira palavra do código), `intro` |
| `areas.csv` | área | `area`, `use_para` (quando usar a área), `series` (séries cuja área principal é esta, separadas por vírgula) |
| `temas.csv` | tema de busca | `tema`, `area`, `regex` (padrão procurado no título da norma), `sinonimos`, `normas_extras` (normas incluídas no tema mesmo sem o padrão no título), `so_auditoria` (`sim` = só vale para normas de auditoria/profissão) |
| `setores.csv` | setor | `setor` (código), `nome`, `pasta`, `use_para`, `intro` |
| `setores_topicos.csv` | tópico (um arquivo `.md` na pasta do setor) | `setor`, `arquivo`, `titulo`, `use_para`, `intro`, `checklist` (um item por linha) |
| `setores_pontos.csv` | trecho de norma num tópico | `setor`, `arquivo` (do tópico), `norma` (código sem a revisão, ex.: `NBC TG 16`), `itens` (ex.: `10–11`, `B28–B33`, `—`), `ponto` (o que diz para o setor) |
| `setores_faq.csv` | pergunta frequente | `setor`, `pergunta`, `resposta`, `norma`, `itens` |
| `setores_externas.csv` | regra de fora do CFC citada num setor | `setor`, `codigo` (ex.: `Res. CMN 4.966/2021`), `titulo`, `url`, `nota` |
| `fontes_externas.csv` | lei ou regra de fora do CFC/CPC citada nos textos | `codigo`, `padrao` (como aparece no texto, em regex), `titulo`, `url`: vira link na seção **Fontes** de cada página |
| `revisao_manual.csv` | trecho conferido à mão | `norma`, `itens`, `data`: trechos que a checagem automática marcou para conferir e que foram lidos no texto oficial e estão corretos |

## Regras que o gerador confere

- Toda norma de `normas.csv` precisa de `secao` existente e de `resumo` (próprio ou herdado).
- Toda `norma` citada em `setores_pontos.csv` e `setores_faq.csv` precisa existir em `normas.csv` (sem a revisão) ou em `setores_externas.csv`.
- Se algo estiver errado, o workflow **Gerar índice** falha e mostra a mensagem: corrija a planilha e envie de novo.

Depois de mudar itens ou resumos, a verificação semanal (`scripts/verificar_itens.py`) confere os números de item no texto oficial.
