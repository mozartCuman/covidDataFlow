import requests

url = 'https://disease.sh/v3/covid-19/countries/brazil?strict=true'


headers = {
    'User-Agent': 'Covid-19 Data Collector/1.0'
}   

try: # Tente fazer a requisição
    #  Realizando a busca (GET) com Segurança (Timeout)
    # Por que: Usamos GET porque queremos buscar informações [8]. 
    # O 'timeout' de 10 segundos impede que o programa fique travado para sempre se o site cair [9, 10].
    response = requests.get(url, headers=headers, timeout=10)

    #Transformação dos dados (JSON)
    # Por que: A API responde com uma "string" longa (texto). 
    # O método .json() converte esse texto em um dicionário Python, facilitando o acesso
    dados = response.json()

    # Extração de informações específicas
    # Três dados importantes: casos confirmados, mortes e recuperados
    # - Use dados['cases'] quando a chave é obrigatória e se quer que o programa quebre caso ela não exista.
    # - Use dados.get('cases', 'N/A') quando a chave pode faltar e você queremos um valor padrão em vez de erro.

    casos = dados['cases'] # 'N/A' é um valor padrão caso a chave não exista
    mortes = dados['deaths'] # 'N/A' é um valor padrão caso a chave não exista
    recuperados = dados['recovered'] # 'N/A' é um valor padrão caso a chave não exista

    print(f" Http 200 - Dados coletados com sucesso!")
    

except requests.exceptions.RequestException as e:
    # Por que: É importante tratar erros (como falta de internet) para o programa não "quebrar" [13].
    print(f"Erro ao buscar dados: {e}")

