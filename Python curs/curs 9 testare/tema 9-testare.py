# https://www.phptravels.net/
# http://automationpractice.com/index.php
# https://formy-project.herokuapp.com/
# https://the-internet.herokuapp.com/
# https://www.techlistic.com/p/selenium-practice-form.html
# jules.app
#
# (obs: nu 3 pe fiecare pagina, 3 in total, de pe ce site doriti, la alegere. Nu toate sites vor avea elemente cu atributul name de ex)
#
# 3 selectors by:
# Id
# Link text
# Partial link text
# Name
# Tag*
# Class name*
# Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
#

#### By Class_name
#1
# chrome.get('http://automationpractice.com/index.php')
#sleep(3)
# first_name = chrome.find_elements(By.CLASS_NAME, 'sf-with-ul')
# stocare_elemente = chrome.find_elements(By.CLASS_NAME, 'sf-with-ul')
# print(len(stocare_elemente))
# sleep(3)
# chrome.quit()
#
#2
# chrome.get('https://jules.app/')
# sleep(3)
# chrome.find_elements(By.CLASS_NAME,'MuiInputBase-input')[0].send_keys('marian@gmail.com')
# sleep(2)
# test = chrome.find_elements(By.CLASS_NAME,'MuiInputBase-input')[1].send_keys('password')
# sleep(2)
# chrome.quit()

#3
# chrome.get('https://the-internet.herokuapp.com/tinymce')
# chrome.find_element(By.CLASS_NAME,'tox-mbtn__select-label').click()
# sleep(3)
# chrome.quit()

###      By ID

# #1

# chrome.get('https://www.phptravels.net/')
# test = chrome.find_element(By.ID,"languages" ).click()
# sleep(5)
# chrome.quit()

#2

# chrome.get('https://the-internet.herokuapp.com/dropdown')
# chrome.find_element(By.ID, 'dropdown').click()
# sleep(3)
# chrome.quit()

#3
# chrome.get('https://the-internet.herokuapp.com/dynamic_loading/1')
# chrome.find_element(By.ID,'start').click()   #  nu da eroare dar nici nu da click....d c?
# sleep(3)
# chrome.quit()

#         BY  Link text


#1
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT,'A/B Testing').click()
# sleep(3)
# chrome.quit()
#
#2
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT,'Context Menu').click()
# sleep(2)
# chrome.quit()
#
#3
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT,'Typos').click()
# sleep(3)
# chrome.quit()
#

#4
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(5)
# chrome.find_element(By.LINK_TEXT,'Automate Amazon like E-Commerce website with Selenium').click()  #nu merge pe acestsite, am incercat mai multe link-uri
# sleep(5)
#chrome.quit()
####
#5
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')    #putem sa scapam de reclame/politica de confidentialitate ca sa ruleze mai departe?
# sleep(10)
# chrome.find_element(By.LINK_TEXT,'Automate Google search with Selenium').click()
# sleep(8)
#chrome.quit()
##

##  BY Partial Link Text

#1
# chrome.get('https://the-internet.herokuapp.com/dynamic_loading')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Example 1').click()
# sleep(3)
# chrome.quit()

#2
# chrome.get('https://the-internet.herokuapp.com/dynamic_loading')
# chrome.find_element(By.PARTIAL_LINK_TEXT,'after the fact').click()
# sleep(3)
# chrome.quit()
#3
# chrome.get('https://jules.app/sign-in')
# chrome.find_element(By.PARTIAL_LINK_TEXT,'password').click()
# sleep(3)
# chrome.quit()






# *La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista
#
# La Xpath:
# 3 dupa atribut valoare
# 3 dupa textul de pe element
# 1 dupa partial text
#
#
# 1 cu SAU, folosind pipe |
# 1 cu *
# 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
# 1 in care sa folosesti parent::
# 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
# 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
#
# Studiu extra daca doriti:
# https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/
#
#
