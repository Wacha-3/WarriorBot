import discord

class Enemy:
    def introduce_self(self):
        print(self.name)



players=4
e=Enemy
e.name = input('What is the name of the enemy: ')
players = int(input('How many players: '))
e.health=75*players
maxHealth = e.health

print('Prepare to face ' + e.name + ': ('+str(maxHealth)+'/'+ str(maxHealth)+')')

while e.health >= 1:
    e.health = e.health - int(input('Damage: ')) 
    print('HP: ('+str(e.health)+('/')+str(maxHealth)+')')

print(e.name + ' has been defeated good work warrior!!')

print('the next enemy will be: ') #+ e.name)


#add individial score tracking per monster 

#add oop enemy classes

#set a schedule for what monsters will apear