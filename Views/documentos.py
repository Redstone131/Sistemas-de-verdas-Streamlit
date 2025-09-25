import streamlit as st
from Utilidade.file_loader import load_pdf, load_excel
from Utilidade.qa_langchain_groq import criar_groq
from Utilidade.limpar_resposta import limpar_resposta
from test.testes import groqCloud

def showDocumentos():
    st.title("Converse com seus documentos (PDF ou Excel)")
    uploaded_file = st.file_uploader("Escolha um arquivo PDF ou Excel", type=["pdf", "csv", "xlsx", "xls"])

    escolha = st.radio("Escolha o estilo", ('Beta teste', 'Com chave'))

    if escolha == 'Com chave':
        chave = st.text_input("Coloque sua chave da API do OpenAI:", type="password")
    else:
        chave = groqCloud
    
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            documentos = load_pdf(uploaded_file)
        elif uploaded_file.type in ["application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "text/csv"]:
            documentos = load_excel(uploaded_file)
        else:
            st.error("Formato de arquivo não suportado. Por favor, envie um PDF ou Excel.")
            return

        if documentos:
            st.success("Documento carregado com sucesso!")
            pergunta = st.text_input("Digite sua pergunta sobre o documento:")
            if st.button("Enviar"):
                if pergunta.strip() == "":
                    st.error("Por favor, digite uma pergunta.")
                else:
                    with st.spinner("Processando sua pergunta..."):
                        resposta = criar_groq(documentos, pergunta, chave)
                        resposta_limpa = limpar_resposta(resposta)
                        st.markdown("**Resposta:**")
                        st.write(resposta_limpa)
        else:
            st.error("Não foi possível carregar o documento. Verifique se o arquivo está correto.")
    