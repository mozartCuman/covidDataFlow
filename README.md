# 📊 Pipeline de Dados COVID

## ✅ O que já foi implementado

### 1. Ingestão (Coleta)
- **Ferramentas**: Python + Requests  
- **Função**: Consome a API pública [Disease.sh](https://disease.sh).  
- **Técnicas aplicadas**:  
  - Uso de `requests.get()` com timeout para evitar travamentos.  
  - Conversão da resposta em JSON → dicionário Python.  
  - Extração de chaves específicas (`cases`, `deaths`, `recovered`).  
  - Tratamento de exceções (`RequestException`) para robustez.  

### 2. Transformação (Transformation)
- **Ferramentas**: Python + Matplotlib  
- **Função**: Organiza os dados coletados e gera visualizações.  
- **Técnicas aplicadas**:  
  - Criação de dicionário com frases descritivas.  
  - Uso de f-strings para combinar números e texto.  
  - Iteração com `.items()` para imprimir resultados formatados.  
  - Visualização com gráfico de barras (`plt.bar`) em duas abordagens.  
  - Customização de cores e rótulos nos gráficos.  

### 3. Banco de Dados (BDD)
- **Ferramenta**: PostgreSQL + SQLAlchemy  
- **Função**: Armazenar os dados tratados em tabelas relacionais.  
- **Técnicas aplicadas**:  
  - Criação de conexão com `create_engine`.  
  - Teste de conexão com `text("SELECT current_database();")`.  
  - Inserção automática dos dados com `INSERT INTO ... ON CONFLICT DO NOTHING`.  
  - Criação das tabelas `continentes`, `paises` e `dados_covid` com chaves estrangeiras.  
  - Pipeline completo: coleta → transformação → persistência.  

### 4. API (FastAPI)
- **Ferramenta**: FastAPI + Uvicorn  
- **Função**: Expor os dados do banco em rotas REST.  
- **Implementações feitas**:  
  - Configuração inicial do servidor FastAPI.  
  - Primeira rota de teste (`/`) retornando mensagem de status.  
  - Criação da rota `/api/continentes` para listar todos os continentes armazenados no banco.  
  - Teste bem-sucedido via navegador e Swagger UI.  

---

## 🚀 O que ainda será feito

### Banco de Dados (Expansão)
- Criar tabelas adicionais: `casos_covid`, `vacinacao`, `regioes`.  
- Implementar carga incremental dos dados.  
- Normalizar strings para garantir compatibilidade com UTF‑8.  

### API (FastAPI)
- Criar rota `/api/paises/{continente}` para listar países de um continente.  
- Criar rota `/api/covid/{pais}` para retornar casos, mortes e recuperados.  
- Implementar CRUD completo (Create, Read, Update, Delete).  
- Modularizar o projeto em `database.py`, `crud.py`, `routes.py`.  

### Inteligência Artificial (Planejamento)
- **Status**: ainda não implementado, mas será parte do pipeline.  
- **Objetivos futuros**:  
  - Treinar modelos de previsão de casos e mortes.  
  - Implementar análise de séries temporais (médias móveis, ARIMA, Prophet).  
  - Aplicar clustering para identificar padrões entre países.  
  - Criar rotas na API para expor previsões e insights automáticos.  
  - Integrar resultados em dashboards interativos.  

### Visualização Avançada (UX/UI)
-> - **Frontend do Projeto**: [covidDataFlow_Frontend](https://github.com/mozartCuman/covidDataFlow_Frontend) - <-
- **Ferramentas**: [Power BI](https://powerbi.microsoft.com) / [Streamlit](https://streamlit.io)   
- **Função**: Dashboards interativos e relatórios.  
- **Próximos passos técnicos**:  
  - Evolução temporal dos casos (média móvel).  
  - Comparativo entre regiões.  
  - Taxa de vacinação por faixa etária.  
  - Inclusão de previsões da IA nos dashboards.  

---

## 📦 Tecnologias
- **Python**: Requests, Pandas, SQLAlchemy, Matplotlib, FastAPI  
- **Banco de Dados**: PostgreSQL  
- **Visualização**: Power BI / Streamlit  
- **IA (planejada)**: Scikit-learn, Prophet, técnicas de Machine Learning  

---

## ⚠️ Dificuldades enfrentadas
- Erros de **UnicodeDecodeError** ao conectar com o banco, resolvidos com ajustes de encoding e revisão da string de conexão.  
- Mudança de comportamento no **SQLAlchemy 2.0**, que não aceita mais strings diretas em `conn.execute()`, exigindo o uso de `text()`.  
- Necessidade de recriar senha e revisar credenciais para evitar problemas de compatibilidade.  
- Ajustes na integração entre DataFrame e banco para garantir que os dados com acentos fossem gravados corretamente.  
- Execução incorreta dos comandos SQL em bloco único no psql, causando erro de “relação não existe”.  
  - Solução: rodar cada `CREATE TABLE` separadamente com ponto e vírgula.  
- Verificação inicial mostrou tabelas criadas mas vazias → confirmado que faltava rodar o script Python para inserir os dados.  
- Erros ao rodar o FastAPI com `uvicorn` por causa da estrutura de pastas.   
- Bloqueio de execução de scripts no PowerShell ao ativar o venv → resolvido usando `cmd` ou ajustando `ExecutionPolicy`.  
- Após ajustes, servidor rodou com sucesso e rota `/api/continentes` foi validada.  

---
