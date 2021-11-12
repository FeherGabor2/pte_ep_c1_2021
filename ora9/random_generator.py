import random

print(random.randint(2, 4))
print(random.random())
number = random.randint(-100, 100)
if number > 0:
    print("A szám nagyobb mint 0")
elif number == 0:
    print("A szám 0")
else:
    print("A szám kisebb mint 0")


i = 1
while i <= 5:
    print(i)
    i += 1

for j in [1,2,3,4,5]:
    print(j)