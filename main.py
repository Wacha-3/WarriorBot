import discord
import os
import datetime

today = datetime.datetime.now()
client = discord.Client()
playerList = []  #initialise the array
currentPlayers = []


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
  global gameRunning 
  global UserNumThatSentMsg 
  for x in range(len(currentPlayers)):  
        if message.author.name == currentPlayers[x]:
          UserNumThatSentMsg = x
          break
        elif message.author.name == currentPlayers[0]:
          UserNumThatSentMsg = 0
          break
  if message.author == client.user:
      return
      

      
     

  elif message.content.startswith('$start'):     
       gameRunning = 1
  elif message.content.startswith('$start'):  
       gameRunning = 0
  elif message.content.startswith('$score'):
       for x in range(len(playerList)):
        await message.channel.send(playerList[x].name + ' has dealt '+ str(playerList[x].damageDealt) +' damage in total!')






        #Takes the name of players and adds it into a list
  elif message.content.startswith('$join'):    

    if currentPlayers.count(message.author.name) == 0:

         playerList.append(Player(message.author.name)) #append the array and create a Player object
         currentPlayers.append(message.author.name) 
         await message.channel.send(message.author.name + ' has joined the arena!') #sends the name 
         global enemy
         enemy = Enemy('Goblin',len(playerList)*75) #####change this multiplier to something scalable for each
            
    else:  
         await message.channel.send(message.author.name + ' has already joined the arena!') #sends the name 






        #checks if $d was used and then adds damage to the monster and the players total
  elif message.content.startswith('$d'):
       dmg = message.content.replace("$d", "")
                    #checks if it is an int then if it is prints the values
       if RepresentsInt(dmg) and int(dmg) >= 0 and int(dmg) <= 100:           
          playerList[UserNumThatSentMsg].damageDealt =  playerList[UserNumThatSentMsg].damageDealt + int(dmg)    
          enemy.health = enemy.health - int(dmg)
          await message.channel.send(message.author.name + ' has dealt'+ dmg +' damage!')
          await message.channel.send(str(enemy.health) + '/' + str(enemy.maxHealth))
          if (enemy.health <= 0):
            message.channel.send(enemy.name + 'has been defeated! Great job warriors :crossed_swords:')
            gameRunning = 0
            for x in range(len(playerList)):
              await message.channel.send(playerList[x].name + ' has dealt '+ str(playerList[x].damageDealt) +' damage in total!')     
            message.channel.send('The next enemy will be the boss monster "GIANT CRAB"')



  elif message.content.startswith('$hp'):
       await message.channel.send(str(enemy.health) + '/' + str(enemy.maxHealth))
  



  elif message.content.startswith('$bg'):
       await message.channel.send(playerList[-1].name)
       await message.channel.send(playerList[UserNumThatSentMsg].name)
       await message.channel.send(len(playerList))    
#  elif message.content.startswith('$'):
   #  await message.channel.send('Invalid Syntax ' + message.author.name)



   
  
  

client.run(os.getenv('TOKEN'))

