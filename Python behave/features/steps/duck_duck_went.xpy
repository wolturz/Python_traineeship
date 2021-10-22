from behave import *
from splinter.browser import Browser                                # importeer de Browser klasse
import time

@given('Chrome has been opened')
def step_impl(context):
    context.browser = Browser('chrome')                             # instantieer een browser object

@given('Duck Duck Go is being displayed')
def step_impl(context):
    context.browser.visit("https://duckduckgo.com")                 # laat de browser naar een URL navigeren

@then(u'Look {first} up')
def step_impl(context,first):
    context.browser.fill('q', first)        # vul een zoektekst in
    button = context.browser.find_by_id('search_button_homepage')  # Zoek de Zoek knop
    button.click()                                         # Druk op de knop

@then(u'wait for {number} seconds for check')
def step_impl(context,number):
    time.sleep(int(number))               # wait 5 seconds
    context.browser.quit()
