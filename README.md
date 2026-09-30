# 💵 Monitor de Indicadores Econômicos

Coleta da cotação do dólar a partir da API pública do Banco Central do Brasil.
O objetivo é acompanhar a variação do câmbio ao longo do tempo e servir de base para análises econômicas.

## 📊 Fonte dos dados
- **API:** SGS – Sistema Gerenciador de Séries Temporais do Banco Central
- **Série:** 1 – Taxa de câmbio livre, dólar americano (venda), diária
- **Frequência:** apenas em dias úteis
- **Link:** https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/09/2026&dataFinal=30/09/2026

## ⚙️ Como executar
1. Criar o ambiente virtual:
```
py -m venv .venv
```
2. Ativar o ambiente:
```
.venv\Scripts\Activate.ps1
```
3. Instalar as dependências:
```
pip install -r requirements.txt
```
4. Rodar o script:
```
python coletar_dolar.py
```

## 📁 Estrutura
- `coletar_dolar.py` – script que consulta a API do Banco Central e salva as cotações
- `dolar.csv` – arquivo gerado com as cotações (data e valor)
- `requirements.txt` – bibliotecas necessárias para executar o projeto

## 🚀 Próximos passos
- [ ] v2: limpeza com pandas e gráfico da evolução do dólar
- [ ] v3: armazenamento em banco de dados (DuckDB) e análises com SQL
- [ ] v4: atualização automática diária com GitHub Actions
- [ ] v5: testes de qualidade de dados e novos indicadores (Selic e IPCA)