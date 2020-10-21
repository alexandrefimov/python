inputfile = "../passwd.txt"
outputfile = "../mypasswd.txt"

search_passwd = "petya"

myfile1 = open(inputfile, mode='r', encoding='ascii')
myfile2 = open(outputfile, mode='a', encoding='ascii')

for num, line in enumerate(myfile1, 1):
    if search_passwd in line:
        print("Line №" + str(num) + ": " + line.strip())
        myfile2.write("Found: " + line)

myfile1.close()
myfile2.close()