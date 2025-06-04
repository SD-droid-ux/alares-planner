# Alares Planner

Projeto inicial com autenticação via login e senha para dois perfis:
- Administrador (login: alares_planner / senha: Admin)
- Usuário comum (login: Projetos01 / senha: cnx@123)

## Como rodar

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Execute o app:
```
streamlit run main.py
```

3. Faça login com seu usuário e senha.

---

## Estrutura

- main.py: tela de login e redirecionamento por perfil
- admin.py: página exclusiva para administrador
- user.py: página para usuários comuns