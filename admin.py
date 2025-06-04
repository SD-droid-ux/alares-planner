import streamlit as st

# Verifica se está logado e é admin
if "autenticado" not in st.session_state or not st.session_state.autenticado or st.session_state.perfil != "admin":
    st.warning("⛔ Acesso restrito. Faça login como administrador.")
    st.stop()

st.title("🛠️ Painel do Administrador")
st.markdown("Gerencie dados, usuários e funcionalidades do sistema.")

# Exemplo de ações
st.button("🔄 Atualizar Base de Dados")
st.button("📤 Exportar Relatórios")