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
  - Visualização com gráfico de barras (`plt.bar`) em duas abordagens:  
    - Extraindo números das frases com `split()`.  
    - Usando diretamente as variáveis numéricas.  
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

---

## 🚀 O que ainda será feito

### 4. Banco de Dados (Expansão)
- Criar tabelas adicionais: `casos_covid`, `vacinacao`, `regioes`.  
- Implementar carga incremental dos dados.  
- Normalizar strings para garantir compatibilidade com UTF‑8.  

### 5. Visualização Avançada (UX/UI)
- **Ferramentas**: Power BI / Streamlit  
- **Função**: Dashboards interativos e relatórios.  
- **Próximos passos técnicos**:  
  - Evolução temporal dos casos (média móvel).  
  - Comparativo entre regiões.  
  - Taxa de vacinação por faixa etária.  

---

## 📦 Tecnologias
- **Python**: Requests, Pandas, SQLAlchemy, Matplotlib  
- **Banco de Dados**: PostgreSQL  
- **Visualização**: Power BI / Streamlit  

---

## ⚠️ Dificuldades enfrentadas
- Erros de **UnicodeDecodeError** ao conectar com o banco, resolvidos com ajustes de encoding e revisão da string de conexão.  
- Mudança de comportamento no **SQLAlchemy 2.0**, que não aceita mais strings diretas em `conn.execute()`, exigindo o uso de `text()`.  
- Necessidade de recriar senha e revisar credenciais para evitar problemas de compatibilidade.  
- Ajustes na integração entre DataFrame e banco para garantir que os dados com acentos fossem gravados corretamente.  
- **Novo desafio**:  
  - Execução incorreta dos comandos SQL em bloco único no psql, causando erro de “relação não existe”.  
  - Solução: rodar cada `CREATE TABLE` separadamente com ponto e vírgula.  
  - Verificação com `SELECT` mostrou tabelas criadas mas vazias, confirmando que faltava rodar o script Python para inserir os dados.  
  - Após rodar o script, dados foram populados com sucesso e a estrutura relacional validada.  

---
