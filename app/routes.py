#neste arquivos ficam as rotas
from app import app
from flask import render_template
#o primeiro app é a pasta e o segundo é o criado no microblog
#podemos colocar várias rotas

@app.route('/index')
@app.route('/')
def index():
    user = {'username':'Sabrina'}
    return render_template("index.html",user=user)