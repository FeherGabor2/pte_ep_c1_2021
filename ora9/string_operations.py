str1 = "Az almafán almák teremnek."
print("A szöveg hossza: ", len(str1))
print(type(len(str1)))
str2 = "Terem"
print("Az str2 megvan az str1-ben: ", str1.find(str2))
lower_str2 = str2.lower()
print(str2)
print("Az lower str2 megvan az str1-ben: ", str1.find(lower_str2))
lower_str1 = str1.lower()
print(str1)
print(lower_str1)
print(str1.upper())
upper_str1 = ""
print("A lower_str2 végig kisbetüs: ", lower_str1.islower())
print("A lower_str2 végig nagybetüs: ", upper_str1.isupper())
str3= "user13"
print("A szövegek csak betűt tartalmaznak: ")
print("\t", str1.isalpha())
print("\t", str2.isalpha())
print("\t", str3.isalpha())
print("A szövegek csak betűt vagy számot tartalmaznak: ")
print("\t", str1.isalnum())
print("\t", str2.isalnum())
print("\t", str3.isalnum())
