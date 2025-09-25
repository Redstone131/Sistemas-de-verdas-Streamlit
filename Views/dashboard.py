import streamlit as st
import pandas as pd
from Utilidade.banco import conect, listar_idade

def showDashboard():
    st.title("Graphic Area")
    
    escolha = st.selectbox("Escolha qual tipo de gráfico irá ver:", ["Idades", "Nomes começando com letras", "Natalidade"])
    if escolha == "Idades":
        st.subheader("Gráfico de idades")
        dados_idade = listar_idade()
        df_idade = pd.DataFrame(dados_idade, columns=["Idade"])
        st.bar_chart(df_idade["Idade"].value_counts())
    
    elif escolha == "Nomes começando com letras":
        st.subheader("Gráfico de nomes começando com letras")
        conn = conect()
        c = conn.cursor()
        c.execute("SELECT nome FROM pessoas")
        dados_nomes = c.fetchall()
        conn.close()
        nomes = [nome[0] for nome in dados_nomes]
        letras_iniciais = [nome[0].upper() for nome in nomes if nome]
        df_letras = pd.DataFrame(letras_iniciais, columns=["Letra"])
        st.bar_chart(df_letras["Letra"].value_counts())
    
    elif escolha == "Natalidade":
        st.subheader("Gráfico de natalidade")
        conn = conect()
        c = conn.cursor()
        c.execute("SELECT nascimento FROM pessoas")
        dados_nascimento = c.fetchall()
        conn.close()
        anos_nascimento = [nascimento[0].split("-")[0] for nascimento in dados_nascimento if nascimento and nascimento[0]]
        df_nascimento = pd.DataFrame(anos_nascimento, columns=["Ano"])
        st.bar_chart(df_nascimento["Ano"].value_counts())