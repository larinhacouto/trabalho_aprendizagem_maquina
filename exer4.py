import pandas as pd
import matplotlib.pyplot as plt
import sys

# Tenta ler o arquivo CSV
try:
    data = pd.read_csv('titanic.csv')
except FileNotFoundError as e:
    print(f"Erro: O arquivo 'titanic.csv' não foi encontrado.")
    sys.exit()

# Questão 4:
# Apresente o gráfico de dispersão da Idade pela Tarifa.

age = data['age']
fare = data['fare']

# Criamos um gráfico de dispersão
plt.scatter(age, fare, alpha=0.5)

# Definimos rótulos dos eixos e título
plt.xlabel('Idade')
plt.ylabel('Tarifa')
plt.title('Gráfico de Dispersão: Idade pela Tarifa')

# Mostra o gráfico
plt.grid(True)
plt.show()
