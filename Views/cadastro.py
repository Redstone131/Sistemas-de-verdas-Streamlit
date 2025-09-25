import streamlit as st
from Models.controller_estud import adicionar_estudante, listar_estudantes

def showCadastro():
    st.title("-- Cadastro de clientes --")
    nome = st.text_input("Coloque seu nome:")
    idade = st.text_input("Coloque sua idade:")
    sexo = st.selectbox("Selecione seu sexo:", ["Masculino", "Feminino", "Outro"])
    email = st.text_input("Coloque seu email:")

    if st.button("Cadastrar"):
        if nome and email:
            adicionar_estudante(nome, sexo, email, idade)
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")