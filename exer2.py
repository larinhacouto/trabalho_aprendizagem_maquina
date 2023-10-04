import pandas as pd
import sys

# Questão 2:
# Apresente no terminal o somatório de homens (male) e de mulheres (female)

# Tenta ler o arquivo CSV
try:
    data = pd.read_csv('titanic.csv')
except FileNotFoundError as e:
    print(f"Erro: O arquivo 'titanic.csv' não foi encontrado.")
    sys.exit()

homens = (data['sex'] == 'male').sum()
mulheres = (data['sex'] == 'female').sum()

# Apresenta os resultados no terminal
print(f"Total de Homens: {homens}")
print(f"Total de Mulheres: {mulheres}")
