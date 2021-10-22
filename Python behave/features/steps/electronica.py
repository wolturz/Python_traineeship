from behave import *
import requests

# # api-endpoint
# URL = "http://dingdata.nl/batterij?"
# URL = URL + "UB=5"+ "&" + "RI=2.5" + "&" + "RL=13" 

# # Request uitvoeren
# r = requests.get(url = URL)
# response = r.json()

def url_maker(uk,rl):
    URL = "http://dingdata.nl/batterij?"
    URL = URL + "UK=" + str(uk) + "&" + "RL=" +  str(rl)
    return URL

def response_maker(URL):
    r = requests.get(url = URL)
    response = r.json()
    return response

@given('the battery calculation module is online and available')
def step_impl(context):
    URL = "http://dingdata.nl/batterij?"
    URL = URL + "UB=5" + "&" + "RI=2.5" + "&" + "RL=13" 
    response = response_maker(URL)


@when(u'I call the battery calculation module with {Uk} and {Rl}')
def step_impl(context,Uk,Rl):
    URL = url_maker(float(Uk),float(Rl))
    context.response = response_maker(URL)
    context.klem = Uk
    context.weerstand = Rl
    context.antwoord = context.response['resultaten']['antwoord'][4:7]

@then(u'The module calculates the correct value of {I}')
def step_impl(context,I):
    assert I == context.antwoord
    

