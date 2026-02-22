from flask import Flask, render_template
from main import app

@app.route('/') # rota da pagina inicial
def index():
    return render_template("index.html")