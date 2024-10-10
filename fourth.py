m = int(input("к-кість рядочків:"))
n = int(input("к-кість стовпців:"))
num = input("всі числа:")
numbers = num.split()

if len(numbers) != m * n:
    print("error")
else:
    mas = []

    index = 0
    for i in range(m):
        line = []
        for j in range(n):
            line.append(numbers[index])
            index += 1
        mas.append(line)

    for i in range(m-1, -1, -1):
        print(mas[i])