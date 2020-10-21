import sys
filename = "../name.txt"

while True:

    try:
        myfile = open(filename, mode='r', encoding='ascii')
    except Exception:
        print("Error found:")
        print(sys.exc_info()[1])
        filename = input("Enter correct filename: ")
    else:
        print(myfile.read())
        break

print("---------------------------------------------------")