import discord
import os
import datetime

today = datetime.datetime.now()
client = discord.Client()

class Enemy:

    name = 'minion'
    HealthPerPlayer = 75
    maxRep = 20
    maxHealth = 0
    currentHealth = 0

    def introduce_self(self):
        print(self.name)


class Player:

    name = 'rob'
    damageDealt = 0
   
   
    def introduce_self(self):
        print(self.name)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


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


#checks if $d was used and then adds damage to the monster and the players total
    if message.content.startswith('$d') or message.content.startswith('$damage') :
        dmg = message.content.replace("$d", "")
        #checks if it is an int then if it is prints the values
        if RepresentsInt(dmg) and int(dmg) >= 0 and int(dmg) <= 10:
            dmg = message.author.name + "," + dmg + "," + today.strftime(' %b-%d')


           
    elif message.content.startswith('$p'):
        msg = message.content.replace("$p", "")

    else:
        await message.channel.send('Invalid Syntax ' + message.author.name)

client.run(os.getenv('TOKEN'))

