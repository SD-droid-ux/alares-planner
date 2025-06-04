import streamlit as st

# Função para verificar login e senha
def autenticar(login, senha):
    return login == "Projetos01" and senha == "cnx@123"

# Verifica se o usuário já está autenticado
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# Se não autenticado, exibe a tela de login
if not st.session_state.autenticado:
    st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")
    st.title("🔐 Página de Login")

    login_input = st.text_input("Login:")
    senha_input = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        if autenticar(login_input, senha_input):
            st.session_state.autenticado = True
            st.success("✅ Login bem-sucedido!")
            st.experimental_rerun()
        else:
            st.error("❌ Login ou senha incorretos.")

# Se autenticado, exibe a tela principal
else:
    st.set_page_config(page_title="Alares Planner", page_icon="📊", layout="wide")
    st.success("🔓 Acesso autorizado.")
    st.markdown("### Bem-vindo ao Alares Planner!")
    st.markdown("Use o menu lateral para navegar entre as funcionalidades.")
