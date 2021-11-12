import random
"""number = 350
if number > 100:
    print("A szám nagyobb mint 100.")
else:
    print(""
          "4A szám nem nagyobb mint 100")

if number % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan")

number2 = 10
if number % number2 == 0:
    print("A", number2, "Osztója a", number, "-nek")
else:

    if number2 % number == 0:
        print("A", number, "Osztója a", number2, "-nek")
    else:
        print("Egyik sem osztója a másiknak")


text = "almafa"
if text[0] == text[-1]:
    print("A szöveg első és utolsó betűje egyezik.")
else:
    print("A szöveg első és utolsó betűje nem egyezik.")

if number > 0:
    print("A szám nagyobb mint 0")
elif number == 0:
    print("A szám 0")
else:
    print("A szám kisebb mint 0")

if text[0].isupper():
    print("A szöveg nagybetűvel kezdődik")
else:
    print("A szöveg nem nagybetűvel kezdődik")
text = "almafavirág"
text2 = "alma"
if text[0:5] == text2[0:5]:
    print("A szövegek első 5 betűje megegyezik")
else:
    print("A szövegek első 5 betűje nem egyezik meg")

if number >= 3 and number < 17:
    print("Beleesik az [3, 17) intervallumba")
else:
    print("A szám nem esik bele a [3, 17) intervallumba")

a, b, c = 3, 4, 4

if a + b > c and b + c > a and a + c > b:
    print("Lehet ezen oldalhosszakkal háromszöget szerkeszteni")
else:
    print("Nem lehet ezen oldalhosszakkal háromszöget szerkeszteni")

if a >= b and a >= c:
    print("Az a valtozo a legnagyobb")
    if b >= c:
        print("A c valtozo a legkisebb")
    else:
        print("A b valtozo a legkisebb")
else:
    if b >= c:
        print("A b változó értéke a legnagyobb")
        if a >= c:
            print("A c valtozo a legkisebb")
        else:
            print("A a valtozo a legkisebb")
    else:
        print("A c változó értéke a legnagyobb")
        if a >= b:
            print("A b valtozo a legkisebb")
        else:
            print("A a valtozo a legkisebb")

character = "a"
maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
numbers = "0123456789"
irasjelek = ",.;:?!"
if maganhangzok.find(character) >= 0:
    print("Magánhangzó")
elif numbers.find(character):
    print("Szám")
elif irasjelek.find(character):
    print("Írásjel")

number = 9
if number % 3 == 0 and number % 5 == 0:
    print("Oszthato 3-mal és 5-tel")
elif number % 3 == 0:
    print("Csak 3-mal oszthato")
elif number % 5 == 0:
    print("Csak 5-tel oszthato")
else:
    print("Nem oszthato sem 3-mal sem 5-tel.")
try:
    grade = int(input())
    if grade == 5:
        print("kiváló")
    elif grade == 4:
        print("jó")
    elif grade == 3:
        print("Közepes")
    elif grade == 2:
        print("Elégséges")
    else:
        print("Rossz")

except ValueError:
    print("De én egy számot kértem")
try:
    print(type(float(input("Kérek egy valós számot"))))
except:
    print("Hibás bemenet")

print(type(str(7)))
print(type(str(-91.2121)))
"""

input_data= input("Kérek egy egész számot: ")
try:
    intnumber = int(input_data)
    print("A kapott szám 3-szorosa: ", 3 * intnumber)
    print(type(input_data))
    print(type(intnumber))
except ValueError:
    print("Ez nem egy egész szám.")
