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
    
    if 'educacao_pais' in dados.columns:
        nulos = dados['educacao_pais'].isna().sum()
        print(f"\nRegistros sem dados sobre educação dos pais: {nulos}")


def limpeza_dados(dados):
    """
    Realiza a limpeza dos dados conforme especificado.
    Retorna o DataFrame com os dados limpos.
    """
    print("\n=== LIMPEZA DE DADOS ===")
    
    # Remover registros com educação dos pais vazios
    if 'educacao_pais' in dados.columns:
        original = len(dados)
        dados = dados.dropna(subset=['educacao_pais'])
        removidos = original - len(dados)
        print(f"Removidos {removidos} registros com educação dos pais vazia.")
    
    # Preencher frequência nula com mediana
    if 'frequencia' in dados.columns:
        mediana = dados['frequencia'].median()
        nulos = dados['frequencia'].isna().sum()
        dados['frequencia'] = dados['frequencia'].fillna(mediana)
        print(f"Preenchidos {nulos} valores nulos em 'frequencia' com a mediana: {mediana:.2f}")
        print(f"Somatório de frequência: {dados['frequencia'].sum():.2f}")
    
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

if __name__ == "__main__":
    main()