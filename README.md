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

### Banco e Encoding
- Conexão e configuração do banco (encoding, credenciais).  
- Inserção de dados com acentos (UTF‑8).  

### Frameworks
- Mudanças no SQLAlchemy 2.0 (uso obrigatório de `text()`).  

### Estrutura
- Execução de múltiplos `CREATE TABLE` em bloco único → erro de dependência.  
- Organização das pastas para rodar com Uvicorn.  

### Ambiente
- Bloqueio de execução de scripts no PowerShell ao ativar venv.  

### Queries
- Coluna inexistente (`d.data`) → corrigida para `d.data_atualizacao`.  
- Referência incorreta (`c.continente`) → corrigida para `c.nome`.  

### Novas dificuldades enfrentadas
- Funções duplicadas (`get_continentes`) e imports incorretos (`get_paises_by_continente` antes de existir).  
- IndexError ao acessar `row[1]` quando a query retornava apenas uma coluna.  
- Demora na validação automática de merge no GitHub.  

---

## 🎯 Aprendizados

### Banco de Dados
- Validar o **schema** antes de escrever queries.  
- Configurar corretamente o **UTF‑8** para evitar problemas com acentos.  

### Frameworks
- Acompanhar mudanças em frameworks (SQLAlchemy 2.0).  
- Uso obrigatório de `text()` em queries SQL.  

### Organização
- Estrutura modular (`database.py`, `crud.py`, `routes/`) facilita manutenção.  
- Separar funções com nomes distintos previne conflitos.  

### Desenvolvimento
- Testar endpoints **um por vez** ajuda a identificar falhas rapidamente.  
- Conferir o formato do retorno SQL (tupla com uma coluna → usar `row[0]`).  

### Fluxo de Trabalho
- Documentar bem PRs facilita revisão.  
- Conhecer alternativas de merge via linha de comando.  

### Boas Práticas
- Garantir integridade dos dados com encoding correto.  
- Fazer commits claros e descritivos.  
- Manter README atualizado com dificuldades e aprendizados.  

---

### 🌐 Exemplos de uso da API

## Status da API
bash
curl http://127.0.0.1:8000/status

##Lista de continentes
bash
curl http://127.0.0.1:8000/api/continentes

## Países de um continente
bash
curl http://127.0.0.1:8000/api/continentes/Asia/paises

## Dados de COVID por país
bash
curl http://127.0.0.1:8000/api/covid/Brazil

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
