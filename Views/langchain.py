import sttreamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re
from tests.testes import groqCloud

def limpar_texto(texto:str) -> str:
    return re.sub(r"<think>.*?</think>", "", texto, flags=re.DOTALL).strip()

def showCadastro():
    st.title("OrtêncIA, a assistente perfeita para suas dúvidas!")
    st.subheader("Chatbot com IA")

    escolha = st.selectbox("Escolha o modo:", ["Beta teste", "Com key"])

    if escolha == "Com key":
        groq_key = st.text_input("Coloque sua chave da Groq aqui:", type="password")
    elif escolha == "Beta teste":
        groq_key = groqCloud

    modelo = st.selectbox("Escolha o modelo de linguagem:", ["deepseek-3.5", "deepseek-4"])

    with st.form("conteudo_form"):
        titulo = st.text_input("Coloque o título do conteúdo:")
        conteudo = st.text_area("Coloque o conteúdo aqui:")
        gerar = st.form_submit_button("Gerar resposta")
    
    if gerar:
        if not groq_key:
            st.error("Por favor, insira sua chave da Groq.")
        elif not titulo or not conteudo:
            st.error("Por favor, insira o título e o conteúdo.")
        else:
            try:
                llm = ChatGroq(model=modelo, api_key=groq_key)
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "Você é uma assistente (mulher) útil que responde perguntas com base no conteúdo fornecido. Se a pergunta não puder ser respondida com o conteúdo, responda educadamente que você não sabe, uma coisa, não coloque seu pensamento, responda normalmente."),
                    ("user", "Crie um conteúdo didático sobre o conteúdo: {conteudo}, com o título: {titulo}. Depois responda a pergunta: {pergunta}."),
                ])
                chain = prompt | llm | StrOutputParser()

                with st.spinner("Gerando resposta..."):
                    resultado = chain.invoke({"Título": titulo, "conteudo": conteudo})
                    resultado = limpar_texto(resultado)
                    
                st.success("Resposta gerada com sucesso!")
                st.write("### Resposta:")
                st.write(resultado)

            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")