# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 1 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video cu Variabile si Tipuri de date din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video cu Operatori si Flow Control din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# b. Usor spre Mediu (obligatoriu)
# 1.
# In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# print('1.O variabila este ca o cutiuta in memoria calculatoului caruia ii putem da valori si ep care o putem accesa ulterior.
# In functie de tipul valorii pe care o dam se modifica memoria ocupata.')
#
# 2.
# Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte

# a = 'este de tip string'
# b = 4
# c = 542.2
# d = b < c


# 3.
# Utilizat functia type pentru a verifica ca ele au tipul de date asteptat
        #valorile lui a,b,c,d sunt de le ex. 2

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# 4.
# Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia
   #valoarea lui c este de la ex.2

# c = round(c)
# print(c)
# print(type(c))

#
# 5.
# folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)
    #pentru a putea printa trebuie sa ruleze exercitiile de mai sus pt a,b si c sunt variabilele de mai sus
# print("Prima variabila este 'a' si",a)
# print("Variabila 'b' nu este folosita la exercitiul nr.",b)
# print(f"La exercitiul nr.4 am folosit variabina 'c' care are valoarea {c} dupa ce a fost rotunjita.")
# print(f"Pentru ca",b,"este mai mic decat",c,"rezulta ca valoarea variabilei 'd' este True.")

#
# 6.
# citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'

# nume = input('Numele')
# prenume = input("Prenumele")
# print('Numele complet are',len(nume)+len(prenume),'caractere')


#
# 7.
# citeste de la tastatura lungimea
# citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'

# L = int(input('Lungimea'))
# l = int(input('latimea'))
# aria = L*l
# print(f'Aria dreptunghiului este {aria}')


# 8.
# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

# prop = 'Coral is either the stupidest animal or the smartest rock'
# nr = int(input('introdu numarul'))
# print (prop[:-nr])


#
# 9.
# acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5

# prop1 = 'Coral is either the stupidest animal or the smartest rock'
# caracter1 = prop1[:5]
# caracter2 = prop1[-5:]
# print(caracter1+caracter2)


#
# 10.
# acelasi string
# afisati de cate ori apare cuvantul 'the'

# prop2 = 'Coral is either the stupidest animal or the smartest rock'
# print((prop2.count('the')))


#
# 11.
# acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul

# prop3 = 'Coral is either the stupidest animal or the smartest rock'
# new = prop3.replace('the','THE')
# print(new)
# print(prop3.replace('the','THE'))


#
# 12.
# acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '

# prop4 = 'Coral is either the stupidest animal or the smartest rock'
# x = prop4.index('rock')
# print(x)
# print(prop4[:53])


#
# 13.
# citeste de la tastatura un string
# verifica daca primul si ultimul caracter sunt la fel
# se va folosi un assert
# atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat

# varianta 1 de rezolvare
# my_str= input('scrie ce vrei')
# assert my_str.casefold()[0]==my_str.casefold()[-1]
# print(f'primul caracter {my_str[0]} este la fel cu ultimul caracter {my_str[-1]}')

# varianta 2
# my_str = input('scrie ce vrei')
# my_str2 = my_str.lower()
# assert my_str2[0]==my_str2[-1]
# print('sunt la fel')


#
# 14.
# avand stringul '0123456789'
# afisati doar numerele pare
# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)

# nr = '0123456789'
# print(nr[2::2])
# print(nr[1::2])

#
# 15.
# acelasi string de la 12
# folositi un assert ca sa verificati daca acest string contine doar numere
# hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
# poate gasim o functie ajutatoare
# nr2 = '0123456789'
# assert nr2.isdigit()
# print(nr2.isdigit())
# print(nr2.isalnum())

#
#
#
# c. Optionale (may need google)
# 16.
# citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc


# def middleChar(string):
#     string = input("scrie ceva")
#     return string[(len(string) // 2)]
# print(middleChar('string'))

#rezolvat

#
# 17.
# Folosind assert, verificati daca un string este palindrom

# x = 'mAmAm'
# assert x.lower() == x[::-1].lower()
# print('sunt la fel')
#rezolvat


# 18.
# folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare

# a,b = input("introdu stringul").split()
# print(a)
# print(b)
# print(a,b)

# rezolvat



#


# 19.
# citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA

# #
# a = input('scrie un string')
# firs_charct = a[0]
# mid_charact = a[1:-1]
# last_charact = a[-1:]
# c = mid_charact.replace(firs_charct,firs_charct.upper())
# print(firs_charct+c+last_charact)





#
# 20.
# citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****

# username = input('username:')
# password = input('password')
# # varianta 1
# cript_pass = password.replace(password,'*')*len(password)
#varianta 2
# cript_pass = password.join('*') * len(password)
#
#print(f'Password for user {username} is: {cript_pass}')








