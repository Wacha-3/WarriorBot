
import discord
import tinydb
import os
import datetime

from tinydb import TinyDB, Query
from discord.ext import commands

today = datetime.datetime.now()

playerList = []  #initialise the array
currentPlayers = []
bot = commands.Bot(command_prefix='$')
db = TinyDB('db.json')
User = Query()
#initiallise an array of minions, and comapre it to date time to decide what enemies will apear 
class Enemy:
    def __init__(self, name, maxHealth): 
       self.name = name
       self.maxHealth = maxHealth
       self.health = 0
       self.alive = 1

    def introduce_self(self):
        print(self.name)


class Player:
    def __init__(self, name): 
       self.name = name
       self.damageDealt = 0
       
   
    def introduce_self(self):
        print(self.name)


#Method to check if something is an int
def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))


@bot.command(name='join')
async def join(ctx):
  author = str(ctx.author)[:-5] 
  if currentPlayers.count(author) == 0:

          playerList.append(Player(author)) #append the array and create a Player object
          currentPlayers.append(author) 
          await ctx.send(author + ' has joined the arena!') #sends the name 
          
          global enemy
          if len(currentPlayers) == 1:
            global hpScale
            hpScale = 75
            enemy = Enemy('Crab',len(playerList)*hpScale) #change this multiplier to something scalable for each\
            await ctx.send('A ' +enemy.name + ' has apeared in the arena! :crossed_swords:')
            
            enemy.health = enemy.maxHealth

          elif(enemy.alive):
            enemy.health = enemy.health + hpScale
            enemy.maxHealth = enemy.maxHealth + hpScale
            await ctx.send(enemy.name + ' has grown in strength '+ str(enemy.health) + '/' + str(enemy.maxHealth))
              
  else:  
        await ctx.send(author + ' has already joined the arena!') #sends the name 


@bot.command(name='d')
async def damage(ctx, arg):
  if IsInt(arg) and int(arg) >= 0 and int(arg) <= 200:
   author = str(ctx.author)[:-5] 
   for x in range(len(currentPlayers)):  
        if author == currentPlayers[x]:
          UserNumThatSentMsg = x
          break
        elif author == currentPlayers[0]:
          UserNumThatSentMsg = 0
          break

  playerList[UserNumThatSentMsg].damageDealt =  playerList[UserNumThatSentMsg].damageDealt + int(arg)    
  enemy.health = enemy.health - int(arg)
  await ctx.send(author + ' has dealt '+ arg +' damage!')
  await ctx.send(str(enemy.health) + '/' + str(enemy.maxHealth))
 
  if (enemy.health <= 0 and enemy.alive == 1):
    await ctx.send(enemy.name + ' has been defeated! Great job warriors :crossed_swords:')
    gameRunning = 0
    enemy.alive = 0
    for x in range(len(playerList)):
      await ctx.send(playerList[x].name + ' has dealt '+ str(playerList[x].damageDealt) +' damage in total!')     
      await ctx.send('The next enemy will be the boss monster "GIANT CRAB"')


      
      db.insert({'name': playerList[x].name, 'damage': playerList[x].damageDealt})
      db.search(User.name == playerList[x].name)

        


@bot.command(name='hp')
async def hp(ctx):
  await ctx.send(str(enemy.health) + '/' + str(enemy.maxHealth))



@bot.command(name='score')
async def score(ctx):
  for x in range(len(playerList)):
   await ctx.send(playerList[x].name + ' has dealt '+ str(playerList[x].damageDealt) +' damage in total!')

@bot.command(name='bg')
async def bg(ctx):
  await ctx.send(playerList[-1].name)
 # await ctx.send(playerList[UserNumThatSentMsg].name)
  await ctx.send(len(playerList))    


bot.run(os.getenv("TOKEN"))