#esse arquivo inicializa o app
#__init__ é o primeiro arquivo que é rodado na pasta
# esses nomes especiais são chamados de python magic

from flask import Flask

app = Flask("__name__")

from app import routes