from tabulate import tabulate


#
#
# 1. Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

# class Cerc:
#     raza = 15
#     culoare = 'rosu'
#
#
#     def __init__(self,culoare,raza):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self,culoare, raza):
#         print(f'Culoarea cercului este {self.culoare} si are raza de {self.raza}')
#
#     def aria(self,aria):
#         self.aria = aria
#         return self.aria
#
#     def diametru(self,diametru):
#         self.diametru= diametru
#         return self.diametru
#
#     def circumferinta(self,circumferinta):
#         self.circumferinta = circumferinta
#         return self.circumferinta
# cerc1 = Cerc
# cerc1.culoare = 'Albastru'
# cerc1.raza = 20
# cerc1.aria = 3.14*(cerc1.raza*cerc1.raza)
# cerc1.diametru = 2* cerc1.raza
# cerc1.circumferinta = 3.14*cerc1.diametru
# print(f'Cercul este {cerc1.culoare}, si are raza {cerc1.raza} cm, circumferinta {cerc1.circumferinta}, diametrul {cerc1.diametru} si  aria {cerc1.aria}')


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

# class Dreptunghi:
#     lungime = 12
#     latime = 10
#     culoare = 'negru'
#
#     def __init__(self):
#         return
#          self.lungime = lungime
#          self.latime = latime
#          self.culoare = culoare
#
#     def descriere(self,lungime,latime,culoare):
#         print(f'Lungime = {lungime}, latime ={latime}, culoarea este {culoare}')
#
#
#     def aria(self,lungime,latime):
#         self.aria =lungime*latime
#         return self.aria
#
#     def perimetru(self,lungime,latime):
#         self.perimetru = 2*(lungime+latime)
#         return self.perimetru
#
# dreptunghi1 = Dreptunghi(20,10,'rosu')
# print(dreptunghi1.aria(20,10))
# print(dreptunghi1.perimetru(20,10))
# print(dreptunghi1.descriere(20,10,'rosu'))


# SAU
#     def descriere(self, lungime, latime, culoare):
#          return (f'Lungime = {lungime}, latime ={latime}, culoarea este {culoare}')
#
#
#     def aria(self,lungime,latime):
#          self.aria =lungime*latime
#          return self.aria
#
#     def perimetru(self,lungime,latime):
#          self.perimetru = 2*(lungime+latime)
#          return self.perimetru
#
#
# dreptunghi2 = Dreptunghi()
# # dreptunghi2.lungime = 12
# # dreptunghi2.latime= 10
# dreptunghi2.culoare = 'maro'
# print(dreptunghi2.aria(12,10))
# print(dreptunghi2.perimetru(12,10))
# print(dreptunghi2.descriere(12,10,'verde'))
# print(dreptunghi2.culoare)


# 3.Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

#
# class Angajat:
#     nume = None
#     prenume = None
#     salariu = 0
#
#     def __init__(self):   #daca adaugam constructor cu atribute atunci nu putem accesa functiile decat daca trecem atributele
#        return
#         # self.nume = nume      # sunt optionale???
#         # self.prenume = prenume
#         # self.salariu = salariu
#
#     def descriere(self,nume,prenume,salariu):
#         return (f'Angajatul cu numele {nume} {prenume} are salariul lunar de {salariu} euro. ')
#
#     def nume_complet(self,nume,prenume):
#         return (f'Numele cpmplet este {nume} {prenume}')
#
#     def salariu_lunar(self,salariu):
#         return (f'Salariul lunar este {salariu}')
#
#     def salariu_anual(self,salariu):
#         salariu_anual = salariu*12
#         return (f'Salariul anual este {salariu_anual}')
#
#     def marire_salariu(self,procent):
#         procent = 2/10
#         salariu_marit = salariu+ salariu*procent
#         return (f'Salariul a fost marit cu {procent} % si dupa marire este {salariu_marit} euro')
#
# angajat1 = Angajat()
# print(angajat1.descriere('Florea','Ion', 5000))
# print(angajat1.salariu_anual(5000))
# angajat2= Angajat()
# nume ='Cretu'
# prenume ='Mihai'
# salariu= 1000
# print(angajat2.nume_complet(nume,prenume))
# print(angajat2.salariu_lunar(salariu))
# print(angajat2.salariu_anual(salariu))
# print(angajat2.marire_salariu(salariu))
# angajat3 =Angajat()
# nume = 'Vlad'
# prenume = 'George'
# salariu = 3000
# print(angajat3.descriere(nume,prenume,salariu))
# print(angajat3.salariu_lunar(salariu))
# print(angajat3.salariu_anual(salariu))
# print(angajat3.marire_salariu(salariu))

### fara constructor

# class Angajati:
#     nume= None
#     prenume =None
#     salariu = 0
#
#     def nume_complet(self,nume,prenume):
#         return f'Numele complet este {nume} {prenume}. '
#
#     def salariu_lunar(self,salariu):
#         return f'Salriul lunar este {salariu} lei.'
#     def salariu_anual(self,salariu):
#         salriu_anual = salariu*12
#         return f'Salariul anual este {salriu_anual} lei.'
#
#     def descriere_angajat(self,nume,prenume,salariu):
#         return  f'Angajatul se numeste {nume} {prenume} si are un salariul lunar de {salariu} lei.'
#
# nume = 'Victor'
# prenume = 'Ion'
# salariu = 1500
# angajat1 = Angajati()
# print(angajat1.descriere_angajat(nume,prenume,salariu))
# print(angajat1.salariu_lunar(salariu))
# print(angajat1.salariu_anual(salariu))
# angajat2 = Angajati()
# nume = 'Misu'
# prenume = 'Cristi'
# salariu = 2500
# print(angajat2.descriere_angajat(nume,prenume,salariu))
# angajat3 = Angajati()
# nume = 'Vlad'
# prenume = 'George'
# salariu = 3000
# print(angajat3.descriere_angajat(nume,prenume,salariu))


