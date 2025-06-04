import streamlit as st

# Função de autenticação
def autenticar(login, senha):
    if login == "Projetos01" and senha == "cnx@123":
        return "user"
    elif login == "alares_planner" and senha == "Admin":
        return "admin"
    else:
        return None

# Inicializa sessão
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.perfil = None

# Página de login
if not st.session_state.autenticado:
    st.set_page_config(page_title="Login", page_icon="🔐")
    st.title("🔐 Login Alares Planner")

    login_input = st.text_input("Login:")
    senha_input = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        perfil = autenticar(login_input, senha_input)
        if perfil:
            st.session_state.autenticado = True
            st.session_state.perfil = perfil
            st.success(f"✅ Login bem-sucedido! Perfil: {perfil.upper()}")
            st.experimental_rerun()
        else:
            st.error("❌ Login ou senha incorretos.")

# Página após login
else:
    st.set_page_config(page_title="Alares Planner", page_icon="📊")
    st.sidebar.success(f"Perfil: {st.session_state.perfil.upper()}")

    # Redirecionamento por perfil
    if st.session_state.perfil == "admin":
        st.experimental_set_query_params(page="admin")
        st.experimental_rerun()
    else:
        st.experimental_set_query_params(page="user")
        st.experimental_rerun()