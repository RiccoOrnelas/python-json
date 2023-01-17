from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=10aba4bf54dc9da3a26637a1945cda93"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=10aba4bf54dc9da3a26637a1945cda93"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=10aba4bf54dc9da3a26637a1945cda93"
    elif propriedade == 'melhores2010': 
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=10aba4bf54dc9da3a26637a1945cda93"
    
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])

@app.route("/home")
def home():
    return render_template("home.html")

app.run(debug=True)