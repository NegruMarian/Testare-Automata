# 1.	Avand ca exemplu pagina https://the-internet.herokuapp.com/login
#
# Feature: User Authentication
#
# Mergeti backwards si ganditi ca un product owner
#
# Generati un epic (doar o propozitie care sa descrie functionalitatea majora ce urmeaza sa fie dezvoltata)
# Test user authentication proces!
#
# Generati un user story pentru login care sa aiba 2 acceptance criteria
from behave import given,when,then
# -	Un login valid (positive)
#user story:
# 'As a client'
# 'I whant to login in my account'
# 'So that help me see my order '

#acceptance criteria
@given ('I am on the login page')
@when ('I populate login form whit valid credentials')
@then ("message is 'login is successful'")

@given ('I am on url page https://the-internet.herokuapp.com/login')
@when ('I populate login form with valid credentials')
@then ("after login new url page is 'https://the-internet.herokuapp.com'")


# -	Un login Invalid (negative)

#User story

"""As an existing customer'
I whant to login with a new email addres
So that helps me see if the email addres is valid """

#acceptance criteria

@given ('I enter the website')
@when ('I try to login with a new email addres')
@then ('I`ll see if I can log in')


# Generati un alt user story care sa acopere functionalitatea de register. Sa contina 2 acceptance criteria
# -	Email e nou, deci user poate face register (positive)
"""As a new customer
I whant to creat an account with a new email addres
So that let me by """

@given ('I enter the website on the new account page')
@when ('I populate the form with my email addres')
@then ('I click the register button')

@given('I launch the chrome browser')
@when('I open https://the-internet.herokuapp.com/login and I populate the form with my email addres and click login button')
@then('I must be logged in')


# -	Email e deja existent in baza de date (negative)
"""As a new client
I whan to creeate an account with my email address whitch is allready registered
and I receive the message 'email address is already registered """

@given('I open the chrome browser')
@when('I populate with my email address')
@then('I receive the message "Your email address is already registered')

# Generati un ultim user story care sa acopere functionalitatea de reset password. Sa contina 2 acceptance criteria
""" As a user 
    I want to replace my password
    with a new one
    """
# -	Email e in baza de date
@ghive ('open https://the-internet.herokuapp.com/login')
@when  ('clic forgot password, button')
@then ('I populate the form with my email address and click the button')

@given ('after I populate with my email address and click the button')
@when ('I receive a message to enter my new password')
@then('I can login with new password')


# -	Email nu e in baza de date
@give ('I open the https://the-internet.herokuapp.com/login')
@when('I click the forgot password and I introduce my email address')
@then ('I receive the message - Your email address is invalid')

@given('I open the ')
#
# Reminder:
# Un user story are forma
# As a …
# I want to …
# So that …
#
# Un Acceptance criteria are forma
# Given …
# When …
# Then …
#
# 2.	Implementați 3 pagini în noul proiect BDD cu POM
# a.	Home page https://the-internet.herokuapp.com/
# -	Sa aiba cel putin 3 elemente inclusiv Form Authentication
# -	Sa contina metode de click pe ele
# b.	Login page https://the-internet.herokuapp.com/login
# -	Sa contina user, pass, login_btn si metode pt interactiune cu ele
# c.	Secure page https://the-internet.herokuapp.com/secure
# -	Sa contina mesajul de succes si verificare ca e displayed
# -	Sa contina logout_btn si click pe el
