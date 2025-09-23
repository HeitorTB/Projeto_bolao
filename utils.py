import json
import os

def carregar_palpites(caminho="dados/palpites.json"):
    if not os.path.exists(caminho):
        return {}
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_palpite(usuario, jogo_id, placar1, placar2, caminho="dados/palpites.json"):
    dados = carregar_palpites(caminho)
    if usuario not in dados:
        dados[usuario] = {}
    if str(jogo_id) in dados[usuario]:
        return False  # Já existe palpite para esse jogo

    dados[usuario][str(jogo_id)] = {
        "placar1": placar1,
        "placar2": placar2
    }
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    return True

def carregar_jogos(caminho="jogos.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)