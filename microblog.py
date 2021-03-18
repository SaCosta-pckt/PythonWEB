from flask import Flask

app = Flask("microblog")


# @ em python é algo chamado "decorator", é como de fosse um operador do python que fica em cima da função e faz algo com ela
@app.route("/") #toda vez que a pessoa entrar na url e não tiver nada depois da barra, ele vai executar a função
def index():
    return "Hello World"

app.run()
#executar na web: escrever na url "localhost:5000"

