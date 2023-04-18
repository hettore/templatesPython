#Importamos o Flask para criar um webApp e o render_template para renderizar
#nossos templates HTML
from flask import Flask, render_template

app = Flask(__name__)

frase = "Hoje meu time joga. Que tristeza."

@app.route("/")
def deu_certo():
    #Estamos retornando o arquivo HTML já renderizado
    return render_template('exemplo.html', textinho = frase)

app.run(debug=True)

