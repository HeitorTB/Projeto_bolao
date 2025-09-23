import json
import pandas as pd

# Carregar JSON
with open("dados/palpites.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Transformar em lista de linhas
linhas = []
for usuario, palpites in dados.items():
    for jogo_id, resultado in palpites.items():
        linhas.append({
            "Usuário": usuario,
            "Jogo ID": jogo_id,
            "Placar Time 1": resultado["placar1"],
            "Placar Time 2": resultado["placar2"]
        })

# Criar DataFrame
df = pd.DataFrame(linhas)

# Exportar para Excel
df.to_excel("palpites_exportados.xlsx", index=False)
