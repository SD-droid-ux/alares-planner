import streamlit as st
import pandas as pd
import os

def autenticar(login, senha):
    if login == "Projetos01" and senha == "cnx@123":
        return "user"
    elif login == "alares_planner" and senha == "Admin":
        return "admin"
    else:
        return None

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.perfil = None
    st.session_state.tela = "login"

if st.session_state.tela == "login":
    st.title("🔐 Login Alares Planner")

    login_input = st.text_input("Login:")
    senha_input = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        perfil = autenticar(login_input, senha_input)
        if perfil:
            st.session_state.autenticado = True
            st.session_state.perfil = perfil
            st.session_state.tela = perfil
            st.experimental_rerun()
        else:
            st.error("❌ Login ou senha incorretos.")

elif st.session_state.tela == "admin":
    st.title("🛠️ Painel do Administrador")

    uploaded_file = st.file_uploader("Faça upload do arquivo Excel (.xlsx ou .xls)", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success("Arquivo carregado com sucesso!")
            st.dataframe(df)

            save_path = "data"
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            file_path = os.path.join(save_path, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.info(f"Arquivo salvo em: {file_path}")

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")

    if st.button("Logout"):
        st.session_state.autenticado = False
        st.session_state.perfil = None
        st.session_state.tela = "login"
        st.experimental_rerun()

elif st.session_state.tela == "user":
    st.title("📋 Painel do Usuário")
    st.markdown("Bem-vindo ao sistema Alares Planner!")

    cidade = st.selectbox("Selecione uma cidade:", ["São Paulo", "Curitiba", "Recife"])
    st.write(f"Cidade selecionada: {cidade}")

    cto = st.text_input("Buscar CTO:")
    if cto:
        st.write(f"Buscando dados para CTO: {cto}")

    if st.button("Logout"):
        st.session_state.autenticado = False
        st.session_state.perfil = None
        st.session_state.tela = "login"
        st.experimental_rerun()
