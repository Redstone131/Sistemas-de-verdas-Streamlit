from Utilidade.banco import conect
from form_model import Registrador

def adicionar_estudante(nome, idade, sexo, email):
    conn = conect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoa (nome) VALUES (?)", (nome, sexo, idade, email))
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM pessoa")
    rows = cursor.fetchall()
    conn.close()
    return [Registrador(*rows) for row in rows]