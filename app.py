import streamlit as st
import pandas as pd
import sqlite3

def conect():
    return sqlite3.connect("banco_dados.db")

def tabela():
    conn = conect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vendas(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  idade INT,
                  sexo TEXT,
                  email TEXT
                )
              ''')
    conn.commit()
    conn.close()

tabela()

def atualizar_bd():
    conn = conect()
    c = conn.cursor()
    c.execute("")

def inserir_cliente(nome, sexo, email, idade):
    conn = conect()
    c = conn.cursor()
    c.execute("INSERT INTO vendas (nome, sexo, email, idade) VALUES (?, ?, ?, ?)", (nome, sexo, email, idade))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conect()
    c = conn.cursor()
    c.execute("SELECT * FROM vendas")
    dados = c.fetchall()
    conn.close()
    return dados

def listar_idade():
    conn = conect()
    c = conn.cursor()
    c.execute("SELECT idade FROM pessoas")
    dados = c.fetchall()
    conn.close()
    return dados


def atualizar_cliente(id, nome, sexo, email, idade):
    conn = conect()
    c = conn.cursor()
    c.execute("UPDATE vendas SET nome = ?, sexo = ?, email = ?, idade = ? WHERE id = ?", (nome, sexo, email, idade, id))
    conn.commit()
    conn.close()

def deletar_cliente(id):
    conn = conect()
    c = conn.cursor()
    c.execute("DELETE FROM vendas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

st.title("Sistema de vendas.")

st.sidebar.title("Menu.")
opcao = st.sidebar.radio("Escolha:", ['Cadastrar', 'Listar / Editar / Excluir', 'Dados'])

if opcao == "Cadastrar":
    st.title("-- Cadastro de clientes --")
    nome = st.text_input("Coloque seu nome:")
    idade = st.text_input("Coloque sua idade:")
    sexo = st.selectbox("Selecione seu sexo:", ["Masculino", "Feminino", "Outro"])
    email = st.text_input("Coloque seu email:")

    if st.button("Cadastrar"):
        if nome and email:
            inserir_cliente(nome, sexo, email, idade)
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")

elif opcao == "Listar / Editar / Excluir":
    st.title("Listar, Editar e Excluir clientes")
    tabela()
    dados = listar_clientes()
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Idade", "Sexo", "Email"])
    st.dataframe(df)

    id_cliente = st.number_input("Digite o ID do cliente para editar ou excluir:", min_value=1, step=1)

    if st.button("Carregar dados do cliente"):
        cliente = df[df["ID"] == id_cliente]
        if not cliente.empty:
            nome_atual = cliente.iloc[0]["Nome"]
            sexo_atual = cliente.iloc[0]["Sexo"]
            idade_atual = cliente.iloc[0]["Idade"]
            email_atual = cliente.iloc[0]["Email"]

            novo_nome = st.text_input("Nome:", value=nome_atual)
            nova_idade = st.text_input("Idade:", value=idade_atual)
            novo_sexo = st.selectbox("Sexo:", ["Masculino", "Feminino", "Outro"], index=["Masculino", "Feminino", "Outro"].index(sexo_atual))
            novo_email = st.text_input("Email:", value=email_atual)

            if st.button("Atualizar"):
                atualizar_cliente(id_cliente, novo_nome, novo_sexo, novo_email, nova_idade)
                st.success("Cliente atualizado com sucesso!")

            if st.button("Excluir"):
                deletar_cliente(id_cliente)
                st.success("Cliente excluído com sucesso!")
        else:
            st.error("Cliente não encontrado.")



#elif opcao == "Dados":
#    st.title("Graphic Area")
#    
#    escolha = st.selectbox("Escolha qual tipo de gráfico irá ver:", ["Idades", "Nomes começando com letras", "Natalidade"])
#    if escolha == "Idades":
#        st.subheader("Gráfico de idades")
#        dados_idade = listar_idade()
#        df_idade = pd.DataFrame(dados_idade, columns=["Idade"])
#        st.bar_chart(df_idade["Idade"].value_counts())
#    
#    elif escolha == "Nomes começando com letras":
#        st.subheader("Gráfico de nomes começando com letras")
#        conn = conect()
#        c = conn.cursor()
#        c.execute("SELECT nome FROM pessoas")
#        dados_nomes = c.fetchall()
#        conn.close()
#        nomes = [nome[0] for nome in dados_nomes]
#        letras_iniciais = [nome[0].upper() for nome in nomes if nome]
#        df_letras = pd.DataFrame(letras_iniciais, columns=["Letra"])
#        st.bar_chart(df_letras["Letra"].value_counts())
#    
#    elif escolha == "Natalidade":
#        st.subheader("Gráfico de natalidade")
#        conn = conect()
#        c = conn.cursor()
#        c.execute("SELECT nascimento FROM pessoas")
#        dados_nascimento = c.fetchall()
#        conn.close()
#        anos_nascimento = [nascimento[0].split("-")[0] for nascimento in dados_nascimento if nascimento and nascimento[0]]
#        df_nascimento = pd.DataFrame(anos_nascimento, columns=["Ano"])
#        st.bar_chart(df_nascimento["Ano"].value_counts())
#
#
