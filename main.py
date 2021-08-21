import discord
import os
import datetime

today = datetime.datetime.now()
client = discord.Client()
playerList = []  #initialise the array
class Enemy:

    name = 'minion'
    HealthPerPlayer = 75
    maxRep = 20
    maxHealth = 0
    currentHealth = 0

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

#Takes the name of players and adds it into a list
    if message.content.startswith('$join'):
        playerList.append(Player(message.author.name)) #append the array and create a Player object
        await message.channel.send(playerList[-1].name + ' has joined the arena!') #sends the name 

        for obj in playerList:
          print(obj.name )
        


#checks if $d was used and then adds damage to the monster and the players total
    if message.content.startswith('$d') or message.content.startswith('$damage'):
        dmg = message.content.replace("$d", "")
        #checks if it is an int then if it is prints the values
        if RepresentsInt(dmg) and int(dmg) >= 0 and int(dmg) <= 10:           
            playerList[0].damageDealt =  playerList[0].damageDealt + int(dmg) 
            await message.channel.send(playerList[0].name + ' has dealt'+ dmg +' damage!')

           
  


    #elif:
     #   await message.channel.send('Invalid Syntax ' + message.author.name)

client.run(os.getenv('TOKEN'))

