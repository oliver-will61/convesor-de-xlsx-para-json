import pandas as pd

# Carrega a planilha Excel
df = pd.read_excel('./planilha.xlsx')

# Converte o DataFrame para JSON com caracteres especiais corretos
json_data = df.to_json(orient='records', force_ascii=False, indent=4)

# Salva o JSON em um arquivo
with open('resultado.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

print("Conversão concluída! JSON salvo como 'resultado.json'.")
