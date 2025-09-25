import sqlite3

def conect():
    return sqlite3.connect("Data/banco_dados.db", check_same_thread=False)

def tabela():
    conn = conect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pessoa(
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

def tabelaRegistro():
    conn = conect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS registro(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT NOT NULL,
                  senha TEXT NOT NULL
                )
              ''')
    conn.commit()
    conn.close()

tabelaRegistro()

def inserir_registro(email, senha):
    conn = conect()
    c = conn.cursor()
    c.execute("INSERT INTO registro (email, senha) VALUES (?, ?)", (email, senha))
    conn.commit()
    conn.close()


