import streamlit as st
from utils import carregar_palpites, salvar_palpite, carregar_jogos

st.title("🏆 Bolão da Copa do Mundo 2026")

usuario = st.text_input("Digite seu nome:")
jogos = carregar_jogos()

if usuario:
    st.subheader("📋 Palpites da fase de grupos")

    dados = carregar_palpites()
    usuario_dados = dados.get(usuario.lower(), {})

    for jogo in jogos:
        jogo_id = str(jogo["id"])
        if jogo_id in usuario_dados:
            st.markdown(f"✅ Palpite já enviado para {jogo['time1']} x {jogo['time2']}: "
                        f"{usuario_dados[jogo_id]['placar1']} x {usuario_dados[jogo_id]['placar2']}")
            continue  # pula para o próximo jogo

        st.markdown(f"**{jogo['time1']} x {jogo['time2']}** (Grupo {jogo['grupo']})")
        col1, col2 = st.columns(2)
        with col1:
            placar1 = st.number_input(f"{jogo['time1']} ({jogo_id})", min_value=0, key=f"{jogo_id}_1")
        with col2:
            placar2 = st.number_input(f"{jogo['time2']} ({jogo_id})", min_value=0, key=f"{jogo_id}_2")

        if st.button(f"Salvar palpite {jogo_id}"):
            sucesso = salvar_palpite(usuario.lower(), jogo["id"], placar1, placar2)
            if sucesso:
                st.success("Palpite salvo com sucesso!")
            else:
                st.warning("Você já enviou palpite para esse jogo.")
