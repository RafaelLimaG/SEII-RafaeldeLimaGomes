import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('~/code/SEII-RafaeldeLimaGomes/Semana03/Exercicio05/athlete_events.csv')

print(dados.head())

masculinos = dados.loc[dados['Sex'] =='M']
altura = masculinos['Height']
peso = masculinos['Weight']

plt.scatter(altura, peso)
plt.show()
