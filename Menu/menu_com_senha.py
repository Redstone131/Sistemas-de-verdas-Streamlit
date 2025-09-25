import streamlit as st
from Utilidade.banco import conect, tabelaRegistro, inserir_registro
from . import principal_menu

def showSenha():
    st.title("Bem-vindo ao OrtêncIA")
    st.sidebar.title("Menu com senha.")
    tabelaRegsitro()

    menu = st.sidebar.radio("Escolha:", ['Login', 'Registrar'])

    if menu == "Login":
        st.subheader("Login")

        email = st.text_input("Email")
        senha = st.text_input("Senha", type='password')
        if st.button("Login"):
            conn = conect()
            c = conn.cursor()
            c.execute("SELECT * FROM registro WHERE email = ? AND senha = ?", (email, senha))
            dados = c.fetchall()
            conn.close()
            if dados:
                st.success("Login realizado com sucesso!")
                showPrincipal()
            else:
                st.error("Email ou senha incorretos.")

    elif menu == "Registrar":
        st.subheader("Registrar novo usuário")

        new_email = st.text_input("Email", key="new_email")
        new_senha = st.text_input("Senha", type='password', key="new_senha")
        if st.button("Registrar"):
            inserir_registro(new_email, new_senha)
            st.success("Usuário registrado com sucesso! Por favor, faça o login.")



