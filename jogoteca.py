from flask import Flask, render_template, request, redirect, session, flash
import os
#comentario
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)
app.secret_key = os.urandom(24)

jogo1 = Jogo('tetris','puzzle', 'Atari')
jogo2 = Jogo('God of War' , 'Ação' , 'PS2')
jogo3 = Jogo('Crash' , 'plataforma' , 'PS1')
lista = [jogo1, jogo2, jogo3]
@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos' , jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html' ,titulo = 'NOVO JOGO')

@app.route('/criar', methods = ['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'senha123' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario'] 
        flash(session['usuario_logado']+' com sucesso!')
        return redirect ('/')
    else:
        flash('Email ou senha incorretos')
        return redirect('/login') 

app.run(debug=True)
#IDEIA -> posso usar