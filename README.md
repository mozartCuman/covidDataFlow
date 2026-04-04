# 📊 Pipeline de Dados COVID

## ✅ O que já foi implementado

### 1. Ingestão (Coleta)
- **Ferramentas:** Python + Requests  
- **Função:** Consome a API pública [Disease.sh](https://disease.sh/v3/covid-19/countries/brazil?strict=true).  
- **Técnicas aplicadas:**  
  - Uso de `requests.get()` com **timeout** para evitar travamentos.  
  - Conversão da resposta em **JSON → dicionário Python**.  
  - Extração de chaves específicas (`cases`, `deaths`, `recovered`).  
  - Tratamento de exceções (`RequestException`) para robustez.  

### 2. Transformação (Transformation)
- **Ferramentas:** Python + Matplotlib  
- **Função:** Organiza os dados coletados e gera visualizações.  
- **Técnicas aplicadas:**  
  - Criação de **dicionário** com frases descritivas.  
  - Uso de **f-strings** para combinar números e texto.  
  - Iteração com `.items()` para imprimir resultados formatados.  
  - Visualização com **gráfico de barras** (`plt.bar`) em duas abordagens:  
    - Extraindo números das frases com `split()`.  
    - Usando diretamente as variáveis numéricas.  
  - Customização de cores e rótulos nos gráficos.  

---

## 🚀 O que ainda será feito

### 3. Banco de Dados (BDD)
- **Ferramenta:** PostgreSQL  
- **Função:** Armazenar dados tratados em tabelas relacionais.  
- **Próximos passos técnicos:**  
  - Criar tabelas (`casos_covid`, `vacinacao`, `regioes`).  
  - Conectar via **SQLAlchemy**.  
  - Implementar carga automática dos dados.  

### 4. Visualização Avançada (UX/UI)
- **Ferramentas:** Power BI / Streamlit  
- **Função:** Dashboards interativos e relatórios.  
- **Próximos passos técnicos:**  
  - Evolução temporal dos casos (média móvel).  
  - Comparativo entre regiões.  
  - Taxa de vacinação por faixa etária.  

---

## 📦 Tecnologias
- **Python** (Requests, Pandas, SQLAlchemy, Matplotlib)  
- **PostgreSQL**  
- **Power BI / Streamlit**  
