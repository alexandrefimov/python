def factorial(x):
    y = 1
    for i in range(1, x + 1):
        y = y * i
    return y

for z in range(1, 10):
    print(str(z) + "!\t = " + str(factorial(z)))