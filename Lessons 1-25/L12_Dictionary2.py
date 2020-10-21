enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo'
}

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

all_enemies[5]['health'] = 30
all_enemies[5]['loc_x'] += 10

for enemies in all_enemies:
    print(enemies)

