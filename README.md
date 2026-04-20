# 📊 Pipeline de Dados COVID

Um sistema completo para **coleta, transformação, persistência e disponibilização de dados sobre COVID-19**, integrando **Python, PostgreSQL, FastAPI** e ferramentas de visualização.

---

## ✅ O que já foi implementado

### 1. Ingestão (Coleta)
- **Ferramentas**: Python + Requests  
- Consumo da API pública [Disease.sh](https://disease.sh).  
- Conversão da resposta em JSON e extração de chaves (`cases`, `deaths`, `recovered`).  
- Tratamento de exceções para robustez.  

### 2. Transformação (Visualização)
- **Ferramentas**: Python + Matplotlib  
- Organização dos dados em dicionários descritivos.  
- Gráficos de barras com customização de cores e rótulos.  

### 3. Banco de Dados (Persistência)
- **Ferramenta**: PostgreSQL + SQLAlchemy  
- Criação das tabelas `continentes`, `paises`, `dados_covid` com chaves estrangeiras.  
- Inserção automática com `ON CONFLICT DO NOTHING`.  
- Pipeline completo: coleta → transformação → persistência.  

### 4. API (FastAPI)
- **Ferramenta**: FastAPI + Uvicorn  
- Endpoints implementados:  
  - `/status` → status da API.  
  - `/api/continentes` → lista continentes.  
  - `/api/continentes/{nome}/paises` → países de um continente.  
  - `/api/covid/{pais}` → dados de COVID por país.  
  - `/api/covid/continente/{nome}` → dados de COVID por continente.  
  - `/api/covid/top/{n}` → top N países com mais casos.  
  - `/api/covid/resumo_global` → resumo global.  
  - `/api/covid/evolucao/{pais}` → evolução temporal.  
  - `/api/covid/ranking/{continente}` → ranking de países dentro de um continente.  

---

## 🚀 O que ainda será feito
- CRUD completo (Create, Read, Update, Delete).  
- Modularização em `database.py`, `crud.py`, `routes.py`.  
- Novas tabelas: `vacinacao`, `regioes`.  
- Rotas adicionais para comparações e previsões.  
- Integração com IA para previsão de casos e mortes.  
- Dashboards interativos com Power BI / Streamlit.  

---

## ⚠️ Dificuldades enfrentadas
- Conexão e configuração do banco (encoding, credenciais).  
- Mudanças no SQLAlchemy 2.0 (uso obrigatório de `text()`).  
- Estrutura das tabelas e dependências de chaves estrangeiras.  
- Inserção de dados com acentos (UTF‑8).  
- Organização das pastas para rodar com Uvicorn.  
- Bloqueio de execução de scripts no PowerShell.  
- Queries SQL específicas corrigidas (`data_atualizacao`, `c.nome`).  

---

## 🎯 Aprendizados
- Validar o **schema do banco** antes de escrever queries.  
- Acompanhar mudanças em **frameworks** (SQLAlchemy 2.0).  
- Modularizar o projeto para evitar erros de importação.  
- Garantir integridade dos dados com atenção ao **encoding**.  
- Fazer testes incrementais (rota por rota) para identificar falhas rapidamente.  

---

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.10+  
- PostgreSQL 14+  
- Virtualenv (recomendado)  

### Passo a passo
```bash
# Clonar o repositório
git clone https://github.com/seuusuario/CovidDataFlow.git
cd CovidDataFlow

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor FastAPI
uvicorn backend.main:app --reload
