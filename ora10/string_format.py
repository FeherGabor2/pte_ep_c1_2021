number = 5
number2 = number * 2
print("A number változó értéke:",number, "\b. Ha megszorzom 2-vel akkor",number2,"\b-t kapok")
print("A number változó értéke: ",number, ". Ha megszorzom 2-vel akkor ",number2,"-t kapok",sep="")
print(f"A number változó értéke: {number}. Ha megszorzom 2-vel akkor {number2}-t kapok")
print("A number változó értéke: {}. Ha megszorzom 2-vel akkor {}-t kapok".format(number,number2))

# Igazítások
print(f"A number változó értéke: {number:<3}. Ha megszorzom 2-vel akkor {number2:>5}-t kapok")
print("A number változó értéke: {:^3}. Ha megszorzom 2-vel akkor {:^4}-t kapok".format(number,number2))

# Számformátumok
number = 125
print(f"A szám bináris alakja: {number:b}, az oktális alakja: {number:o}, a decimális: {number:d},"
      f" hexadecimális: {number:X}")
print("A szám bináris alakja: {:b}, az oktális alakja: {:o}, a decimális: {:d},"
      " hexadecimális: {:X}".format(number,number,number,number,number))

number = 65
print(f"{number:c}")
print("{:c}".format(number))

number = 100.12345
print(f"Tudomanyos: {number:e} vagy {number:E}")
print(f"Valós szám: {number:f}")
print(f"3 tizedes jegy pontosság: {number:.3f}")
print(f"Százalékos: {number:%}")
print(f"15 karakteren: {number:15f}")
print(f"15 karakteren, 3 tizedes jegy pontosság: {number:15.3f}")