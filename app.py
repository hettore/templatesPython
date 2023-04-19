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

produtos = {
    1: {
        "nome": "Iphone 14 PRO",
        "descricao": "Iphone 14, modelo PRO MAX, na cor vermelha",
        "preco": 7800.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    2: {
        "nome": "Samsung Galaxy S21",
        "descricao": "Samsung Galaxy S21, modelo com 5G, na cor preta",
        "preco": 5500.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    3: {
        "nome": "MacBook Pro",
        "descricao": "MacBook Pro 16 polegadas, processador M1 Max, na cor prata",
        "preco": 15999.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    4: {
        "nome": "Sony PlayStation 5",
        "descricao": "Console Sony PlayStation 5, com controle DualSense, na cor branca",
        "preco": 4499.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    5: {
        "nome": "Amazon Echo Dot",
        "descricao": "Caixa de som inteligente Amazon Echo Dot, com assistente virtual Alexa, na cor azul",
        "preco": 349.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    6: {
        "nome": "Nvidia GeForce RTX 3080",
        "descricao": "Placa de vídeo Nvidia GeForce RTX 3080, 10GB GDDR6X, na cor preta",
        "preco": 7299.00,
        "imagem": "https://placehold.co/600x400.png"
    }
}

@app.route("/")
def deu_certo():
    #Estamos retornando o arquivo HTML já renderizado
    return render_template('exemplo.html', textinho = frase)

@app.route("/produto")
def exibe_produto():
    return render_template("produto.html", **produto)

@app.route("/produto_boot")
def exibe_produto_boot():
    return render_template("produto_boot.html", **produto)

@app.route("/produtos/<int:produto_id>")
def exibe_produtos_por_id(produto_id):
    return render_template("produto_boot.html", **produtos[produto_id])

@app.route("/produtos")
def exibe_todos_produtos():
    return render_template("produtos_boot.html", produtos=produtos)

app.run(debug=True)

