import pandas as pd
import matplotlib.pyplot as plt
import sys

# Tenta ler o arquivo CSV
try:
    data = pd.read_csv('data/titanic.csv')
except FileNotFoundError as e:
    print(f"Erro: O arquivo 'titanic.csv' não foi encontrado.")
    sys.exit()

# Questão 3:
# Considerando a coluna "survived", sendo 0 como não sobrevivente e 1 como sobrevivente, apresente em um gráfico de pizza a porcentagem de sobreviventes e não sobreviventes.

survived = (data['survived'] == 1).sum()
n_survived = (data['survived'] == 0).sum()

# Criação do gráfico de pizza
plt.figure(figsize=(6, 6))
labels = ['Sobreviventes', 'Não Sobreviventes']
sizes = [survived, n_survived]
colors = ['green', 'red']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.title('Porcentagem de Sobreviventes e Não Sobreviventes')
plt.show()
