# 1.Git setup
#
# OBLIGATORIU!
# Git setup: (ne ajuta sa ne expunem proiectele angajatorilor - super important)
# https://drive.google.com/file/d/1yaURoa2VGyCARQ7BUZ-gplnMTxnJjRuz/view?usp=sharing
#
#
# OPTIONAL
# How to use gitignore: (ne ajuta sa ignoram fisiere pe care nu vrem sa le expunem)
# https://drive.google.com/file/d/17NVuy28nspPt5_DzynmD0CF7mbmiVzY9/view?usp=sharing
#
#
# 2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)

from abc import ABC, abstractmethod
import math


# ABSTRACTION
# Clasa abstracta FormaGeometrica
class FormaGeometrica(ABC):
# Contine un field PI=3.14
    PI = 3.14

# Contine o metoda abstracta aria
    @abstractmethod
    def aria(self):
        pass


    # Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
    def descrie(self):
        print('Cel ami probabil am colturi')


#
# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# class Patrat(FormaGeometrica):
#     __latura = 10
#     # constructor pt latura
#     def __init__(self, latura):
#         self.__latura = latura
#
#     # ENCAPSULATION
#     # latura este proprietate privata
#
#
#     # Implementati getter, setter, deleter pt latura
#     @property
#     def latura(self):
#         return self.__latura
#
#     @latura.getter
#     def latura(self):
#         return self.__latura
#
#     @latura.setter
#     def latura(self, latura):   # aici trebuie cod de update
#          if latura > 0:
#               self.__latura = latura
#
#          else:
#               print('Lungimea laturii nu este valida')
#
# #
#     @latura.deleter
#     def latura(self):
#         self.__latura = 0
#
#     # Implementati metoda ceruta de interfata
#
#     def aria(self):
#         self.aria= self.__latura*self.__latura
#         return self.aria

# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# cutie = Patrat(10)
# print(cutie.aria())
# print(cutie.latura)
# cutie.latura=7
# print(cutie.latura)
# print(cutie.aria())  #aici afiseaza tot aria avand latura initiala de 10 in loc de 7
# cutie.latura= -8
# print(cutie.latura)
# print(cutie.aria())

#Clasa Cerc - mosteneste FormaGeometrica
# class Cerc(FormaGeometrica):
#     __raza = 15
#
#     # constructor pt raza
#     def __init__(self, raza):
#         __raza = raza
#
#     # raza este proprietate privata
#
#     # Implementati getter, setter, deleter pt raza
#     @property
#     def raza(self):
#         return self.__raza
#
#     @raza.getter
#     def raza(self):
#         return self.__raza
#
#     @raza.setter
#     def raza(self,raza):
#         if raza > 0:
#             self.__raza = raza
#         else:
#             print('raza are o valoare ireala')
#
#     @raza.deleter
#     def raza(self):
#         self.__raza = None
#
#
# # Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
#     def aria(self):
#         self.aria =(self.__raza*self.__raza) * self.PI
#         return self.aria
#
# # POLYMORPHISM
# # Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
#     def descrie(self):
#         print('Eu nu am colturi')





# Creati un obiect de tip Cerc si jucati-va cu metodele lui
# mingeVolei = Cerc(20)
# print(mingeVolei.raza)
# mingeVolei.raza = 20
# print(mingeVolei.raza)
# mingeVolei.descrie()
# print(mingeVolei.aria())
#
# 3. Actualizati proiectul pe github facand un push la noul cod
# In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public
