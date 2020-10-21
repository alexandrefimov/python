import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='ascii')

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'Awards': ["oregon", "nevada", "new york"]
}

player2 = {
    'PlayerName': "Barak Obama",
    'Score': 346,
    'Awards': ["washington", "texas", "missury"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# Save by JSON

json.dump(myplayers, myfile)
myfile.close()

# Load by JSON

myfile = open(filename, mode='r', encoding='ascii')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name: " + str(user['PlayerName']))
    print("Player score: " + str(user['Score']))
    for num, x in enumerate(user['Awards'], 1):
        print("Player Award №" + str(num) + ": " + x)
    print("-----------------------\n")