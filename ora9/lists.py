my_list = [1, 2.5, "alma", False]
print("A lista hossza: ", len(my_list)) #lista hosszának lekérdezése
print("A len() függvény visszatérési értékének a típusa: ", type(len(my_list)))
print()

print("A lista tartalmazza-e 2.5-ös értéket", 2.5 in my_list)
print("Az in operátor eredményének típusa: ", type(2.5 in my_list))
print()

print("A lista tartalmazza-e 2.5-ös értéket", 2 in my_list)
print("Az in operátor eredményének típusa: ", type(2 in my_list))
print()

print("A 2.5-ös érték pozíciója a listában: ", my_list.index(2.5))
print("Az index() metódus visszatérési értékének típusa: ", type(my_list.index(2.5)))
print()

try:
    print("A 2.5-ös érték pozíciója a listában: ", my_list.index(2))
    print("Az index() metódus visszatérési értékének típusa: ", type(my_list.index(2)))
except ValueError:
    print("Hiba!")
print()

print("A lista 4. elemének a lekérdezése: ", my_list[3])
print("A lista 1. elemének a lekérdezése: ", my_list[0])
print("A lista utolo. elemének a lekérdezése: ", my_list[-1])
print("A lista utolso. elemének a lekérdezése: ", my_list[len(my_list)-1])
print(my_list[0:2])
print(type(my_list[0:2]))

print(my_list)
my_list[0] = -3
print(my_list)

my_list.append("körte")
print(my_list)

my_list.append([5,6,7])
print(my_list)


my_list.extend([1,2,3])
print(my_list)

my_list.insert(0,"start")
print(my_list)

del(my_list[7])
print(my_list)


while 1 in my_list:
    my_list.remove(1)

print(my_list)

my_list = [4,7,1,4.5,7,6]
print(my_list)

my_list.sort()
print("A sort() metódus visszatérési értékének a típusa:", type(my_list.sort()))
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.sort()
my_list.reverse()
print(my_list)

my_list2 = sorted(my_list)
print(my_list)
print(my_list2)