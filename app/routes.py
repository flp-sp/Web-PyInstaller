from flask import Flask, render_template, request, session, redirect, url_for
from main import app

@app.route('/') # rota da pagina inicial
def index():
    return render_template("index.html")

@app.route('/config', methods=['GET','POST']) # rota da pagina de configurar o projeto para conversão
def config():
    if request.method == 'POST':
        session['repo'] = request.form.get('repositorio') # link do repositorio

        # armazena variaveis booleanas no session para as plataformas selecionadas a partir do checkbox
        session['want_linux'] = bool(request.form.get('cLinux'))
        session['want_win'] = bool(request.form.get('cWindows'))
        session['want_alpine'] = bool(request.form.get('cAlpine'))
    return render_template("config.html")