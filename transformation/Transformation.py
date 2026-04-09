from ingestion import Coleta
import matplotlib.pyplot as plt

dados_paises = Coleta.dados

# gerar gráficos para os 5 primeiros países
for pais in dados_paises[:5]:
    nome = pais['country']
    continente = pais.get('continent', 'N/A')
    casos = pais['cases']
    mortes = pais['deaths']
    recuperados = pais['recovered']

    dic = {
        "casos": f"{casos} pessoas foram infectadas.",
        "mortes": f"{mortes} pessoas morreram.",
        "recuperados": f"{recuperados} pessoas se recuperaram."
    }

    print(f"\n--- {nome} ({continente}) ---")
    for chave, valor in dic.items():
        print(f"{chave.capitalize()}: {valor}")

    # Visualização dos dados com Matplotlib
    plt.bar(dic.keys(), [int(v.split()[0]) for v in dic.values()])
    plt.xlabel("Situação")
    plt.ylabel("Número de Pessoas")
    plt.title(f"Dados do COVID-19 em {nome} ({continente})")

    categorias = ['Casos', 'Mortes', 'Recuperados']
    valores = [casos, mortes, recuperados]

    plt.bar(categorias, valores, color=['blue', 'red', 'green'])
    plt.title(f'Dados COVID-19 - {nome} ({continente})')
    plt.show()