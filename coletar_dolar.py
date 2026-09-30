import requests
import pandas as pd

#Montar endereço da API (série 1 = dolar comerial, venda)
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"
parametros = {
    "formato": "json",
    "dataInicial": "01/01/2025",
    "dataFinal": "30/09/2026",
}

# Faz requisição para API
resposta = requests.get(url, params=parametros, timeout=30)
resposta.raise_for_status() #se devolver erro, o script para aqui

# Converte o JSON em tabela(DataFrame)
dados = resposta.json()
df = pd.DataFrame(dados)

#Ajusta os tipos: texto -> data e texto -> número
df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
df["valor"] = df["valor"].astype(float)
df = df.rename(columns={"valor": "dolar_venda"})

# Mostra o resumo e salva em CSV
print(df.tail())
print(f"total de dias: {len(df)}")
df.to_csv("dolar.csv", index=False)
print("Arquivo dolar.csv salvo!")
