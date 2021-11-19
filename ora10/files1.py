fileobject = open("lorem.txt", "r")

sor = fileobject.readline()
while len(sor) > 0:
    print(sor)
    sor =fileobject.readline()

fileobject.close()

print("2.feladat")
fileobject = open("lorem.txt", "r")
max_length = 0
max_row = ""
for line in fileobject:
    if len(line) > max_length:
        max_row = line
        max_length = len(line)
print(max_row)
print(max_length)
fileobject.close()

print("3.feladat")
fileobject1 = open("lorem.txt", "r")
fileobject2 = open("lorem_copy2.txt", "w")

line1 = fileobject1.readline()
while line1 !="":
    fileobject2.write(line1)
    line1 = fileobject1.readline()

fileobject1.close()
fileobject2.close()

print("4.feladat")
fileobject1 = open("lorem.txt", "r")
fileobject2 = open("lorem_copy2.txt", "w")

for line in fileobject1:
    new_row=""
    for character in line:
        if character != " ":
            new_row += character
        else:
            new_row += "   "
    fileobject2.write(new_row)


fileobject1.close()
fileobject2.close()



print("5.feladat")
fileobject1 = open("fajl1.txt", "r")
fileobject2 = open("fajl2.txt", "r")
fileobject3 = open("fajl1_es_fajl2.txt", "w")

line1 = fileobject1.readline()
line2 = fileobject2.readline()
while line1 !="" or line2 !="":
    fileobject3.write(line1)
    fileobject3.write(line2)
    line1 = fileobject1.readline()
    line2 = fileobject2.readline()

fileobject1.close()
fileobject2.close()
fileobject3.close()