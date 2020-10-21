import re

input_filename = "./files/random_data.txt"
result_filename = "./files/result_names.txt"

inputfile = open(input_filename, mode='r')
resultfile = open(result_filename, mode='w')
mytext = inputfile.read()

lookfor = r"[\w._-]+@(?!intel\.com)[\w.-_]+\.\w+"

results = re.findall(lookfor, mytext)

for num, item in enumerate(results, 1):
    print("E-mail №" + str(num) + " " + item)
    resultfile.write(item + "\n")

print("Total: " + str(len(results)))

inputfile.close()
resultfile.close()