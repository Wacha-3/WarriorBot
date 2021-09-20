import discord  #imports discord library
import tinydb   #import tinydb library (database)
import os       #working with operating system
import datetime
import sys 
import subprocess
import exercise

from tinydb import TinyDB, Query
from discord.ext import commands


today = datetime.datetime.now()

playerList = []  #initialise the array
currentPlayers = []
excercise = []
bot = commands.Bot(command_prefix='$')
db = TinyDB('db.json')
User = Query()
ExNum = 9

#initiallise an array of minions, and comapre it to date time to decide what enemies will apear 
class Enemy:
    def __init__(self, name, maxHealth): 
       self.name = name
       self.maxHealth = maxHealth
       self.health = 0
       self.alive = 1
   

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


@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
   
""""
def populateExercises():
  excerciseList.append(exercise.Exercise("Traps",30,60,150))
  excerciseList.append(exercise.Exercise("Biceps",8,15,75))
  excerciseList.append(exercise.Excercise("Shoulders",15,30,100))
  excerciseList.append(exercise.Excercise("Calves",30,60,150))
  excerciseList.append(exercise.Excercise("Core",0,500,250))

  excerciseList.append(exercise.Excercise("Back",0,20,100))
  excerciseList.append(exercise.Excercise("Chest",0,30,100))
  excerciseList.append(exercise.Excercise("Triceps",0,35,100))
  excerciseList.append(exercise.Excercise("Thighs",0,35,200))

populateExercises()
"""
#Sets the excercise which entails different peramiters
@bot.command(name='ex')
async def ex(ctx, arg): 
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
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  elif arg == "Biceps" or arg == "biceps" or arg == "2" :
    ExNum = 1
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  elif arg == "Shoulders" or arg == "shoulders" or arg == "3" :
    ExNum = 2
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  elif arg == "Calves" or arg == "calves" or arg == "4" :
    ExNum = 3
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  elif arg == "Core" or arg == "core" or arg == "5" :
    ExNum = 4
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep)) 
  elif arg == "Back" or arg == "back" or arg == "6" :
    ExNum = 5
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  elif arg == "Chest" or arg == "chest" or arg == "Pushups"  or arg == "pushups" or arg == "7" :
    ExNum = 6
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  elif arg == "Triceps" or arg == "triceps" or arg == "8" :
    ExNum = 7
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  elif arg == "Thighs" or arg == "thighs" or arg == "Squats" or arg == "squats" or arg == "9" :
    ExNum = 8
    await ctx.send(author + " has set the excercise to " + excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  else:
    await ctx.send(author + " has entered an invalid Excercise")
  
  await ctx.message.delete()



#This sets up the player with a temporary scorekeeping in the arena
@bot.command(name='join')
async def join(ctx):
  global ExNum 
  author = str(ctx.author)[:-5] 
  if ExNum == 9:
    await ctx.send('Please set an excercise before joining')
  elif ExNum >= 0 and ExNum <=8:
    if currentPlayers.count(author) == 0:
       playerList.append(Player(author)) #append the array and create a Player object
       currentPlayers.append(author) 
       await ctx.send(author + ' has joined the arena!') #sends the name   
       global enemy
       if len(currentPlayers) == 1:
         enemy = Enemy('Crab',len(playerList)*excercise[ExNum].hpScale)
         enemy.health = enemy.maxHealth
         await ctx.send('A ' +enemy.name + ' has apeared in The Arena! :crossed_swords: '+ str(enemy.health) + '/' + str(enemy.maxHealth))
       elif(enemy.alive):
        enemy.health = enemy.health + excercise[ExNum].hpScale
        enemy.maxHealth = enemy.maxHealth + excercise[ExNum].hpScale
        await ctx.send(enemy.name + ' has grown in strength '+ str(enemy.health) + '/' + str(enemy.maxHealth))         
    else:  
        await ctx.send(author + ' has already joined The Arena!') 
  else:
    await ctx.send('what the fuck did you just do???')
  await ctx.message.delete()


#Takes an argument which is the ammount of reps/damage that will be dealt to the enemy
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
   await ctx.send(author + ' has dealt '+ arg +' damage! ' + str(enemy.health) + '/' + str(enemy.maxHealth)) 
   if (enemy.health <= 0 and enemy.alive == 1):
     await ctx.send(enemy.name + ' has been defeated! Great job warriors :crossed_swords:')
     enemy.alive = 0
     for x in range(len(playerList)):
       await ctx.send(playerList[x].name + ' has dealt '+ str(playerList[x].damageDealt) +' damage in total! :muscle: ')          
  else:
    await ctx.send("Invalid rep range for "+ str(excercise[ExNum].name)  +" it is " + str(excercise[ExNum].minRep) + " to " + str(excercise[ExNum].maxRep)+ "reps") 
  await ctx.message.delete()
      

    
#Displays the current health of the enemy and the excercise name and rep range
@bot.command(name='hp')
async def hp(ctx):
  await ctx.send(str(enemy.health) + '/' + str(enemy.maxHealth))
  await ctx.send(excercise[ExNum].name + " rep range is " + str(excercise[ExNum].minRep) + "-" + str(excercise[ExNum].maxRep))
  await ctx.message.delete()


#Displays the current total damage for each player
@bot.command(name='score')
async def score(ctx):
  for x in range(len(playerList)):
   await ctx.send(playerList[x].name + ' has dealt '+ str(playerList[x].damageDealt) +' damage in total!')
   
#adding in code to update to database ---echo

@bot.command(name='listex')
async def listxx(ctx):
  for x in range(len(excercise)):
    await ctx.send("")

#Restarts the bot
@bot.command(name='restart')
async def restart(ctx):
  await ctx.send("Arena is being cleaned up for the next battle!")
  subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
  


bot.run(os.getenv("TOKEN")) 




    # db.insert({'name': playerList[x].name, 'damage': playerList[x].damageDealt})
     # db.search(User.name == playerList[x].name