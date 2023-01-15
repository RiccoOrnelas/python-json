from flask import Flask
import urllib.request, json
 
url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=10aba4bf54dc9da3a26637a1945cda93"
resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)
print(jsondata["results"])
