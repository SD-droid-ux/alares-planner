import streamlit as st

# Verifica se está logado e é usuário comum
if "autenticado" not in st.session_state or not st.session_state.autenticado or st.session_state.perfil != "user":
    st.warning("⛔ Acesso restrito. Faça login como usuário.")
    st.stop()

st.title("📋 Painel do Usuário")
st.markdown("Bem-vindo ao sistema Alares Planner!")

# Exemplo de funcionalidades
cidade = st.selectbox("Selecione uma cidade:", ["São Paulo", "Curitiba", "Recife"])
st.write(f"Cidade selecionada: {cidade}")

cto = st.text_input("Buscar CTO:")
if cto:
    st.write(f"Buscando dados para CTO: {cto}")