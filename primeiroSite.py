from flask import Flask

app = Flask(__name__)
#route -> saolourencodaserradoacoes.com/contatos
#função -> o que você quer exibir naquela página

@app.route("/")
def homepage():
    return "Aqueça seu coração"

@app.route("/contatos")
def contatos():
    return "Nossos contatos são: E-mail: trabalhounivesp@gmail.com Telefone(11)99999-9999"

@app.route("/quem_somos")
def informações():
    return "Somos um canal de doação focado em conectar doadores a receptores e assim facilitar o modo como as doações são destinadas, fazendo a ponte para que as pessoas recebam o que de fato precisam.   "

@app.route("/quero_receber")
def receptores():
    return "Aqui você pode escolher quais são suas necessidades e aguardar um doador"

@app.route("/quero_doar")
def doares():
    return "Aqui você apoia um receptor e faz sua doação"


#colocar o site no ar

if __name__=="__main__":
    app.run(debug=True)