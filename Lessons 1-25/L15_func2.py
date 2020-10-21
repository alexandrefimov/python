def create_record(name, telephone, address):
    record = {
        'name' : name,
        'telephone' : telephone,
        'address' : address
    }
    return record

user1 = create_record("Vasya", "123", "SPb")

print(user1)

def give_award(medal, *persons):
    for person in persons:
        print("Tovarish " + person.title() + " nagrazhdaetsya medliyu " + medal)

give_award("Za Berlin", "vasya", "petya")
give_award("Za London", "petya", "kolya", "ibragim")