import random
mas = []
mas11 = []

for i in range(20):
    number = random.randint(0, 100)
    mas.append(number)
print(mas)
for number in mas:
    if number % 11 == 0:
        mas11.append(number)

mas11.sort(reverse = True)

if mas11:
    print(mas11)
else:
    print("немає чисел")
