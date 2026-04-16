📊 Pipeline de Dados COVID
✅ O que já foi implementado
1. Ingestão (Coleta)
Ferramentas: Python + Requests

Consumo da API pública Disease.sh.

Conversão da resposta em JSON e extração de chaves (cases, deaths, recovered).

Tratamento de exceções para robustez.

2. Transformação (Visualização)
Ferramentas: Python + Matplotlib

Organização dos dados em dicionários descritivos.

Gráficos de barras com customização de cores e rótulos.

3. Banco de Dados (Persistência)
Ferramenta: PostgreSQL + SQLAlchemy

Criação das tabelas continentes, paises, dados_covid com chaves estrangeiras.

Inserção automática com ON CONFLICT DO NOTHING.

Pipeline completo: coleta → transformação → persistência.

4. API (FastAPI)
Ferramenta: FastAPI + Uvicorn

Endpoints implementados:

/status → status da API.

/api/continentes → lista continentes e países.

/api/covid/{pais} → dados de COVID por país.

/api/covid/continente/{nome} → dados de COVID por continente.

/api/covid/top/{n} → top N países com mais casos.

/api/covid/resumo_global → resumo global de casos, mortes e recuperados.

/api/covid/evolucao/{pais} → evolução temporal de um país.

/api/covid/ranking/{continente} → ranking de países dentro de um continente.

🚀 O que ainda será feito
CRUD completo (Create, Read, Update, Delete).

Modularização em database.py, crud.py, routes.py.

Novas tabelas: vacinacao, regioes.

Rotas adicionais para comparações e previsões.

Integração com IA para previsão de casos e mortes.

Dashboards interativos com Power BI / Streamlit.

⚠️ Dificuldades enfrentadas
1. Conexão e Configuração do Banco
Erros de UnicodeDecodeError e credenciais inválidas ao conectar no PostgreSQL.

Solução: ajuste da string de conexão, recriação da senha e configuração correta de encoding UTF‑8.

2. Evolução do SQLAlchemy
Mudança no SQLAlchemy 2.0, que não aceita mais strings diretas em conn.execute().

Solução: uso obrigatório de text() para envolver comandos SQL, garantindo compatibilidade.

3. Estrutura das Tabelas
Execução de múltiplos CREATE TABLE em bloco único no psql → erro de “relação não existe”.

Solução: rodar cada comando separadamente com ponto e vírgula, validando dependências de chaves estrangeiras.

4. Inserção e Encoding de Dados
Dados com acentos não eram gravados corretamente.

Solução: revisão do encoding e normalização de strings para UTF‑8.

5. FastAPI e Estrutura de Pastas
Erros ao rodar uvicorn devido à organização dos arquivos.

Solução: reorganização do projeto em módulos (database.py, routes.py, etc.), garantindo importações corretas.

6. Ambiente de Desenvolvimento
Bloqueio de execução de scripts no PowerShell ao ativar venv.

Solução: uso do cmd ou ajuste da ExecutionPolicy.

7. Queries SQL específicas
Coluna inexistente (d.data) → corrigida para d.data_atualizacao.

Referência incorreta (c.continente) → corrigida para c.nome.

Solução: revisão do schema das tabelas e ajuste das queries.

🎯 Aprendizados
Validar o schema do banco antes de escrever queries.

Acompanhar mudanças em frameworks (SQLAlchemy 2.0).

Modularizar o projeto para evitar erros de importação.

Garantir integridade dos dados com atenção ao encoding.

Fazer testes incrementais (rota por rota) para identificar falhas rapidamente.
