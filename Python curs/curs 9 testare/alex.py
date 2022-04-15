from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service = s)
chrome.maximize_window()

# chrome.get('https://jules.app/sign-in')
#
#  # selector by Partial Link Text
# chrome.find_elements(By.PARTIAL_LINK_TEXT,'forgot')[0].click()
#
#
# sleep(3)
#chrome.quit()

# chrome.get('https://jules.app/')
# chrome.find_element(By.PARTIAL_LINK_TEXT,'Sign').click()
# #pas = chrome.find_elements(By.PARTIAL_LINK_TEXT,'Sign')
#
# #print(len(pas))
# sleep(3)
# chrome.quit()

#4 Selectors by Tag NAME -NU SE COMPLETEAZA FORMULAR!


# navigam catre un url
chrome.get('https://www.phptravels.net/signup')

# selector by name
chrome.find_elements(By.CLASS_NAME, 'form-control')

sleep(2)

# gasim mai multe si punem in lista
lista_formular = chrome.find_elements(By.TAG_NAME, 'input')
lista_formular[1].send_keys('Alex')
lista_formular[2].send_keys('Dorin')
lista_formular[3].send_keys('0767365348')
lista_formular[4].send_keys('alecs.patrascoiu@yahoo.ro')
lista_formular[5].send_keys('parolaMea!')

sleep(3)
chrome.quit()