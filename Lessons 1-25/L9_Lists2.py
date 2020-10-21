cars = ['bmw', 'vw', 'skoda', 'lada', 'seat']
print(cars)

for x in cars:
    print(x.upper())

for x in range(1,6):
    print(x)

number_list = list(range(0, 10))
print(number_list)

for x in number_list:
    x = x * 2
    print(x)

print("Maximum nunber is: " + str(max(number_list)))
print("Maximum nunber is: " + str(min(number_list)))

mycars = cars

print(mycars)