# Como contribuir

Achou link quebrado, norma nova ou revisada, ou um resumo errado? Há dois caminhos.

## 1. Abrir uma issue (não precisa saber programar)

Em **Issues → New issue**, escolha o modelo: *Link quebrado*, *Norma nova ou revisada* ou *Correção de conteúdo*.
Informe a norma, o item e, se possível, o link oficial.

## 2. Propor a alteração (pull request)

1. Edite a planilha certa em [`dados/`](dados/README.md). Ela abre no Excel; salve como **CSV UTF-8 com ponto e vírgula**.
2. Abra um *pull request*. O mantenedor revisa e aprova; ninguém altera o repositório sem essa aprovação.
3. Depois da aprovação, o GitHub Actions regenera README, áreas, pastas por setor, grafo e mapa.

Não edite à mão os arquivos gerados (`README.md`, `areas/`, pastas por setor, `normas.json`, `graphify-out/`): eles são sobrescritos.

## Regras de conteúdo

- Cite sempre a norma, o item e o link oficial (CFC, CPC, BCB, CVM ou SUSEP).
- Resuma com suas palavras: não copie o texto das normas (direitos autorais).
- Indique se a norma foi revogada e por qual.
