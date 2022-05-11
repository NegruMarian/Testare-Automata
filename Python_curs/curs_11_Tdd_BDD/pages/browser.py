
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser():
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.set_page_load_timeout(5)
    chrome.maximize_window()
    chrome.get("https://the-internet.herokuapp.com/")



    Form_Authentication = (By.XPATH,'//*[@id="content"]/ul/li[21]/a')
    Forgot_Password = (By.XPATH,'//*[@id="content"]/ul/li[20]/a')
    A_B_Testing = (By.XPATH,'//*[@id="content"]/ul/li[1]/a')

    # def close(self):
    #     self.chrome.quite()
    #
    # def setUp(self):
    #     self.s = Service(ChromeDriverManager().install())
    #     self.chrome = webdriver.Chrome(service=self.s)
    #     self.chrome.maximize_window()
    #     self.chrome.get('https://the-internet.herokuapp.com/')
    #
    #
    # def tearDown(self):
    #     self.chrome.quite

# avem sau nu nevoie de setup sau tearDown?






