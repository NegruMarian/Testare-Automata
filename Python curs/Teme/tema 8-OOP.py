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
        # raise NotImplementedError

    # Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
    def descrie(self):
        print('Cel ami probabil am colturi')


#
# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
class Patrat(FormaGeometrica):

    # constructor pt latura
    def __init__(self, latura):
        self.latura = latura

    # ENCAPSULATION
    # latura este proprietate privata
    __latura = 10

    # Implementati getter, setter, deleter pt latura
    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def get_latura(self, latura):
        if latura > 0:
            self.__latura = latura
            return self.__latura
        else:
            print('Lungimea laturii nu este valida')

    @latura.setter
    def set_latura(self, latura):   # aici trebuie cod de update
        pass

    @latura.deleter
    def delet_latura(self):
        self.__latura = 0

    # Implementati metoda ceruta de interfata

    def aria(self):
        self.aria= self.__latura*self.__latura
        return self.aria


# Clasa Cerc - mosteneste FormaGeometrica
class Cerc(FormaGeometrica):


    # constructor pt raza
    def __init__(self, raza):
        __raza = raza

    # raza este proprietate privata
    __raza = 15
    # Implementati getter, setter, deleter pt raza
    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def get_raza(self):
        return self.__raza

    @raza.setter
    def setter_raza(self,raza):
        self.__raza = raza

    @raza.deleter
    def deleter_raza(self):
        self.__raza = None


# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
    def aria(self):
        self.aria =(self.__raza*self.__raza) * self.PI
        return self.aria

# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
    def descrie(self):
        print('Eu nu am colturi')
#
# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# cutie = Patrat()
# print(cutie.aria(4))

# Creati un obiect de tip Cerc si jucati-va cu metodele lui
#
# 3. Actualizati proiectul pe github facand un push la noul cod
# In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public