#####Rezolvat


# 4.Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
#
# from datetime import date
# class Factura:
#     seria = 'ff1'
#     numar_fact = 0
#     nume_produs = None
#     cantitate = 0
#     pret_buc = 0
#
#     def __init__(self, nrF, numeP, cantitate, pret):
#         self.numar_fact = nrF
#         self.nume_produs = numeP
#         self.cantitate = cantitate
#         self.pret_buc = pret
#
#     def schimba_cantitatea(self, cantitatea):
#         self.cantitate = cantitatea
#         return self.cantitate
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#         return self.pret_buc
#
#     def schimba_nume_produs(self, numeP):
#         self.nume_produs = numeP
#         return self.nume_produs
#
#
#     def genereaza_factura(self):
#         self.total = self.pret_buc * self.cantitate
#         print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, self.total,date.today()]],headers = ['Produs', 'Cantitate', 'pret', 'total','Date']))
#
# factura = Factura(1, 'factura_gaze', 6, 428)
# factura.genereaza_factura()
#
# factura_curent= Factura(2,'Factura Curent', 150,1.5)
# factura_curent.genereaza_factura()

######    rezolvat


# 5. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

# class Cont():
#     iban = None
#     titular_cont = None
#     sold = 0
#     def __init__(self,iban,titular,sold):
#         self.iban = iban
#         self.titular_cont = titular
#         self.sold = sold
#
#     def iban(self,cont):
#         self.iban = cont
#         return self.iban
#     def titular_cont(self,titular):
#         self.titular_cont = titular
#         return self.titular_cont
#     def sold(self,sold):
#         self.sold = sold
#         return self.sold
#     def afisare_sold(self,titular,cont,sold):
#         return f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei'
#     def debitare_cont(self,suma_debitata):
#         while self.sold >0 and suma_debitata<=self.sold:
#             self.sold=self.sold-suma_debitata
#             break
#         print(f'Clientul {self.titular_cont} are in contul {self.iban} suma de {self.sold} dupa ce a fost debitata suma de {suma_debitata} lei!')
#     def credtare_cont(self,suma_creditata):
#         self.sold=self.sold+suma_creditata
#         print(f'Contul a fost creditat cu {suma_creditata} lei si aveti in contul {self.iban} suma de {self.sold} lei')
#
#  client1 = Cont('ro5dddddde4', 'Negru', 354)
#  client1.debitare_cont(100)
#  client1.credtare_cont(150)
# client2 = Cont('ROxxxx', 'Marian', 587)
# client2.credtare_cont(150)
# client2.debitare_cont(160)

# client2 = Cont('iban','titular','sold')
# iban = 'roaaaaaddddfff5'
# titular_cont = 'Cristi'
#
# #rezolvat



# BONUS: (daca aveti timp si doriti sa lucrati suplimentar)
#
# 6.Clasa Masina
#
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
#
# Constructor: model, viteza_maxima
#
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0
# class Masina():
#     marca = 'skoda'
#     model = 'octavia'
#     viteza_maxima = 250
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = ('alb', 'negru', 'rosu', 'albastru')
#     inbatricutala = False
#
#     def __init__(self,marca,model,viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#         self.marca = marca
#
#     def descriere(self):
#         print(self.marca,self.model,self.culoare,self.viteza_maxima,self.viteza_actuala, self.inbatricutala)
#
#     def inmatricutala(self):
#         self.inmatricutala= True
#         return self.inmatricutala
#
#     def vopseste(self,noua_culoare):
#         if noua_culoare in self.culori_disponibile:
#             self.culoare = noua_culoare
#             return self.culoare
#         else:
#             print('Culoarea nu este disponibila')
#             return self.culoare
#     def accelereaza(self,noua_viteza):
#         if noua_viteza <=0:
#             print('Masina sta pe loc')
#         elif noua_viteza > self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#             return self.viteza_maxima
#         else:
#             self.viteza_actuala = noua_viteza
#             return self.viteza_actuala
#
#
#
# masina1 = Masina('Skoda', 'octavia',220)
# print(masina1.vopseste('rosu'))
# masina1.descriere()
# print(masina1.accelereaza(250))

##### Rezolvat





# 7. Clasa TodoList
class TodoList():
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
    todo = {'contract1': 'de semnat si trimis',
            'contract2': 'de negociat',
            'contract3': 'de prelungit'}

# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
    def adauga_task(self):
        self.todo = {'semneaza_CTR': 'luni 5 feb'}


# finalizeaza_task(nume) - se va sterge din dict
    def finalizeaza_tasc(self):
        self.todo.pop('semneaza CTR')
        return self.todo
#afiseaza_todo_list() - doar cheile
    def afiseaza_todo_list(self):
        print(self.todo)


# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
    def detalii_suplimentare(self,nume_task):
        if nume_task in self.todo.keys():
            print(self.todo.keys())
        else:
            option = input('vrei sa il adaugam da/nu')
            if option == 'da':
                detalii = input('introdu detalii suplimentare')
                self.todo[nume_task]= detalii
                print(self.todo)

            else:
                print('La revedere!')

Cristi = TodoList()
Cristi.detalii_suplimentare('contract1')
Cristi.afiseaza_todo_list()
Andrei =TodoList
todo = {'materiale': 'de livrat',
        'materiale noi': 'de cumparat',
        'accesorii': 'de montat la usa'}
# Cristi.detalii_suplimentare('sunat')
Andrei.detalii_suplimentare('catel')



# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict



