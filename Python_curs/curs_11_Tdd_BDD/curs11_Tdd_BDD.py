# Test Driven Development (TDD) = Abordare in care scriem testele inainte sa scriem codul. Rulam testele, ele sunt failed pentru ca nu avem codul dezvoltat, apoi se creeaza codul, se actualizeaza testele cu metoda de identificare a elementelor, apoi se reexecuta, moment in care ne asteptam sa fie passed
#
# Behaviour Driven Development (BDD) = O extensie a TDD care se implementeaza prin definirea unor fisiere descriptie legate de codul de automatizare. Fisierele sunt definite pe baza unor user stories scrise in limbajul gherkin
#
# User Story = descriere a unui scenariu de business din punctul de vedere al utilizatorului
#
# Structura simplista a unui feature file:
# GIVEN I am a user
# WHEN I perform an action
# THEN I expect to gain a benefit
#
#
#
# from browser import Browser
# from selenium.webdriver.common.by import By
#
#
# class Sign_in_page(Browser):
#     EMAIL_INPUT = ()
#     PASS_INPUT=()
#     LOGIN_BUTTON = ()
#     FORGOT_PASSWORD_LINK=()
#
#
#     def navigate_to_sign_in_page(self):
#         self.driver.get("")
#
#     def set_email(self,email):
#         self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
#
#     def set_pass(self,password):
#         self.driver.find_element(*self.PASS_INPUT).send_keys(password)
#
#     def click_login_button(self):
#         self.driver.find_element(*self.LOGIN_BUTTON).click()
#
#     def click_forgot_password_link(self):
#         self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
#
#     # step definition (o agregare de pasi mici care au logica sa fie sub o singura umbrela/functie)
#     def user_login(self,username, email, password):
#         self.set_email(email)
#         self.set_pass(password)
#         self.click_login_button()

# from browser import Browser
# from selenium.webdriver.common.by import By
#
# class Forgot_password_page(Browser):
#     FORGOT_PASS_LINK = (By.LINK_TEXT,"Forgot password?")
#     EMAIL_INPUT = (By.XPATH, "//input[@placeholder ='Enter your email']")
#     SEND_EMAIL_BTN = (By.XPATH,"//*[@id="root"]/div/div[2]/div/div[2]/button")
#
#     def set_email(self,email):
#         self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)



#from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from time import sleep
#
# class Browser():
#     s = Service(ChromeDriverManager().install())
#     chrome = webdriver.Chrome(service=s)
#     chrome.maximize_window()
#     chrome.implicitly_wait(5)
#     chrome.set_page_load_timeout(10)
#     chrome.maximize_window()
#     chrome.get("https://jules.app/")
#
#     def close(self):
#         self.chrome.quit()
#
#     def click_send_email_button(self):
#         self.driver.find_element(*self.SEND_EMAIL_BTN).click()


