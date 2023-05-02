from flask import Flask, render_template

app = Flask(__name__)
#route -> saolourencodaserradoacoes.com/contatos
#função -> o que você quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/quem_somos")
def informações():
    return "Somos um canal de doação focado em conectar doadores a receptores e assim facilitar o modo como as doações são destinadas, fazendo a ponte para que as pessoas recebam o que de fato precisam.   "

@app.route("/quero_receber")
def receptores():
    return "Aqui você pode escolher quais são suas necessidades e aguardar um doador"

@app.route("/quero_doar")
def doadores():
    return "Aqui você apoia um receptor e faz sua doação"

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


#colocar o site no ar

if __name__=="__main__":
    app.run(debug=True)

    #servidor heroku