mylist = []

msg = ""
while msg != 'STOP':
    msg = input("Enter new item, or STOP to finish ")
    mylist.append(msg)

print(mylist)
