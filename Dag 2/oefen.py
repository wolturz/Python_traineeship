##import requests
##
### api-endpoint
##URL = "http://dingdata.nl/batterij?"
##
##URL = URL + "UK=5.0"+ "&" + "RL=2.5" 
##
### POST body klaarmaken en POST versturen
##part_data = {
##	"nummer":48,
##	"naam":"cranc",
##	"omschrijving":"Trapper cranc aluminimum",
##	"aantal":12
##}
##
### Request uitvoeren
##r = requests.get(url = URL)#, json = part_data)
##
##response = r.json()
##Uk = response['resultaten']['antwoord']
##print(Uk[4:7])

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hallo_wereld():
    return "Hallo, wereld"

##from flask import Flask
##app = Flask(__name__)
##
##@app.route("/")
##def hallo_wereld():
##	return '''
##	<html><body>
##		<h1>Hallo wereld</h1>
##		<p>Dit is een webpagina waar we nog heel veel plezier van gaan hebben
##		in het vervolg van deze training!</p>
##	</body>
##	</html>
##	'''
