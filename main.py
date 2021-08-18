enemyName = input('What is the name of the enemy: ')
maxHealth = int(input('What is the health of the enemy: '))
health = maxHealth

while health >= 0:
    health = health - int(input('Damage: '))
    print(str(health)+('/')+str(maxHealth))

print(enemyName + ' has been defeated good work warrior!!')
