# ABSTRACTION
# Clasa abstracta FormaGeometrica
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

# Contine un field PI=3.14
    PI = 3.14

# Contine o metoda abstracta aria
    @abstractmethod
    def aria(self):
        pass

# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi
    def descrie(self):
        print('Cel mai probabil am colturi')

# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
class Patrat(FormaGeometrica):

# constructor pt latura
    def __init__(self, latura):
        self.__latura = latura
# ENCAPSULATION
# latura este proprietate privata
    __latura = 10
# Implementati getter, setter, deleter pt latura
    @property
    def latura(self,latura):
        self.__latura= latura
    @latura.getter
    def latura(self):
        return self.__latura
    @latura.setter
    def latura(self,latura):
        if latura >0:
            self.__latura = latura
        else:
            print('Dimensiunea laturii nu este valida')

    @latura.deleter
    def latura(self):
        self.__latura = 0
# Implementati metoda ceruta de interfata
    def aria(self):
        aria = self.__latura**2
        return aria
# Creati un obiect de tip Patrat si jucati-va cu metodele lui
masa = Patrat(5)
# masa.descrie()
print(masa.latura)
print(masa.aria())
# masa.latura= 11
# print(masa.latura)
# print(masa.aria)
# del masa.latura
# masa.latura= 8
# print(masa.latura)
# print(masa.aria())
# del masa.latura
masa.latura = 15.2
print(masa.latura)
print(masa.aria())

# #Clasa Cerc - mosteneste FormaGeometrica
# class Cerc(FormaGeometrica):
#     _raza= 70
# # constructor pt raza
#     def __init__(self,raza):
#         self.raza = raza
#
# # raza este proprietate privata
# # Implementati getter, setter, deleter pt raza
#     @property
#     def raza(self,raza):
#         self._raza = raza
#
#     @raza.getter
#     def raza(self):
#         return self._raza
#     @raza.setter
#     def raza(self,raza):
#         if raza >= 0:
#             self._raza = raza
#         else:
#             print('Raza cercului nu este valida')
#     @raza.deleter
#     def raza(self):
#         self.raza=0
#
# # Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
#     def aria(self):
#         self.aria = (self.raza**2)*self.PI
#         return self.aria
# # POLYMORPHISM
# # # Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
#     def descrie(self):
#         print('Eu nu am colturi')
# # Creati un obiect de tip Cerc si jucati-va cu metodele lui
# mingeFotbal= Cerc(10)
# print(mingeFotbal.aria())
# del mingeFotbal.raza
# print(mingeFotbal.raza)
# mingeFotbal.raza = 25
# print(mingeFotbal.raza)
# print(mingeFotbal.aria())