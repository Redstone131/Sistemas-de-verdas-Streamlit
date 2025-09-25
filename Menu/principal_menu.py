import streamlit as st
from Utilidade.banco import tabela
from Views import cadastro, langchain, dashboard


def showPrincipal():
    st.title("OrtêncIA")

    st.sidebar.title("Menu.")
    opcao = st.sidebar.radio("Escolha:", ['Cadastrar', 'Listar / Editar / Excluir', 'Dados', 'IA', 'Documentos'])

    if opcao == "Cadastrar":
        cadastro.showCadastro()

    elif opcao == "Listar / Editar / Excluir":
        cadastro.showListar()

    elif opcao == "Dados":
        dashboard.showDashboard()

    elif opcao == "IA":
        langchain.show()

    elif opcao == "Documentos":
        from Views import documentos
        documentos.showDocumentos()