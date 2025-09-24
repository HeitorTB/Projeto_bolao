import streamlit as st 
from utils import carregar_palpites, salvar_palpite, carregar_jogos

# 🔐 Captura e mantém o nome do usuário
if "usuario" not in st.session_state:
    nome = st.text_input("Digite seu nome:", key="nome_usuario")
    if nome:
        st.session_state.usuario = nome.lower()
        st.rerun()  # Recarrega a página com o nome salvo

# ✅ Se o nome já estiver salvo, segue com o app
else:
    usuario = st.session_state.usuario
    st.success(f"Bem-vindo, {usuario.capitalize()}!")

    st.title("🏆 Bolão da Copa do Mundo 2026")
    st.subheader("📋 Palpites da fase de grupos")

    jogos = carregar_jogos()
    dados = carregar_palpites()
    usuario_dados = dados.get(usuario, {})

    for jogo in jogos:
        jogo_id = str(jogo["id"])
        if jogo_id in usuario_dados:
            palpite = usuario_dados[jogo_id]
            st.markdown(f"✅ {jogo['time1']} x {jogo['time2']}: {palpite['placar1']} x {palpite['placar2']}")
            continue

        st.markdown(f"**{jogo['time1']} x {jogo['time2']}** (Grupo {jogo['grupo']})")
        col1, col2 = st.columns(2)
        with col1:
            placar1 = st.number_input(f"{jogo['time1']} ({jogo_id})", min_value=0, key=f"{jogo_id}_1")
        with col2:
            placar2 = st.number_input(f"{jogo['time2']} ({jogo_id})", min_value=0, key=f"{jogo_id}_2")

        if st.button(f"Salvar palpite {jogo_id}"):
            sucesso = salvar_palpite(usuario, jogo["id"], placar1, placar2)
            if sucesso:
                st.success("Palpite salvo com sucesso!")
                st.rerun()
            else:
                st.warning("Você já enviou palpite para esse jogo.")

    # 🔄 Botão para trocar de usuário
    if st.button("Trocar de usuário"):
        del st.session_state.usuario
        st.rerun()
