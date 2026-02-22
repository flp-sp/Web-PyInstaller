from flask import Flask, render_template, request, session, redirect, url_for
from git import Repo
import requests
import docker
from core.methods import limpar_src

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
        limpar_src()
        if session.get('want_linux') or session.get('want_win') or session.get('want_alpine'):
            return redirect(url_for('convert'))


    return render_template("config.html")

@app.route('/convert')
def convert():
    #tenta puxar o repositorio para previnir links errados
    try:
        clone_repo = Repo.clone_from(session.get('repo'), "./src")
    except:
        return redirect(url_for('config'))

    env_platforms = [] # lista da env PLATAFORMS
    if session['want_linux']:
        env_platforms.append("linux")
    if session['want_win']:
        env_platforms.append("win")
    if session['want_alpine']:
        env_platforms.append("alpine")

    single_env = ", ".join(env_platforms) # env PLATAFORMS em uma string pronta para bash

    cliente = docker.from_env()
    cliente.containers.run("fydeinc/pyinstaller", 
                                command="main.py", 
                                volumes={'/home/flp-sp/Projects/webpyinstaller/app/src' : {'bind' : '/src', 'mode' : 'rw'}}, 
                                environment=[f"PLATFORMS={single_env}"])
    
    res = requests.get(request.host_url + url_for('convert')).status_code
    if res == 200:
        return "download"

    return render_template("convert.html")