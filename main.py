import discord  #imports discord library
import tinydb   #import tinydb library (database)
import os       #working with operating system
import datetime

from tinydb import TinyDB, Query
from discord.ext import commands

today = datetime.datetime.now()

playerList = []  #initialise the array
currentPlayers = []
excercise = []
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
       self.exercise = ""

    def introduce_self(self):
        print(self.name)

class Excercise:
    def __init__(self, name, minRep, maxRep, hpScale):
      self.name = name
      self.minRep = minRep #make a list of excerices then use the perams to scale enemy
      self.maxRep = maxRep
      self.hpScale = hpScale


class Player:
    def __init__(self, name): 
       self.name = name
       self.damageDealt = 0
       
   
    def introduce_self(self):
        print(self.name)

""""
#Method to check if something is an int
def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
"""
@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
   

@bot.command(name='ex')
async def ex(ctx, arg): #yooooooooooooooooo echooooooo
  author = str(ctx.author)[:-5] 
  global ExNum 
  excercise.append(Excercise("Traps",30,60,150))
  excercise.append(Excercise("Biceps",8,15,75))
  excercise.append(Excercise("Shoulders",15,30,100))
  excercise.append(Excercise("Calves",30,60,150))
  excercise.append(Excercise("Core",0,500,250))

  excercise.append(Excercise("Back",0,20,100))
  excercise.append(Excercise("Chest",0,30,100))
  excercise.append(Excercise("Triceps",0,35,100))
  excercise.append(Excercise("Thighs",0,35,200))

  if arg == "Traps"  or arg == "traps" or arg == "1":
    ExNum = 0
  elif arg == "Biceps" or arg == "biceps" or arg == "2" :
    ExNum = 1
  elif arg == "Shoulders" or arg == "shoulders" or arg == "3" :
    ExNum = 2
  elif arg == "Calves" or arg == "calves" or arg == "4" :
    ExNum = 3
  elif arg == "Core" or arg == "core" or arg == "5" :
    ExNum = 4 
  elif arg == "Back" or arg == "back" or arg == "6" :
    ExNum = 5
  elif arg == "Chest" or arg == "chest" or arg == "7" :
    ExNum = 6
  elif arg == "Triceps" or arg == "triceps" or arg == "8" :
    ExNum = 7
  elif arg == "Thighs" or arg == "thighs" or arg == "9" :
    ExNum = 8
  else:
    await ctx.send(author + " has entered an invalid Excercise")
  await ctx.send(author + " has said " + arg)
  await ctx.send(author + " has set the excercise to " + excercise[ExNum].name)


@bot.command(name='join')
async def join(ctx):
  global ExNum 
  author = str(ctx.author)[:-5] 
  if currentPlayers.count(author) == 0:

          playerList.append(Player(author)) #append the array and create a Player object
          currentPlayers.append(author) 
          await ctx.send(author + ' has joined the arena!') #sends the name 
          
          global enemy
          if len(currentPlayers) == 1:
            enemy = Enemy('Crab',len(playerList)*excercise[ExNum].hpScale) #change this multiplier to something scalable for each\
            await ctx.send('A ' +enemy.name + ' has apeared in the arena! :crossed_swords:')
            
            enemy.health = enemy.maxHealth

          elif(enemy.alive):
            enemy.health = enemy.health + excercise[ExNum].hpScale
            enemy.maxHealth = enemy.maxHealth + excercise[ExNum].hpScale
            await ctx.send(enemy.name + ' has grown in strength '+ str(enemy.health) + '/' + str(enemy.maxHealth))
              
  else:  
        await ctx.send(author + ' has already joined the arena!') #sends the name 


@bot.command(name='d')
async def damage(ctx, arg):
  global ExNum
  author = str(ctx.author)[:-5] 
  if int(arg) >= excercise[ExNum].minRep and int(arg) <= excercise[ExNum].maxRep:
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
     enemy.alive = 0
     for x in range(len(playerList)):
       await ctx.send(playerList[x].name + ' has dealt '+ str(playerList[x].damageDealt) +' damage in total!')     
    
     await ctx.send('The next enemy will be the boss monster "GIANT CRAB"')

        
  else:
    await ctx.send("Invalid rep range for "+ str(excercise[ExNum].name)  +" it is:" + str(excercise[ExNum].minRep) + " to " + str(excercise[ExNum].maxRep))
    await ctx.send()

      
     # db.insert({'name': playerList[x].name, 'damage': playerList[x].damageDealt})
     # db.search(User.name == playerList[x].name)

        


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

@bot.command(name='restart')
async def restart(ctx):
  global Exnum
  enemy.clear()
  playerList.clear()
  ExNum=null

bot.run(os.getenv("TOKEN")) 