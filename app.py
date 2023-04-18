#Importamos o Flask para criar um webApp e o render_template para renderizar
#nossos templates HTML
from flask import Flask, render_template

app = Flask(__name__)

frase = "Hoje meu time joga. Que tristeza."

produto = {
	"id":1,
	"nome":"Iphone 14 PRO ",
	"descricao":"Iphone 14, modelo PRO MAX, na cor vermelha",
	"preco":7800.00,
	"imagem":"https://upload.wikimedia.org/wikipedia/commons/3/37/Back_of_the_iPhone_14_Pro.jpg"
}

@app.route("/")
def deu_certo():
    #Estamos retornando o arquivo HTML já renderizado
    return render_template('exemplo.html', textinho = frase)

@app.route("/produto")
def exibe_produto():
    return render_template("produto.html", **produto)

app.run(debug=True)

