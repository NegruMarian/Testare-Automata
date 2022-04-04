# # exercitii de recapitulat!
# # a)	Afiseaz-o
# # b)	Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# # c)	Printeaza varianta actuala (inversata)
# # d)	Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# # e)	Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
# # print(list.reverse(list2))
# # lista = [1,2,3,4]
# # print(lista[::-1])
# # print(list.reverse(lista))
# # lista.reverse()
# # print(lista)
#
#
# ##### STRUCTURI REPETITIVE
#
# # i = 0
# # while i <=3:
# #     print(i)
# #     i+=1
# # else:
# #     print('Am terminat ciclul')
# #
# # #for
# # for i in range(4):  # pe ultimul element nu il afiseaza
# #     print(i)
# # else:
# #     print('am terminat')
#
#
# # ### for each
# # # este folosit pt liste
# # culori = ['verde', 'galben', 'rosu']
# # for culoare in culori:
# #     print(f'culoarea mea preferata este {culoare}')
#
#
#
# #     #breack
# # for i in range(999):
# #     if i ==3:
# #         break
# #     print(i)
#
# # #ex
# note = [7,6,4,10]
# for nota in note:
#     if nota ==4:
#         print('asta este primul student care a picat')
#         break   #cand programul intalneste nota 4 programul se opreste chiar daca dupa mai urmeaza alta nota de 4
#
#
# #CONTINUE
#
note = [7,6,4,10]
for nota in note:
    if nota ==4:
        continue
    print(f'Nota curenta este {nota}')
#
#
# # exemple
# print('---------while------')
# i = 0
# while i <=3:
#     print(f'valoarea curenta a contorului este {i}')
#     i = i+1
#     print(f'valoarea contorului dupa incrementare este {i}')
# else:
#     print('testul a luat sfarsit')  # se executa dupa ce conditia de evaluare nu mai este indeplinita


#print('-----FOR----')
#for i in range(40):
    #print(i)

 #ex 101 dalmatieni
# for i in range(1, 102) :
#      print(f'acesta este dalmatianul cu numarul {i}')
#
# for i in range(0, 101,2) :
#      print(f'urmatorul numar par este {i}')
#
#
# for i in range(100, 0,-2) :
#      print(f'urmatorul numar par este {i}')

# for i in reversed(range(0, 101, 2)):
#     print(f' urmatorul nr. par este  {i}')


#
# culori = ['albastru', 'alb' ,'verde', 'rosu', 'alb']
# for culoare in culori:
#     print(f'culoarea curenta este {culoare}')
#
# for i in range(len(culori)):
#     if culori [i]=='alb':
#         culori[i] = 'mov'
#         print(f'lista curenta este {culori}')
# print(f'lista finala este  {culori}')
#
# for culoare in culori:
#    if culoare == 'mov':
#        index = culori.index('mov')
#        culori[index] = 'magenta'
#        print(f'culoarea curenta este {culori[index]}')
# print(f'noula lista de culori este {culori}')


# print('-----break----------')
# for i in range(len(culori)):
#     if culori [i]=='magenta':
#         culori[i] = 'purpuliu'
#         print(f'lista curenta este {culori}')
#         break
# print(f'lista finala este  {culori}')
#
# print('-----continue----------')
#
# for i in range(len(culori)):
#     if culori [i]=='magenta':
#         continue
#         culori[i] = 'purpuliu'
#         print(f'lista curenta este {culori}')
# print(f'lista finala este  {culori}')

# note = [10,4,6,8,6]
# note_premiante = []
# for nota in note:
#     if nota <= 4 :
#         print(f'studentul curent a picat si a luat nota {nota}') # arata doar cei ce au picat
#         continue
#     note_premiante.append(nota)
# print(f' Lista note premiate este : {note_premiante}')