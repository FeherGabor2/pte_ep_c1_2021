print("1.feladat")
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október",
         "November", "December"]

months_and_days = []
for i in range(len(months)):
    months_and_days.append(months[i])
    months_and_days.append(days_in_months[i])
print(months_and_days)

print()
print("2.feladat")
import random

random.randint(3, 5)
random.random()

numbers = []
for i in range(20):
    numbers.append(random.randint(1, 101))
print(numbers)
max= numbers[0]
for j in range(len(numbers)):
    if numbers[j] > max:
        max = numbers[j]
print("A numbers lista legnagyobb eleme: ", max)

min = numbers[0]
hely = 0
for k in range(len(numbers)):
    if numbers[k] < min:
        min = numbers[k]
        hely=k
print("A numbers lista legkisebb eleme: ", min)
print("Helye: ",hely+1)
