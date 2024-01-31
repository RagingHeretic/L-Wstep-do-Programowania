# Hubert Jackowski
# Zadanie 1
import math
class LogExp:
    def __init__(self, base):
        self.__a = base
    def exp(self, x):
        """Funkcja zwraca wyrażenie a^x"""
        return self.__a ** x
    def log(self, x):
        """Funkcja zwraca wyrażenie loga(x)"""
        return math.log(self.__a, x)

# Zadanie 2
class Prostokat():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def Area(self):
        """Funkcja zwraca pole figury"""
        return self.__a * self.__b

class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)

# Zadanie 3
class Student:
    def __init__(self, name, surname, index, subjectsKeys):
        self.__name = name
        self.__surname = surname
        self.__index = index
        self.__subjects = dict.fromkeys(subjectsKeys)
    def GetSubjects(self):
        """Funkcja zwraca prdzednioty na jakie uczęszcza student"""
        return self.__subjects
    def GetIdentity(self):
        """Funkcja zwraca imię, nazwisko i index studenta"""
        return [self.__name, self.__surname, self.__index]
    def SetGrade(self, subjectKey, newGrade):
        """Funkcja zmienia ocenę z przedmioty subjectKey na wartość argumentu newGrade i zwraca wartość 1 jeśli przedmiot istnieje.
        Funkcja zwraca 0 jeśli przedmiot subjectKey nie istnieje"""
        if(subjectKey in self.__subjects):
            self.__subjects[subjectKey] = newGrade
            return 1
        else:
            return 0
    def GetGrade(self, subjectKey):
        """Funkcja zwraca ocene z przedmiotu podanego jako argument"""
        return self.__subjects[subjectKey]

# Zadanie 4
class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__annual_salary = annual_salary
    def GetFirstName(self):
        return self.__first_name
    def GetLastName(self):
        return self.__last_name
    def GetAnnualSalary(self):
        return self.__annual_salary
    def GiveRaise(self, value = 2000):
        self.__annual_salary += value
