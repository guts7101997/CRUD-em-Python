from tkinter import *
import mysql.connector

# conexão com banco
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mello0408',
    database='cruddb'
)

cursor = conexao.cursor()

# funções CRUD

def inserir():
    nome = entrada_nome.get()
    valor = entrada_valor.get()

    comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"
    valores = (nome, valor)

    cursor.execute(comando, valores)
    conexao.commit()

    listar()


def listar():
    lista.delete(0, END)

    comando = "SELECT * FROM vendas"
    cursor.execute(comando)

    resultado = cursor.fetchall()

    for linha in resultado:
        lista.insert(END, linha)


def atualizar():
    nome = entrada_nome.get()
    valor = entrada_valor.get()

    comando = "UPDATE vendas SET valor=%s WHERE nome_produto=%s"
    valores = (valor, nome)

    cursor.execute(comando, valores)
    conexao.commit()

    listar()


def deletar():
    nome = entrada_nome.get()

    comando = "DELETE FROM vendas WHERE nome_produto=%s"
    valores = (nome,)

    cursor.execute(comando, valores)
    conexao.commit()

    listar()


# janela
janela = Tk()
janela.title("Sistema de Vendas")
janela.geometry("400x400")


# campos
Label(janela, text="Nome do Produto").pack()
entrada_nome = Entry(janela)
entrada_nome.pack()

Label(janela, text="Valor").pack()
entrada_valor = Entry(janela)
entrada_valor.pack()


# botões
Button(janela, text="Inserir", command=inserir).pack(pady=5)
Button(janela, text="Atualizar", command=atualizar).pack(pady=5)
Button(janela, text="Deletar", command=deletar).pack(pady=5)
Button(janela, text="Listar", command=listar).pack(pady=5)


# lista de resultados
lista = Listbox(janela, width=50)
lista.pack(pady=10)


janela.mainloop()


cursor.close()
conexao.close()
