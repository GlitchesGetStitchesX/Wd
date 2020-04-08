#Zad 1

A = [1/x for x in range(11)]

B = [2**i for i in range(11)]

C = [x for x in B if x % 4 !=0]

print(A)
print(B)
print(C)

#Zad 2

import random

matrix = [[random.radiant(0, 10) for i in range (4)],
[]]

print(matrix)

lista = [j for j in matrix if]

#Zad 3

slownik = {"czekolada":"sztuki", "sok":"sztuki", "pomarancze":"kg"}

produkty = [j for j in slownik if slownik[j] == "sztuki"]
print(produkty)

#Zad 4

def monotonicznosc(a):
    if(a > 0):
        print("rosnaca")
        return 0
    elif(a < 0):
        print("malejaca")
        return 0
    else:
        print("stala")
        return 0



a=input("Podaj wartosc a funkcji y=ax+b ")
a=int(a)
print(monotonicznosc(a))

#Zad 5
    
    def proste (a1, a2):
        if(a1 = a2):
            print("rownlegle")
            return 0
        elif(a1 * a2 = -1):
            print("prostopadle")
            return 0
    
a1 = input("Podaj wartosc a1 funkcji y=a1x+b1")
a1 =  int(a1)
a2 = input("Podaj wartosc a2 funkcji y=a2x+b2")
a2 = int(a2)

#Zad 6

import math

def promien(a=1, b=2, x=0, y=0):
    r = ((x-a)**2)+((y-b)**2)
    return r**(1/2)

print(promien())