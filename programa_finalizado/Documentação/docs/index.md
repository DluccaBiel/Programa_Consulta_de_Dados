# Analisador de Dados de Estudantes

Bem-vindo ao **Analisador de Dados de Estudantes**!

Este projeto visa analisar dados de estudantes para gerar estatísticas sobre suas notas, presença, gênero, e a educação de seus pais. Você pode carregar arquivos de dados no formato CSV ou JSON e visualizar gráficos e estatísticas detalhadas.

## Funcionalidades

- **Carregamento de dados**: O sistema permite o carregamento de arquivos CSV ou JSON com dados de estudantes.
- **Resumo estatístico**: O sistema fornece um resumo estatístico dos dados carregados, incluindo a quantidade de registros, a distribuição por gênero, e a quantidade de registros com dados ausentes sobre a educação dos pais.
- **Limpeza de dados**: O programa realiza a limpeza dos dados, removendo registros com dados faltantes e preenchendo valores nulos com a mediana de outras colunas.
- **Consulta a dados**: Você pode consultar a média, mediana, moda e desvio padrão de diferentes colunas numéricas.
- **Gráficos**: São gerados gráficos de dispersão, barras e pizza para visualizar a relação entre diferentes variáveis.

## Como usar

1. Carregue os dados usando a função `carregar_dados()`.
2. Veja o resumo estatístico dos dados com `resumo_estatistico(dados)`.
3. Realize a limpeza dos dados com `limpeza_dados(dados)`.
4. Consulte estatísticas das colunas com `consulta_estatisticas(dados)`.
5. Visualize os gráficos com `gerar_graficos(dados)`.

Abaixo você pode consultar o código-fonte do projeto.

---

Para mais detalhes sobre a implementação, veja a [documentação do código](codigo.md).
