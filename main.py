import discord
import os
import datetime

today = datetime.datetime.now()
client = discord.Client()
playerList = []  #initialise the array


class Enemy:
    def __init__(self, name, maxHealth): 
       self.name = name
       self.maxHealth = maxHealth
       self.health = maxHealth
      

    def introduce_self(self):
        print(self.name)


class Player:
    def __init__(self, name): 
       self.name = name
       self.damageDealt = 0
       
   
    def introduce_self(self):
        print(self.name)


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))



#Method to check if something is an int
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



#When a message is sent
@client.event
async def on_message(message):

  if message.author == client.user:
    return



       

  elif message.content.startswith('$start'):
       global gameRunning 
       gameRunning = 1
  elif message.content.startswith('$stop'):
       gameRunning = 0
       for x in playerList:
        await message.channel.send(playerList[0].name + ' has dealt '+ str(playerList[0].damageDealt) +' damage in total!')

        #Takes the name of players and adds it into a list
  elif message.content.startswith('$join'):
        playerList.append(Player(message.author.name)) #append the array and create a Player object
        await message.channel.send(playerList[-1].name + ' has joined the arena!') #sends the name 
        global enemy
        enemy = Enemy('Goblin',len(playerList)*75) #####change this multiplier to something scalable for each
       

        #checks if $d was used and then adds damage to the monster and the players total
  elif message.content.startswith('$d') & gameRunning:
       dmg = message.content.replace("$d", "")
                    #checks if it is an int then if it is prints the values
       if RepresentsInt(dmg) and int(dmg) >= 0 and int(dmg) <= 100:           
          playerList[0].damageDealt =  playerList[0].damageDealt + int(dmg)    
          enemy.health = enemy.health - int(dmg)
          await message.channel.send(playerList[0].name + ' has dealt'+ dmg +' damage!')
          await message.channel.send(str(enemy.health) + '/' + str(enemy.maxHealth))
                 
  elif message.content.startswith('$hp'):
       await message.channel.send(str(enemy.health) + '/' + str(enemy.maxHealth))

  
            
  elif message.content.startswith('$'):
     await message.channel.send('Invalid Syntax ' + message.author.name)



   
  
  

client.run(os.getenv('TOKEN'))

