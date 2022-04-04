# def printGreeting():
#     print('Buna ziua!')
#
# def printGreetingByName(nume,prenume):
#     print(f'Buna ziua {nume} {prenume}')
#
# def mediaNr(a,b,c):
#     return (a+b+c)/3
#
# def piValue():
#     return 3.14
#
# #exercitiu
#     #daca persoana este majora, altfel fals
# # def verificareMajor(varsta):
# #     if varsta >= 18:
# #         return True
# #     else:
# #         return False
#
#
#     printGreeting()
# printGreeting()
# printGreetingByName("Marian", "Negru")
# printGreetingByName("Iris", "Alexandra")
# printGreetingByName("negru", "Mihaela")
# print(mediaNr(3,3,4))
# print(piValue())
#print(verificareMajor(17))

# acces in functie de varsta - Nu returneaza nimic
def VarstaMinimaNecesara(varsta):
    varsta = int(input("introdu varsta")) #nu merge sa accesezi varsta de la input
    if varsta >= 18:
         return True
         print("bine ai venit")
    else:
     return False
     print('nu ai varsta minima de acces')

