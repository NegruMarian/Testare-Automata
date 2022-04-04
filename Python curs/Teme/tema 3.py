# # a. Usor (recomandat)
# # 1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
# # 2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare'
# # (Daca nu ai facut-o deja)
# # 3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'
# # Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# # si sigur ti se vor intipari in minte mai bine.
# # https://www.itfactory.ro/8174437-intro-in-programare/
# #
# # b. Usor spre Mediu (obligatoriu)
#
#
#
#
#
# # 1.
# # Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# # Afiseaz-o
# # Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# # Printeaza varianta actuala (inversata)
# # Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# # Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
# # Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
#
# #note_muzicale = ['do','re','mi','fa','so','la','si','do']
# # inversate = note_muzicale[::-1]
# # print(inversate)
# # inversate.reverse()
# # print(inversate)
#
# #rezolvat
#
#
#
#
# # 2.
# # De cate ori apare ‘do’?
# #print(note_muzicale.count('do'))
#
# #Rezolvat
#
# # 3.
# # Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# # Gasiti 2 variante sa le uniti intr-o singura lista.
# # # Afisati lista ordonata astfel [0,1,2,3,4,5,6]
# list1 = [3,1,0,2]
# list2 = [6,5,4]
# # prima optiune este concatenarea: list1+list2
# # a doua optiune este functia extend: list1+list2
# #list1.append(list2) # prima varianta de unire intr-o singura lista
# #print(list1)
# list1.extend(list2)  # a doua varianta de unire intr-o singura lista
# print(sorted(list1))
#
#
# #Rezolvat
#
#
# # 4.
# # Sortati si afisati lista generata la ex anterior
# # Stergeti numarul 0 folosind o functie
# # Afisati iar lista
# #print(sorted(list1))
# #list1.remove(0)
# # sau
# # list1.pop(2)
# # print(list1)
# # # varianta 2
# # print(list1[1:7])
# #Rezolvat
#
#
# # 5.
# # Folosind un if verificati lista generata la ex3 si afisati
# # Lista este goala
# # Lista nu este goala
#
# # if len(list1) == 0:
# #     print('Lista este goala')
# # else:
# #      print('Lista nu este goala')
#
# # Rezolvat
# #
# #
# # 6.
# # Folositi o functie care sa stearga lista de la ex3
# #del list1
# list1.clear()
#
#
# #Rezolvat
#
# #
# # 7.
# # Copy paste la ex 5. Verificati inca o data.
# # Acum ar trebui sa se afiseze ca lista e goala
#
# if  len(list1) == 0:
#      print('Lista este goala')
# else:
#      print('Lista nu este goala')
# #
# #Rezolvat
#
# # 8.
# # Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# # Folositi o functie ca sa afisati Elevii (cheile)
# #
# # dict1 = {'Ana':8, 'Gigel': 10, 'Dorel': 5}
# # print(dict1.keys())
#
#
# #Rezolvat
#
#
# # 9.
# # Printati cei 3 elevi si notele lor
# # Ex: ‘Ana a luat nota {x}’
# # Doar nota o veti lua folosindu-va de cheie
# #
# # print(f"Ana a luat nota {dict1['Ana']}")
# # print(f"Gigel a luat nota {dict1['Gigel']}")
# # print(f"Dorel a luat nota {dict1['Dorel']}")
# # rezolvat
# #
# # 10.
# # Dorel a facut contestatie si a primit 6
# # Modificati nota lui Dorel in 6
# # Printati nota dupa modificare
# # dict1['Dorel'] = 6
# # print(dict1['Dorel'])
# #rezolvat
#
# # 11.
# # Gigel se transfera din clasa
# # Cautati o functie care sa il stearga
# # Vine un coleg nou. Adaugati Ionica, cu nota 9
# # Printati noii elevi
# # dict1.pop('Gigel')
# # dict1['Ionica']=9
# # print(dict1)
#
# #rezolvat
# #
# # 12.
# # Set
# # zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# # weekend = {'sambata', 'duminica'}
# # Adaugati in zilele_sapt ‘luni’
# # Afisati zile_sapt
# # zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# # weekend = {'sambata', 'duminica'}
# # zile_sapt.add('luni')
# #print(zile_sapt)
#
# #
# # 13.
# # Folositi un if si verificati daca
# # Weekend este un subset al zilelor din sapt
# # Weekend nu este un subset al zilelor din sapt
# # if weekend.issubset(zile_sapt):
# #     print('Weechend este un subset al zilelor din sapt')
# # else:
# #     print('Weechend nu este subset al zilelor din sapt')
# #
# # 14.
# # Afisati diferentele dintre aceste 2 seturi
# # print(zile_sapt.difference(weekend))
# #
# # 15.
# # Afisati intersectia elementelor din aceste 2 seturi
# # print(zile_sapt.intersection(weekend))
#
# #
# # c. Optionale (may need google)
# # 16.
# # Ne imaginam o echipa de fotbal pt teren sintetic.
# # 3 Schimbari maxime admise
# #
# # Declara o Lista cu 5 jucatori
# # Schimbari_efectuate = va jucati voi cu valori diferite
# #
# # Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# # Efectuam schimbarea
# # Stergem jucatorul scos din lista
# # Adaugam jucatorul intrat
# # Afisam a intra x, a iesit y, mai aveti z schimbari
# # Daca jucatorul nu e in teren:
# # Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# # Afisati ‘mai aveti z schimbari’
# #
# # Testati codul cu diferite valori
# #
# # Google search hint
# # “how to check if item is in list python”
# #
# # #varianta 1
#
# # echipa = ['player1', 'player2','player3', 'player4','player5', 'player6', 'player7', 'player8','player9']
# # jucatori_in_teren = ['player1', 'player2','player3', 'player4','player5']
# # jucatori_de_rezerva = set(echipa) - set(jucatori_in_teren)
# # schimbari_efectuate = int(input('a cata schimbare este?'))
# # schimbari_ramase = 3 - schimbari_efectuate
# # if schimbari_efectuate <= 3:
# #     jucator_care_intra = input('introdu jucatorul care intra')
# #     jucator_care_iese = input('introdu jucatorul care iese')
# #     if jucator_care_intra in jucatori_de_rezerva and jucator_care_iese in jucatori_in_teren:
# #         jucatori_in_teren.remove(jucator_care_iese)
# #         jucatori_in_teren.append(jucator_care_intra)
# #         print(f'A intrat {jucator_care_intra} si a iesit {jucator_care_iese} si mai aveti {schimbari_ramase} schimbari ')
# #         print(f'Noua lista cu jucatorii in teren este:{jucatori_in_teren}')
# #     else:
# #         print('Jucatorul nu este in teren')
# #         schimbari_initiale = schimbari_ramase+ schimbari_efectuate
# #         print(f'Mai aveti {schimbari_initiale} schimbari')
# # else:
# #     print('Schimbarea nu se poate efectua')
#
#
# # alta varianta
#
# # echipa = ['player1', 'player2','player3', 'player4','player5', 'player6', 'player7', 'player8','player9']
# # jucatori_in_teren = ['player1', 'player2','player3', 'player4','player5']
# # jucatori_de_rezerva = set(echipa) - set(jucatori_in_teren)
# # schimbari_efectuate = int(input('Schimbarea nr:'))
# # schimbari_ramase = 3 - schimbari_efectuate
# # if schimbari_efectuate <= 3:
# #     jucator_care_intra = input('introdu jucatorul care intra')
# #     if jucator_care_intra in jucatori_de_rezerva:
# #         jucator_care_iese = input('introdu jucatorul care iese')
# #         if jucator_care_iese in jucatori_in_teren:
# #             jucatori_in_teren.remove(jucator_care_iese)
# #             jucatori_in_teren.append(jucator_care_intra)
# #             print(f'A intrat {jucator_care_intra} si a iesit {jucator_care_iese} si mai aveti {schimbari_ramase} schimbari.')
# #             print(f'Noua lista cu jucatorii in teren este:{jucatori_in_teren}')
# #         else:
# #             print('jucatorul nu se afla in teren!')
# #     else:
# #         print('Jucatorul nu face parte din echipa sau este deja in teren!')
# #         schimbari_initiale = schimbari_ramase+ schimbari_efectuate
# #         print(f'Mai aveti {schimbari_initiale} schimbari.')
# # else:
# #     print('Nu mai aveti schimbari valabile.')
