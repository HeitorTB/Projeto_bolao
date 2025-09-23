import json
from openpyxl import Workbook

# Carregar dados
with open("dados/palpites.json", "r", encoding="utf-8") as f:
    palpites = json.load(f)

with open("jogos.json", "r", encoding="utf-8") as f:
    jogos = json.load(f)

# Criar dicionário de jogos por ID
jogos_dict = {str(j["id"]): j for j in jogos}

# Criar planilha
wb = Workbook()
wb.remove(wb.active)  # Remove aba padrão

for usuario, jogos_usuario in palpites.items():
    sheet = wb.create_sheet(title=usuario.capitalize())
    sheet.append(["Jogo", "Grupo", "Time 1", "Placar 1", "Time 2", "Placar 2"])

    for jogo_id, resultado in jogos_usuario.items():
        jogo = jogos_dict.get(jogo_id)
        if jogo:
            linha = [
                f"{jogo['time1']} x {jogo['time2']}",
                jogo["grupo"],
                jogo["time1"],
                resultado["placar1"],
                jogo["time2"],
                resultado["placar2"]
            ]
            sheet.append(linha)

# Salvar planilha
wb.save("palpites_por_usuario.xlsx")
print("✅ Planilha gerada com sucesso!")
