


def main ():
    import pandas as pd

    def menu():
        while True:
            coluna_nome = input('Digite o nome das coluna_nomes que deseja converter'
            '\n>> ')

            coluna_para_converter = []

            if  coluna_nome in df.columns:
                print("Coluna adicionada")
                coluna_para_converter.push(df['coluna_nome'])
                print(coluna_para_converter)
                break

            else:
                print("Erro: Coluna não encontrada!")
                continue

            

    df = pd.read_excel('./planilha.xlsx')

    menu()

    
            



main()