Descrição: Esta função permite que o usuário carregue um arquivo CSV com os dados dos estudantes. A função pede o caminho do arquivo e, se o arquivo for válido, ele é carregado em um DataFrame do pandas.

Parâmetros: Não possui parâmetros de entrada.

Retorno: Retorna um DataFrame contendo os dados carregados do arquivo CSV.

2. resumo_estatistico(dados)
python
Copiar
Editar
def resumo_estatistico(dados):
    """
    Exibe um resumo estatístico dos dados carregados.
    """
Descrição: Esta função exibe informações sobre os dados carregados, como o total de registros, a quantidade de homens e mulheres e o número de registros com dados ausentes sobre a educação dos pais.

Parâmetros:

dados: Um DataFrame contendo os dados carregados dos estudantes.

Retorno: Não possui retorno, mas exibe informações no console.

3. limpeza_dados(dados)
python
Copiar
Editar
def limpeza_dados(dados):
    """
    Realiza a limpeza dos dados conforme especificado.
    Retorna o DataFrame com os dados limpos.
    """
Descrição: Realiza a limpeza dos dados, removendo registros com dados faltantes sobre a educação dos pais e preenchendo valores nulos na coluna de "Attendance" com a mediana.

Parâmetros:

dados: Um DataFrame contendo os dados carregados dos estudantes.

Retorno: Retorna um DataFrame limpo, com os valores ausentes tratados.

4. consulta_estatisticas(dados)
python
Copiar
Editar
def consulta_estatisticas(dados):
    """
    Permite ao usuário consultar estatísticas das colunas numéricas.
    """
Descrição: Permite ao usuário consultar a média, mediana, moda e desvio padrão das colunas numéricas dos dados.

Parâmetros:

dados: Um DataFrame contendo os dados limpos.

Retorno: Exibe as estatísticas no console.

5. gerar_graficos(dados)
python
Copiar
Editar
def gerar_graficos(dados):
    """
    Gera os gráficos especificados a partir dos dados.
    """
Descrição: Gera gráficos de dispersão, barras e pizza para visualizar as relações entre as variáveis.

Parâmetros:

dados: Um DataFrame contendo os dados limpos.

Retorno: Exibe os gráficos gerados.

Estrutura do Projeto
O código está estruturado da seguinte forma:

Funções:

carregar_dados(): Carrega os dados do arquivo.

resumo_estatistico(dados): Exibe o resumo estatístico.

limpeza_dados(dados): Limpa os dados.

consulta_estatisticas(dados): Consulta estatísticas.

gerar_graficos(dados): Gera gráficos.

Bibliotecas:

pandas: Para manipulação dos dados.

matplotlib.pyplot: Para geração dos gráficos.

pathlib.Path: Para verificar a existência do arquivo.

Como usar
Carregar os dados: O usuário fornece o caminho de um arquivo CSV contendo os dados dos estudantes.

Gerar resumos estatísticos: Após o carregamento, um resumo estatístico é exibido.

Limpeza de dados: A função limpeza_dados() realiza a limpeza necessária para corrigir valores ausentes.

Consultas de estatísticas: O usuário pode consultar a média, mediana, moda e desvio padrão de qualquer coluna numérica.

Gerar gráficos: Gráficos de dispersão, barras e pizza são gerados para análise visual.

Este código permite realizar uma análise eficiente dos dados de estudantes, com foco na presença, notas e dados demográficos.

yaml
Copiar
Editar

---

### **Estrutura do Projeto**

Agora, o conteúdo deve estar assim na sua pasta **`docs/`**:

docs/ │ ├── index.md # Página inicial do seu projeto (explicação geral) ├── codigo.md # Documentação do código (explicação das funções) ├── mkdocs.yml # Arquivo de configuração do MkDocs

yaml
Copiar
Editar

---

### **Finalizando**

Depois de criar esses dois arquivos, você pode rodar o comando `mkdocs serve` no terminal para visualizar