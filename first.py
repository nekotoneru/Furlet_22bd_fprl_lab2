import random
for i in range(10):
    series = []
    sum = 0
    while sum != 12:
        num = random.randint(0,2)
        if sum == 11:
            num = random.randint(0,1)
        if sum <= 12:
            series.append(num)
            sum += num
    print(series)