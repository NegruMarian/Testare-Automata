# # operatori si asignare
# import math
# x = 3 #stocare de calori la o anumita adresa de memorie
# print(x)
# x = x + 3  #crestem valoarea lui x cu 3
# print(x)
# x += 3 #crestem valoarea lui x cu 3
# print(x)
# x = x-3
# print(x)
# x -= 3
# print(x)
# x = x * 3
# print(x)
# x *= 3
# print(x)
# x = x/3
# print(x)
# x /=3
# print(x)
# print('-----------------------')
#
#
# #operatori aritmetici
# print(10 % 3)
# print(2**3)  # 2 la puterea 3
# x = 9
# print(x**(1/2)) #radical din x
# print('----------')
# #operatori de comparare
# x = 5
# y = 3
# print(x==y)  #oparot de comparatie
# x = y
# print(x==y)
# x=5
# print(x != y) #verifica daca valorile sunt diferite
# print(x<y)
# print(x<=y)
# print(x>y)
# print(x>=y)
#
#
# print('operatori logici')
#
# '''
# Operatori logici sunt : and, or, not
# Intotdeauna operatorul and are prioritate in fata lui or
# '''
# print(x<2 and x<y) #ambele conditii trebuie sa fie TRUE ca sa dea in final TRUE
# print(x>2 and x<y)
# print(x>2 and x<y or y>2)
# print('--------')
# passaport = input('Introduceti validarea pasaportului: DA/NU')
# ambii_parinti = input('Are ambii parinti? DA/NU')
# permisiunea = input('Are permisiunea? DA/NU/NA')
# if passaport =='DA' and (ambii_parinti == 'DA' or permisiunea == 'DA'):
#     print('Permite calatoria')
# else:
#     print('Nu permite calatoria')



NOTA_DE_TRECERE = 5 #o constanta se scrie cu litere mari si se doreste sa nu fie schimbata
NOTA_TRECERE_PURTARE = 7
nota_examen = int(input('introdu nota la examen'))
nota_purtare = int(input('intro nota la purtare'))
if nota_examen >= NOTA_DE_TRECERE and nota_purtare >= NOTA_TRECERE_PURTARE:
    print('bravo, ai trecut')
    if nota_examen == 10 and nota_purtare == 10 :
        print('felicitari estei premiat')
else:
    print('nu ai trecut clasa!')