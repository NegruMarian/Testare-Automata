from browser import Browser
from selenium.webdriver.common.by import By


class Forgot_password_page(Browser):
    FORGOT_PASS = (By.XPATH,'//*[@id="content"]/ul/li[20]/a')

    def click(self):
        self.driver.find_element(*self.FORGOT_PASS).click


class Form_Authentication(Browser):
    Form_Authentication = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')

    def click(self):
        self.driver.find_element(*self.Form_Authentication).click()


class A_B_Testing(self):
    A_B_Testing = (By.XPATH,'//*[@id="content"]/ul/li[1]/a')

    def click(self):
        self.drive.find_element(*self.A_B_Testing).click

     ##### nu merge, ramane pagina web deschisa si nu se intampla nimic......

