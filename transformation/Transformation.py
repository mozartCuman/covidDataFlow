from ingestion import Coleta
import matplotlib.pyplot as plt

casos = Coleta.casos
mortes = Coleta.mortes
recuperados = Coleta.recuperados

# Dicionário para organizar os dados de forma mais legível
dic = {
    "casos": str(casos) + " pessoas foram infectadas.",
    "mortes": f"{mortes} pessoas morreram.",
    "recuperados": f"{recuperados} pessoas se recuperaram."
}

for chave, valor in dic.items():
    print(f"{chave.capitalize()}: {valor}")

# Visualização dos dados usando Matplotlib com 2 bar diferentes
plt.bar(dic.keys(), [int(v.split()[0]) for v in dic.values()])
plt.xlabel("Situação")
plt.ylabel("Número de Pessoas")
plt.title("Dados do COVID-19 no Brasil")

categorias = ['Casos', 'Mortes', 'Recuperados']
valores = [casos, mortes, recuperados]

plt.bar(categorias, valores, color=['blue', 'red', 'green'])
plt.title('Dados COVID-19 - Brasil')
plt.show()