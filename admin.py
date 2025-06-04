import streamlit as st
import pandas as pd
import os

# Verifica se está logado e é admin
if "autenticado" not in st.session_state or not st.session_state.autenticado or st.session_state.perfil != "admin":
    st.warning("⛔ Acesso restrito. Faça login como administrador.")
    st.stop()

st.title("🛠️ Painel do Administrador")

uploaded_file = st.file_uploader("Faça upload do arquivo Excel (.xlsx ou .xls)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.write("Visualização dos dados:")
        st.dataframe(df)

        # Opcional: salvar arquivo para persistência
        save_path = "data"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        file_path = os.path.join(save_path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.info(f"Arquivo salvo em: {file_path}")

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
