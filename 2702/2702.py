print("Ala ma " + " 5 lat")
print(0 - 1)
print(2 / 1)
print(2 * 1)
print(2 // 1) # dzielenie bez reszty
print(2 ** 1) # potegowanie
print(2 % 1) # dzielenie modulo
print(5)
print("Ala ma 5 lat")
# print("Ala ma " + 5 + " lat") # blad
print("Ala ma " + str(5) + " lat")

# forrmatting

print("Ala ma {} lat" .format(5))
print("Ala ma {1} lat a Marta {0}" .format(5,10))

# f-string (Python 3.6)

wiek = 5
print(f"Ala ma {wiek} lat")

imie = "Malgorzata"
print(imie[4])
# imie[4] = "a"
imie = "Adam"
print(imie.lower())
imie = imie.lower()
print(imie)
"Wojtek".lower().lstrip().rsplit()

# listy 

lista = []
print(type(lista))
print(type("Ala"))
print(type(5))

lista.append(5)
lista.insert(0, 6)

lista2 = [1, 2, 3, 4, 5]
lista2[3]
lista3 = lista + lista2
print(lista3)
lista4 = [1, "Ala", imie, 3.4, [1, 3]]
print(lista4[4][1])

macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

macierz[1][1]

# slownik
slownik = {}
print(type(slownik))
# <class 'dict'>

slownik["imie"] = "Marek"
print(slownik)
slownik2 = {'imie': 'Marek',
            'wiek': 25,
            'wzrost' : 175}
print(slownik2)
print(slownik2.keys())
print(slownik2.items())
print(slownik2['imie'])

# def pow(
 #   pass)

# import
from math import *
from math import pow

import math as m

m.pow(2, 2)


wejscie = input("Wprowadz wartosc:")
print(wejscie)

liczba =10
if liczba > 10:
    print ()
    elif liczba > 0:
        print ()
else:
    print("Poza zakresem")

if liczba < 10 and liczba > 0:
    print ()
else:
    print("Poza zakresem")

#rownowazne

if 10 > liczba > 0:
    print ()
else:
    print("Poza zakresem")

# rozne od liczba !=0
# rowne liczba == 0

#liczba is not True
#liczba is True

if liczba in [1, 2, 3, 10]:
    print("jest w liscie")
else:
    print("nie ma w liscie")