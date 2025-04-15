import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def carregar_dados():
    """
    Carrega o arquivo CSV com os dados dos estudantes.
    Retorna um DataFrame com os dados carregados.
    """
    while True:
        caminho = input("Digite o caminho completo do arquivo CSV: ").strip()
        
        if not Path(caminho).exists():
            print("Arquivo não encontrado. Por favor, tente novamente.")
            continue
            
        try:
            dados = pd.read_csv(caminho)
            print("\nDados carregados com sucesso!")
            return dados
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}. Por favor, tente novamente.")


def resumo_estatistico(dados):
    """
    Exibe um resumo estatístico dos dados carregados.
    """
    print("\n=== RESUMO ESTATÍSTICO ===")
    print(f"Total de registros carregados: {len(dados)}")
    
    if 'genero' in dados.columns:
        print("\nQuantidade por gênero:")
        print(dados['genero'].value_counts())
    
    if 'Parent_Education' in dados.columns:
        nulos = dados['Parent_Education'].isna().sum()
        print(f"\nRegistros sem dados sobre educação dos pais: {nulos}")


def limpeza_dados(dados):
    """
    Realiza a limpeza dos dados conforme especificado.
    Retorna o DataFrame com os dados limpos.
    """
    dados = dados.copy()  # Cria uma cópia dos dados para evitar modificações no original
    print("\n=== LIMPEZA DE DADOS ===")
    
    # Remover registros com educação dos pais vazios
    if 'Parent_Education' in dados.columns:
        original = len(dados)
        dados = dados.dropna(subset=['Parent_Education'])
        removidos = original - len(dados)
        print(f"\nRemovidos {removidos} registros com educação dos pais vazia.\n")
    
    # Preencher frequência nula com mediana (usando Attendance)
    if 'Attendance' in dados.columns:
        mediana = dados['Attendance'].median()
        nulos = dados['Attendance'].isna().sum()
        dados.loc['Attendance'] = dados['Attendance'].fillna(mediana)
        print(f"\nPreenchidos {nulos} valores nulos em 'Attendance' com a mediana: {mediana:.2f}")
        print(f"Somatório de frequência: {dados['Attendance'].sum():.2f}")
        print("\n *DADOS LIMPOS COM SUCESSO.*")
        
    return dados


def consulta_estatisticas(dados):
    """
    Permite ao usuário consultar estatísticas das colunas numéricas.
    """
    print("\n=== CONSULTA DE ESTATÍSTICAS ===")
    
    colunas_numericas = dados.select_dtypes(include=['number']).columns
    
    if len(colunas_numericas) == 0:
        print("Nenhuma coluna numérica encontrada.")
        return
    
    print("Colunas numéricas disponíveis:")
    for i, coluna in enumerate(colunas_numericas, 1):
        print(f"{i}. {coluna}")
    
    while True:
        try:
            escolha = input("\nDigite o número da coluna (ou 'sair'): ").strip().lower()
            if escolha == 'sair':
                break
                
            escolha = int(escolha) - 1
            if escolha < 0 or escolha >= len(colunas_numericas):
                print("Número inválido. Tente novamente.")
                continue
                
            coluna = colunas_numericas[escolha]
            print(f"\nEstatísticas para '{coluna}':")
            print(f"Média: {dados[coluna].mean():.2f}")
            print(f"Mediana: {dados[coluna].median():.2f}")
            print(f"Moda: {dados[coluna].mode().values[0]:.2f}")
            print(f"Desvio padrão: {dados[coluna].std():.2f}")
            
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")


def gerar_graficos(dados):
    """
    Gera os gráficos especificados a partir dos dados.
    """
    print("\n=== GERANDO GRÁFICOS ===")
    
    # Gráfico de dispersão: horas de sono x nota final
    if 'horas_sono' in dados.columns and 'nota_final' in dados.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(dados['horas_sono'], dados['nota_final'], alpha=0.6)
        plt.title('Relação entre Horas de Sono e Nota Final')
        plt.xlabel('Horas de Sono por Noite')
        plt.ylabel('Nota Final')
        plt.grid(True)
        plt.show()
    
    # Gráfico de barras: idade x média das notas parciais (usando Midterm_Score)
    if 'idade' in dados.columns and 'Midterm_Score' in dados.columns:
        plt.figure(figsize=(10, 6))
        dados.groupby('idade')['Midterm_Score'].mean().plot(kind='bar')
        plt.title('Média das Notas Parciais por Idade')
        plt.xlabel('Idade')
        plt.ylabel('Média das Notas Parciais (Midterm)')
        plt.grid(True)
        plt.show()
    
    # Gráfico de pizza: distribuição por faixa etária
    if 'idade' in dados.columns:
        plt.figure(figsize=(8, 8))
        bins = [0, 17, 21, 24, 100]
        labels = ['Até 17', '18 a 21', '21 a 24', '25 ou mais']
        dados['faixa_etaria'] = pd.cut(dados['idade'], bins=bins, labels=labels, right=False)
        contagem = dados['faixa_etaria'].value_counts()
        contagem.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição por Faixa Etária')
        plt.ylabel('')
        plt.show()


def main():
    """Função principal que executa o programa."""
    print("=== ANALISADOR DE DADOS DE ESTUDANTES ===")
    
    # Carregar dados
    dados = carregar_dados()
    
    # Exibir resumo estatístico
    resumo_estatistico(dados)
    
    # Limpeza de dados
    dados_limpos = limpeza_dados(dados)
    
    # Consulta de estatísticas
    consulta_estatisticas(dados_limpos)
    
    # Gerar gráficos
    gerar_graficos(dados_limpos)
    
    print("\nAnálise concluída com sucesso!")


if __name__ == "__main__":
    main()