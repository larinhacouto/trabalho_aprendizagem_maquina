import pandas as pd
import sys

# Questão 1:
# Ajuste as idades que não são válidas ou estão vazias para a moda da amostra. Grave a saída no arquivo Resposta01.txt

# Tenta ler o arquivo CSV
try:
    data = pd.read_csv('data/titanic.csv')
except FileNotFoundError as e:
    print(f"Erro: O arquivo 'titanic.csv' não foi encontrado.")
    sys.exit()

# Calcula a moda da idade
moda_idade = data['age'].mode()[0]

# Preenche os valores em branco na coluna 'age' com a moda
data['age'].fillna(moda_idade, inplace=True)

# Salva os dados ajustados no arquivo 'Resposta01.txt'
data.to_csv('Resposta01.txt', index=False)

# Confirmação de que a operação foi concluída
print("Os valores de idade inválidos foram ajustados e o resultado foi salvo em 'Resposta01.txt'.")
