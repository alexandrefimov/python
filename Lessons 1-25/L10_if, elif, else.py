age = 36
if (age <= 4):
    print("Baby")
elif (age > 4) and (age < 12):
    print("Child")
elif (age >= 12) and (age < 40):
    print("Man")
else:
    print("Old")



all_cars = ['Dacia', 'Renault', 'BMW', 'Mercedes', 'Alfa', 'Lada', 'Porche']
german_cars = ['BMW', 'Mercedes']

if 'Lada' in all_cars:
    print("Yes in list")
else:
    print("Not exist")



for xxx in all_cars:
    if xxx in german_cars:
        print(xxx + " is German car")
    else:
        print(xxx + " is not German car")