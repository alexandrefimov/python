enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo'
}

print("Location X = " + str(enemy['loc_x']))
print("location Y = " + str(enemy['loc_y']))
print("His name is: " + enemy['name'])

enemy['renk'] = 'Admiral'

print(enemy)

del enemy['renk']

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print(enemy)