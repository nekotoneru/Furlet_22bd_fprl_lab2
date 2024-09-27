mas = []
mas11 = []

for i in range(5):
    number = int(input("введіть масив: "))
    mas.append(number)

for number in mas:
    if number % 11 == 0:
        mas11.append(number)

mas11.sort(reverse = True)

if mas11:
    print(mas11)
else:
    print("немає чисел")