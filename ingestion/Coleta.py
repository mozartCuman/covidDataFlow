import requests

url = 'https://disease.sh/v3/covid-19/countries'
headers = {'User-Agent': 'Covid-19 Data Collector/1.0'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    dados = response.json()  # lista de países

    

    # Exibir os países com continente só para ver se deu certo o aumento de escala.
    for pais in dados[5:10]:
        nome = pais['country']
        continente = pais.get('continent', 'N/A')
        casos = pais['cases']
        mortes = pais['deaths']
        recuperados = pais['recovered']
        print(f"{nome} ({continente}): {casos} casos, {mortes} mortes, {recuperados} recuperados")

    print("Http 200 - Dados coletados com sucesso!")

except requests.exceptions.RequestException as e:
    print(f"Erro ao buscar dados # Tente outra vez!!! Toca Raul: {e}")