name = input("Enter your name: ")
print(name)

num1 = input("Enter X: ")
num2 = input("Enter Y: ")
sum = int(num1) + int(num2)
print(sum)

message = ""
while message != 'secret':
    message = input("Enter password: ")
    print(message + " Password not correct")