#liste
#
# liste_inlista = [
#     [1.23], [4.5.6],['a,b,c']
# ]
#






# SET {}



# vocale ={'a','e','i','o','u'}
# type(vocale)
# print(type(vocale))
# #print(vocale[0])        # am accesat elementul din pozitia 0 dar nu ne lasa programul pt ca nu se poate
# vocale.add('a')
# print(vocale)
# litera= input('va rog sa introduceti o litera'.upper())
# if litera in vocale:
#    print('litera este o vocala')



# tuplu:    este imutabil,
        # nu se poate schimba,
        # permite valori
        # este ordonata

#ex
camere_hotel = (1,2,3,4,5,5)
print(camere_hotel[0])
print(camere_hotel.count(5))
print(camere_hotel.index(3))
print(len(camere_hotel))


#dict  {}     Dictionare

# structura care stocheaza informatii in formatul cheie: evaluare
#
# capitale = {
#     'Romania': 'Bucuresti',
#     'Italia': 'Roma',
#     'Ukraina': 'kiev'
# }
# print(capitale['Romania'])  #accesarea informatiilor din dictionar in functie de cheie
# print(capitale.get('Romania')) # idem
#
# #cum sa actualizam o informatie
# capitale['Romania']='Cluj'  #inlocuim o valoare pe baza de cheie
# print(capitale)
# print(capitale['Romania'])
#
# # cum adaugam o informatie noua
#
# capitale['Rusia']= 'Moscova'
# print(capitale['Rusia'])
# print(capitale)
# print(len(capitale))
#
# # Cum putem sa stergem o informatie
#
# capitale.pop('Rusia')
# print(capitale)
#
# def calculeazasuma(a,b):
#     return a+b
# print(calculeazasuma(5,6))

note = ['do','re','mi','fa']
invers = note[::-1]
print(invers)
invers.reverse()
print(invers)