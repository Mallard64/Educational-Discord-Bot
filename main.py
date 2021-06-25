#Note that this code does not have the token.
import keep_alive
import time
import random
import discord
import json
from dotenv import load_dotenv
from discord.ext import commands
from discord import opus
invalidation = False
invalidation = False
def replace(key1, key2, dicty):
  print(key1)
  print(key2)
  print(dicty)
  key = list(dicty.values())
  notvalue = list(dicty.keys())
  dicty = list(dicty)
  print(dicty)
  if key1 in dicty:
    pogchamp = notvalue.index(key1)
    dicty[pogchamp] = key2
  newdict = {}
  for i in range(len(dicty)):
    newdict[dicty[i]] = key[i]
  print(newdict)
  return newdict


def ltos(s : list):
  c = ''
  for i in range(len(s)):
    c = c + s[i]
  return c

def decase(s):
  s = list(s)
  s[0] = s[0].upper()
  if '-' in s:
    b = s.index('-')
    s[b+1] = s[b+1].upper()
  s = ltos(s)
  return s


spoon = ['Spoon-Pepe','Super-Spoon','Lord-Spoon']
evolvedata = {
  'Smol-Pepe' : [16,'Scared-Pepe'],
  'Scared-Pepe' : [36, 'Pepe'],
  'Pepe' : ['Dank-Stone', 'Dank-Pepe_alpha', 'Dank-Pepe_omega'],
  'Time-Pepe' : ['Developer Token', 'Dank-Time-Pepe'],
  'Space-Pepe' : ['Developer Token', 'Dank-Space-Pepe'],
  'Tritium-Pepe' : ['Dank-Stone', 'Dank-Tritium-Pepe'],
  'Sad-Pepe' : [34, 'Smug-Pepe'],
  'Smug-Pepe' : ['Dank-Stone', 'Normie-Slayer-Pepe'],
  'Lord-Pepe' : ['Dank-Stone', 'Dank-Lord-Pepe'],
  'Mad-Pepe' : [12, 'reee-Pepe'],
  'reee-Pepe' : [24, 'Reeee-Pepe'],
  'Reeee-Pepe' : ['Dank-Stone', 'Dank-REEEEEEEEEE-Pepe'],
  'Old-Pepe' : [12, 'Glad-Pepe'],
  'Glad-Pepe' : [24, 'Happy-Pepe'],
  'Happy-Pepe' : ['Developer Token', 'error-Pepe'],
  'Shark-Pepe' : ['Dank-Stone', 'Dank-Shark-Pepe']
}
animals = ['Smol-Pepe', 'Scared-Pepe', 'Pepe', 'Time-Pepe', 'Space-Pepe', 'Mad-Pepe', 'reee-Pepe', 'Reeee-Pepe', 'error-Pepe', 'Old-Pepe', 'Glad-Pepe', 'Happy-Pepe', 'Sad-Pepe', 'Smug-Pepe', 'Lord-Pepe', 'Tritium-Pepe', 'Dank-Pepe_alpha', 'Dank-Pepe_omega', 'Normie-Slayer-Pepe', 'Enlightened-Pepe']
commonAnimals = ['Smol-Pepe', 'Mad-Pepe', 'reee-Pepe', 'Old-Pepe']
rareAnimals = ['Glad-Pepe', 'Reeee-Pepe', 'Happy-Pepe', 'Scared-Pepe', 'Sad-Pepe']
epicAnimals = ['Pepe','Smug-Pepe','Lord-Spoon','Super-Spoon','Spoon-Pepe','Gengar','Mega-Gengar']
legendAnimals = ['Time-Pepe', 'Space-Pepe', 'Lord-Pepe', 'Tritium-Pepe', 'Dank-Pepe_alpha', 'Dank-Pepe_omega', 'Normie-Slayer-Pepe', 'Enlightened-Pepe']

icondata = {
  'Smol-Pepe' : 'smolpepe.png',
  'Scared-Pepe' : 'scaredpepe.jpg',
  'Pepe' : "pepe.jpg",
  'Sad-Pepe' : 'sad-pepe.webp',
  'Smug-Pepe' : 'smugpepe.jpg',
  'Mad-Pepe' : 'madpepe.jpg',
  'reee-Pepe' : 'reee.jpg',
  'Reeee-Pepe' : 'Reeee.jpg',
  'Old-Pepe' : 'oldpepe.png',
  'Glad-Pepe' : 'gladpepe.jpg',
  'Happy-Pepe' : 'happypepe.jpg',
  'error-Pepe' : 'errorpepe.jpg',
  'Lord-Pepe' : 'lordpepe.png',
  'Time-Pepe' : 'timepepe.png',
  'Space-Pepe' : 'spacepepe.png',
  'Tritium-Pepe' : 'tritiumpepe.png',
  'Enlightened-Pepe' : 'enlightenedpepe.jpg',
  'Mexican-Pepe' : 'mexicanpepe.jpg',
  'Dark-Pepe' : 'darkpepe.jpg',
  'Spoon-Pepe' : 'spoonpepe.png',
  'Super-Spoon' : 'superspoon.jpg', 
  'Lord-Spoon' : 'lordspoon.jpg',
  'Shark-Pepe' : 'sharkpepe.jpg',
  'Gengar' : 'gengar.png',
  'Mega-Gengar' : 'megagengar.png',
}

movedata = {'Smol-Pepe' : ["Punch","Heal","Killing-Intent","Anticipate"], 'Scared-Pepe' : ["Punch","Kick","Heal","Cry"], 'Pepe' : ["REEEEEE", "Pepe-Punch",'Pepe-Kick','Protect'], 'Time-Pepe' : ['Distortion','Temporal-REEEEEE','Pepe-Punch','Pepe-Kick'], 'Space-Pepe' : ['Space-Warp','Spatial-REEEEEE','Pepe-Punch','Pepe-Kick'], 'Mad-Pepe' : ['Punch','Kick','Heal','Protect'], 'reee-Pepe' : ['Punch','Kick','Heal','reee'], 'Reeee-Pepe' : ['Pepe-Punch','Pepe-Kick','Reeee','Protect'], 'error-Pepe' : ['Glitch','Hack','Pepe-Punch','Pepe-Kick'], 'Old-Pepe' : ['Punch','Kick','Protect','Heal'], 'Glad-Pepe' : ['Punch','Kick','Protect','Heal'], 'Happy-Pepe' : ['Happy','Pepe-Punch','Pepe-Kick'], 'Sad-Pepe' : ["Punch","Kick","Sulk","Protect"], 'Smug-Pepe' : ['Pepe-Punch','Pepe-Kick','Arrogance','Protect'], 'Lord-Pepe' : ["Judgement", "Godly-Smite", "Obliterate", "Nullification"], 'Tritium-Pepe' : ["Tritium-Laser", 'Pepe-Punch','Pepe-Kick','Radioactive'], 'Dank-Pepe_alpha' : ['Alpha-Dominance','Pepe-Punch','Pepe-Kick','Protect'], 'Dank-Pepe_omega' : ['Omega-Dominance','Pepe-Punch','Pepe-Kick','Protect'], 'Normie-Slayer-Pepe' : ['Normie-Slayer', 'Pepe-Punch','Pepe-Kick','Protect'], 'Enlightened-Pepe' : ['Big-Brain','Pepe-Punch','Pepe-Kick','Brain-Control'],'Dark-Pepe' : ['Dark-Aura','Dark-Flame','Pepe-Punch','Pepe-Kick'], 'Mexican-Pepe' : ['STFU','Pepe-Punch','Pepe-Kick','Protect'], 'Shark-Pepe' : ['Bite','Pepe-Bite','Pepe-Punch','Pepe-Kick'], 'Dank-Lord-Pepe' : ["Judgement", "Godly-Smite", "Obliterate", "Nullification"],'Gengar' : ["Shadow-Ball", "Shadow-Claw", "Sludge-Bomb", "Grand-Cathedral"], 'Mega-Gengar' : ["Shadow-Ball", "Shadow-Claw", "Sludge-Bomb", "Grand-Cathedral"]}
#future notes for move power
#[power,effects,target,amount]
#hp is 0,def is 1,atk is 2

from discord.ext import commands
from discord.ext.commands import Bot
from globals import stats
hp1 = 100
hp2 = 100
file4_name = 'pog.json'
file69_name = 'moves.json'
load_dotenv()
with open(file4_name, "r") as yoyo_file:
  TOKEN = json.load(yoyo_file)
GUILD = 'Church of Pepe' #os.getenv('Pointless Chat')
string_utf = TOKEN.encode()
bot = commands.Bot(command_prefix='pepe ')
TOKEN = string_utf.decode()
opus.load_opus("libopus.so.0")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print('opus loaded = ', opus.is_loaded())

adcharacters = ['Lord-Spoon','Super-Spoon','Spoon-Pepe', 'Gengar','Mega-Gengar']

file1_name = "OwO.json"
file2_name = "bal.json"
file4_name = 'items.json'
file5_name = 'levels.json'
file7_name = 'select.json'
with open(file1_name, "r") as OwO_file:
  userdata = json.load(OwO_file)
with open(file2_name, "r") as bal_file:
  baldata = json.load(bal_file)
with open(file4_name, "r") as item_file:
 itemdata = json.load(item_file) 
with open(file5_name, "r") as level_file:
  leveldata = json.load(level_file)
with open('select.json', "r") as select_file:
  selectdata = json.load(select_file)
with open('moves.json', "r") as move_file:
  moves = json.load(move_file)

@bot.command(name = 'start', help = 'to start the rpg. Must be used.')
async def start(ctx):
  if not str(ctx.author.id) in userdata:
    if str(ctx.author.id) in userdata:
      print('wtf man')
    else:
      userdata[str(ctx.author.id)] = ['Smol-Pepe']
  else:
    print('bruh, no restarting')
  if not str(ctx.author.id) in baldata:
    baldata[str(ctx.author.id)] = 0
    if str(ctx.author.id) in userdata:
      print('wtf man')
    else:
      baldata[str(ctx.author.id)] = 10
  else:
    print('bruh, no restarting')
  if not str(ctx.author.id) in itemdata:
    itemdata[str(ctx.author.id)] = []
  if not str(ctx.author.id) in leveldata:
    leveldata[str(ctx.author.id)] = {"Smol-Pepe" : 1}
  if not str(ctx.author.id) in selectdata:
    selectdata[str(ctx.author.id)] = "Smol-Pepe"
  if not str(ctx.author.id) in moves:
    moves[str(ctx.author.id)] = ["Punch","Heal","Killing-Intent","Anticipate"]
  with open(file1_name, "w") as OwO_file:
    json.dump(userdata, OwO_file)
  with open(file2_name, "w") as bal_file:
    json.dump(baldata, bal_file)
  with open(file4_name, "w") as item_file:
    json.dump(itemdata, item_file)
  with open(file5_name, "w") as level_file:
    json.dump(leveldata, level_file)
  with open("select.json", "w") as select_file:
    json.dump(selectdata, select_file)

@bot.command(name = 'bal', help = 'look at that money!')
async def bala(ctx):
  with open(file2_name, "r") as bal_file:
    baldata = json.load(bal_file)
  print(baldata)
  if str(ctx.author.id) not in baldata:
    await ctx.send('As a reward for starting, you have been given 10,000 credits.')
    baldata[ctx.author.id] = 10000
  with open(file2_name, "w") as bal_file:
    json.dump(baldata, bal_file)
  await ctx.send('you have ' + str(baldata[str(ctx.author.id)]) + ' credits.')

@bot.command(name = 'box', help = 'see your glorious characters')
async def charsa(ctx, ff = 'o'):
  if ff == 'o':
    sync()
    chars = userdata[str(ctx.author.id)]
    await ctx.send('You have ' + ', '.join(chars))
  else:
    if ff in userdata:
      chars = userdata[ff]
      await ctx.send(ff + ' has ' + ', '.join(chars))
    else:
      await ctx.send('Oops, that does not work!')

@bot.command(name = 'invalidate', help = 'invalidate stuff')
async def apa(ctx):
  if ctx.author.name == 'MEE7':
    invalidation = True
    time.sleep(2)
    await ctx.send('everything was invalidated')
    invalidation = False
  else:
    await ctx.send('no permission :(')


def sync():
  file1_name = "OwO.json"
  file2_name = "bal.json"
  file4_name = "items.json"
  with open(file1_name, "r") as OwO_file:
    userdata = json.load(OwO_file)
  with open(file2_name, "r") as bal_file:
    baldata = json.load(bal_file)
  with open(file4_name, "r") as item_file:
    itemdata = json.load(item_file)

@bot.command(name = 'kick', help = 'kick some people')
async def kick(ctx, member : discord.Member):
  if invalidation == False:
    if member.name == "MEE8" or member.name == 'MEE7' or member.name == 'MEE9':
      await ctx.send('no')
    else:
      await ctx.guild.ban(member)
      await ctx.send(member + ' has been kicked.')

@bot.command(name = 'save', help = 'save progress')
async def save(ctx):
  if invalidation == False:
    global userdata
    with open(file1_name, "w") as OwO_file:
      json.dump(userdata, OwO_file)
    with open(file2_name, "w") as bal_file:
      json.dump(baldata, bal_file)
    with open(file4_name, "w") as item_file:
      json.dump(itemdata, item_file)
    with open(file5_name, "w") as level_file:
      json.dump(leveldata, level_file)
    await ctx.send('File saved!')

@bot.command(name = 'items', help = 'check your items')
async def items(ctx):
  sync()
  await ctx.send("You have: " + str(itemdata[str(ctx.message.author.id)]))


@bot.command(name = 'battle', help = 'get drunky and fight')
async def duel(ctx):
  if invalidation == False:
    opponents = ['Pepe the Frog', 'MEE7', 'aaaaaaa', 'dumpster', 'Lord Spoon', 'Dank Memer', 'MEE6', 'OwO', 'Mr. Sakurai']
    character = selectdata[str(ctx.author.id)]
    pointless_counter = 0
    opponent = random.choice(animals)
    opponentname = random.choice(opponents)
    oi = str(ctx.author.id)
    chars = userdata[oi]
    print(chars)
    print(character in chars)
    if character in chars:
      message = await ctx.send(ctx.author.name + ' is going to battle!')
      time.sleep(1)
      await message.edit(content = 'Your opponent is ' + opponentname)
      time.sleep(1)
      await message.edit(content = opponentname + ' sent out ' + opponent + '!')
      enemylevel = leveldata[oi][character] + random.randrange(-5,5)
      php = stats[character][0] + leveldata[oi][character] * 2
      ehp = stats[opponent][0] + enemylevel * 2
      eatk = stats[opponent][2] + enemylevel * 2
      pdef = stats[character][1] + leveldata[oi][character] * 2
      edef = stats[opponent][1] + enemylevel * 2
      patk = stats[character][2] + leveldata[oi][character] * 4
      movepower = {'Punch' : [30,2,patk,10],'Heal' : [0,0,php,30],'Killing-Intent' : [0,0,edef,-20],'Anticipate' : [0,1,pdef,20],'Kick' : [50,0,php,0],'Cry' : [0,2,eatk,-10],'REEEEEE' : [50,1,edef,-30],'Pepe-Punch' : [60,2,patk,20],'Protect' : [0,1,pdef,30],'Pepe-Kick' : [70,0,php,0],'Distortion' : [60,0,php,20],'Temporal-REEEEEE' : [60,0,php,30],'Spatial-REEEEEE' : [60,1,pdef,30],'Space-Warp' : [60,0,php,20],'reee' : [20,1,edef,-20],'Reeee' : [45,1,edef,-40],'Glitch' : [70,1,edef,-50],'Hack' : [80,0,php,0],'Happy' : [0,0,php,50],'Sulk' : [0,2,eatk,-20],'Arrogance' : [0,2,patk,80],'Judgement' : [100,2,patk,10000],'Godly-Smite' : [40000,0,php,-30],'Obliterate' : [100,1,edef,-10000],'Nullification' : [0,0,php,1000000],'Tritium-Laser' : [80,1,edef,-30],'Radioactive' : [0,1,edef,-70],'Alpha-Dominance' : [0,2,patk,80],'Omega-Dominance' : [0,1,pdef,80],'Normie-Slayer' : [130,1,pdef,-60],'Big-Brain' : [0,2,patk,70],'Dark-Aura' : [70,1,edef,-40],'Dark-Flame' : [80,1,edef,-30],'STFU' : [70,1,edef,-40],'Bite' : [50,1,edef,-20],'Pepe-Bite' : [70,1,edef,-10], 'Shadow-Ball' : [70,1,edef,-10],'Shadow-Claw' : [70,2,patk,15],'Sludge-Bomb' : [60,1,edef,-25],'Grand-Cathedral' : [0,2,patk,90]}
      nodamage = ['Anticipate','Cry','Heal','Big-Brain','Radioactive','Alpha-Dominance','Omega-Dominance','Nullification','Protect','Arrogance','Killing-Intent']
      while ehp > 0 and php > 0 and pointless_counter < 12:
        time.sleep(1)
        emove = random.choice(movedata[opponent])
        emove = movepower[emove]
        if eatk + emove[0] >= pdef:
          ivalue = emove[0]
          if emove[0] == 0:
            emove[0] = pdef-eatk
          await message.edit(content = opponent + f' used {random.choice(movedata[opponent])}, which did {str(eatk + emove[0] - pdef)} damage.')
          php -= (eatk + emove[0] - pdef)
          if str(emove[2]) == 'pdef':
            pdef += emove[3]
          elif str(emove[2]) == 'patk':
            patk += emove[3]
          elif str(emove[2]) == 'edef':
            edef += emove[3]
          else:
            eatk += emove[3]
          emove[0] = ivalue
        else:
          await message.edit(content = f'{opponent} attacked!')
          time.sleep(1.5)
          await message.edit(content = "...it did no damage")
          pointless_counter += 1
        time.sleep(1.5)
        await message.edit(content = f'{character} is at {str(php)} health.')
        #now php atk
        time.sleep(1.5)
        await ctx.send('What will your Pepe do? Your case-sensitive moves are: ' + str(movedata[character]))
        pmove = await bot.wait_for('message')
        pmove = pmove.content
        pmove = decase(pmove)
        pinfo = movepower[pmove]
        if patk + pinfo[0] >= edef:
          ivalue = pinfo[0]
          if pinfo[0] == 0:
            pinfo[0] = edef-patk
          await message.edit(content = character + f' attacked, which did {str(patk + pinfo[0] - edef)} damage.')
          ehp -= (patk + pinfo[0] - edef)
          if str(pinfo[2]) == 'pdef':
            pdef += pinfo[3]
          elif str(pinfo[2]) == 'patk':
            patk += pinfo[3]
          elif str(pinfo[2]) == 'edef':
            edef += pinfo[3]
          else:
            eatk += pinfo[3]
          pinfo[0] = ivalue
        else:
          await message.edit(content = character + ' attacked!')
          time.sleep(1.5)
          await message.edit(content = "...it did no damage")
          pointless_counter += 1
        time.sleep(1.5)
        await message.edit(content = opponent + ' is at ' + str(ehp) + ' health.')
      time.sleep(1.5)
      if ehp > 0:
        await message.edit(content = opponent + ' wins!')
        time.sleep(1.5)
        await message.edit(content = 'weakling, you lost to an AI')
      else:
        await message.edit(content = 'You win!')
        time.sleep(1.5)
        await message.edit(content = 'You recieved ' + str(php - ehp) + ' credits!')
        baldata[oi] += php - ehp
        with open(file2_name, "w") as bal_file:
          json.dump(baldata, bal_file)
    else:
      await ctx.send("Uh... who?")

@bot.command(name = 'pvpbattle', help = 'WIP')
async def pvp(ctx,opponent : discord.Member):
      print(opponent)
      print(type(opponent))
      await ctx.send('@' + opponent.name + ', ' + ctx.author.name + ' would like to battle! Type y to accept and n to decline. Remember to go to the channel which you were pinged in.')
      oi = str(ctx.author.id)
      name = ctx.author.name
      io = str(opponent.id)
      result = await bot.wait_for('message')
      result = result.content
      if result == 'y':
        character = selectdata[str(ctx.author.id)]
        echaracter = selectdata[str(io)]
        await ctx.send(opponent.name + ' has accepted your battle! Get ready...')
        await ctx.send('Let the battles begin!')
        message = await ctx.send(ctx.author.name + ' is going to battle!')
        await message.edit(content = opponent.name + ' sent out ' + echaracter + '!')
        enemylevel = leveldata[io][character]
        php = stats[character][0] + leveldata[oi][character] * 2
        ehp = stats[echaracter][0] + leveldata[io][echaracter] * 2
        eatk = stats[echaracter][2] + leveldata[io][echaracter] * 2
        pdef = stats[character][1] + leveldata[oi][character] * 2
        edef = stats[echaracter][1] + leveldata[io][echaracter] * 2
        patk = stats[character][2] + leveldata[oi][character] * 2
        movepower = {'Punch' : [30,2,patk,10],'Heal' : [0,0,php,30],'Killing-Intent' : [0,0,edef,-20],'Anticipate' : [0,1,pdef,20],'Kick' : [50,0,php,0],'Cry' : [0,2,eatk,-10],'REEEEEE' : [50,1,edef,-30],'Pepe-Punch' : [60,2,patk,20],'Protect' : [0,1,pdef,30],'Pepe-Kick' : [70,0,php,0],'Distortion' : [60,0,php,20],'Temporal-REEEEEE' : [60,0,php,30],'Spatial-REEEEEE' : [60,1,pdef,30],'Space-Warp' : [60,0,php,20],'reee' : [20,1,edef,-20],'Reeee' : [45,1,edef,-40],'Glitch' : [70,1,edef,-50],'Hack' : [80,0,php,0],'Happy' : [0,0,php,50],'Sulk' : [0,2,eatk,-20],'Arrogance' : [0,2,patk,80],'Judgement' : [100,2,patk,10000],'Godly-Smite' : [40000,0,php,-30],'Obliterate' : [100,1,edef,-10000],'Nullification' : [0,0,php,1000000],'Tritium-Laser' : [80,1,edef,-30],'Radioactive' : [0,1,edef,-70],'Alpha-Dominance' : [0,2,patk,80],'Omega-Dominance' : [0,1,pdef,80],'Normie-Slayer' : [130,1,pdef,-60],'Big-Brain' : [0,2,patk,70],'Dark-Aura' : [70,1,edef,-40],'Dark-Flame' : [80,1,edef,-30],'STFU' : [70,1,edef,-40],'Bite' : [50,1,edef,-20],'Pepe-Bite' : [70,1,edef,-10],'Shadow-Ball' : [70,1,edef,-10],'Shadow-Claw' : [70,2,patk,15],'Sludge-Bomb' : [60,1,edef,-25],'Grand-Cathedral' : [0,2,patk,90], 'Brain-Control' : [100,0,edef,0]}
        nodamage = ['Anticipate','Cry','Heal','Big-Brain','Radioactive','Alpha-Dominance','Omega-Dominance','Nullification','Protect','Arrogance','Killing-Intent']
        while ehp > 0 and php > 0:
          time.sleep(1)
          await ctx.send(opponent.name + ', what will your Pepe do? Your case-sensitive moves are: ' + str(movedata[echaracter]))
          emove = await bot.wait_for('message')
          emove = emove.content
          emove = decase(emove)
          oldemove = emove
          emove = movepower[emove]
          if eatk + emove[0] >= pdef:
            ivalue = emove[0]
            if emove[0] == 0:
              emove[0] = pdef-eatk
            await message.edit(content = opponent.name + f"'s {echaracter} used {oldemove}, which did {str(eatk + emove[0] - pdef)} damage.")
            php -= (eatk + emove[0] - pdef)
            if str(emove[2]) == 'pdef':
              pdef += emove[3]
            elif str(emove[2]) == 'patk':
              patk += emove[3]
            elif str(emove[2]) == 'edef':
              edef += emove[3]
            else:
              eatk += emove[3]
            emove[0] = ivalue
          else:
            await message.edit(content = f"{opponent.name}'s {echaracter} attacked!")
            time.sleep(1.5)
            await message.edit(content = "...it did no damage")
          time.sleep(1.5)
          await message.edit(content = f'{character} is at {str(php)} health.')
          #now php atk
          time.sleep(1.5)
          await ctx.send(name + ', what will your Pepe do? Your case-sensitive moves are: ' + str(movedata[character]))
          pmove = await bot.wait_for('message')
          pmove = pmove.content
          pinfo = movepower[pmove]
          pmove = decase(pmove)
          if patk + pinfo[0] >= edef:
            ivalue = pinfo[0]
            if pinfo[0] == 0:
              pinfo[0] = edef-patk
            await message.edit(content = character + f' attacked, which did {str(patk + pinfo[0] - edef)} damage.')
            ehp -= (patk + pinfo[0] - edef)
            if str(pinfo[2]) == 'pdef':
              pdef += pinfo[3]
            elif str(pinfo[2]) == 'patk':
              patk += pinfo[3]
            elif str(pinfo[2]) == 'edef':
              edef += pinfo[3]
            else:
              eatk += pinfo[3]
            pinfo[0] = ivalue
          else:
            await message.edit(content = character + ' attacked!')
            time.sleep(1.5)
            await message.edit(content = "...it did no damage")
          time.sleep(1.5)
          await message.edit(content = opponent.name + f"'s {echaracter} is at " + str(ehp) + ' health.')
        time.sleep(1.5)
        if ehp > 0:
          await message.edit(content = opponent.name + ' wins!')
          time.sleep(1.5)
          await message.edit(content = opponent.name + ' recieved ' + str(ehp - php) + ' credits!')
          baldata[io] += ehp - php
          with open(file2_name, "w") as bal_file:
            json.dump(baldata, bal_file)
        else:
          await message.edit(content = name + ' wins!')
          time.sleep(1.5)
          await message.edit(content = name + ' recieved ' + str(php - ehp) + ' credits!')
          baldata[oi] += php - ehp
          with open(file2_name, "w") as bal_file:
            json.dump(baldata, bal_file)
      else:
        await ctx.send(opponent.name + ' has declined your battle.')
# @bot.command(name = 'vbattle', help = 'battle villains all across the series!')
# async def vb(ctx):
  
#   character = selectdata[str(ctx.author.id)]
#   pointless_counter = 0
#   opponent = random.choice(animals)
#   opponentname = 
#   oi = str(ctx.author.id)
#   chars = userdata[oi]
#   print(chars)
#   print(character in chars)
#   if character in chars:
#     message = await ctx.send(ctx.author.name + ' is going to battle!')
#     time.sleep(1)
#     await message.edit(content = 'Your opponent is ' + opponentname)
#     time.sleep(1)
#     await message.edit(content = opponentname + ' sent out ' + opponent + '!')
#     php = stats[character][0] + leveldata[oi][character] * 2
#     ehp = stats[opponent][0] + random.randrange(2, 20)
#     eatk = stats[opponent][2] + random.randrange(4, 40)
#     pdef = stats[character][1] + leveldata[oi][character] * 2
#     edef = stats[opponent][1] + random.randrange(2, 20)
#     patk = stats[character][2] + leveldata[oi][character] * 4
#     while ehp > 0 and php > 0 and pointless_counter < 12:
#       time.sleep(1)
#       if stats[opponent][2] > stats[character][1]:
#         await message.edit(content = opponent + f' attacked, which did {str(eatk - pdef)} damage.')
#         php -= (eatk-pdef)
#       else:
#         await message.edit(content = f'{opponent} attacked!')
#         time.sleep(1)
#         await message.edit(content = "...it did no damage")
#         pointless_counter += 1
#       time.sleep(1)
#       await message.edit(content = f'{character} is at {str(php)} health.')
#       #now php atk
#       time.sleep(1)
#       if patk > edef:
#         await message.edit(content = character + f' attacked, which did {str(patk-edef)} damage.')
#         ehp -= (patk - edef)
#       else:
#         await message.edit(content = character + ' attacked!')
#         time.sleep(1)
#         await message.edit("...it did no damage")
#         pointless_counter += 1
#       time.sleep(1)
#       await message.edit(content = opponent + ' is at ' + str(ehp) + ' health.')
#     time.sleep(1)
#     if ehp > 0:
#       await message.edit(content = opponent + ' wins!')
#       time.sleep(1)
#       await message.edit(content = 'weakling, you lost to an AI')
#     else:
#       await message.edit(content = 'You win!')
#       time.sleep(1)
#       await message.edit(content = 'You recieved ' + str(php - ehp) + ' credits!')
#       baldata[oi] += php - ehp
#       with open(file2_name, "w") as bal_file:
#         json.dump(baldata, bal_file)
#   else:
#     await ctx.send("Uh... who?")

@bot.command(name = 'shop', help = 'buy some characters')
async def shopit(ctx):
  if invalidation == False:
    initialuser = ctx.message.author.name
    sync()
    oii = str(ctx.author.id)
    items = ['Dark-Pepe', 'Shark-Pepe', 'Senor-Pepe', 'error-Pepe', 'Levelup', 'Dank-Stone', 'Lucky-Charm']
    prices = {
      'Dark-Pepe' : 1000000,
      'Shark-Pepe' : 7000,
      'Mexican-Pepe' : 20000,
      'error-Pepe' : 'Developer Token',
      'Levelup' : 100,
      'Dank-Stone' : 1000000,
      'Lucky-Charm' : 1000,
    }
    await ctx.send('Trader: Hello! What can I do for you?')
    await ctx.send('Here are our Pepes/items for sale.')
    for i in range(len(items)):
      chars = userdata[oii]
      await ctx.send(items[i])
    contento = await bot.wait_for('message')
    contento = contento.content
    contento = decase(contento)
    if type(prices[contento]) == int:
      if baldata[oii] >= prices[contento] and 'Developer Token' in itemdata[oii]:
        if 'Developer Token' in itemdata[oii]:
          await ctx.send(f'Hello, developer {ctx.message.author.name}')
        else:
          baldata[oii] -= prices[contento]
        await ctx.send('Item bought!')
        if contento != 'Levelup':
          chars.append(contento)
          leveldata[oii][contento] = 1
        else:
          leveldata[oii][selectdata[oii]] += 1
          pög = evolvedata[selectdata[oii]][0]
          if type(pög) == str:
            if evolvedata[selectdata[oii]][0] in itemdata[oii]:
              oldpoke = selectdata[oii]
              selectdata[oii] = evolvedata[selectdata[oii]][1]
              leveldata[oii] = replace(oldpoke, selectdata[oii], leveldata[oii])
              print(leveldata)
          else:
            if leveldata[oii][selectdata[oii]] >= evolvedata[selectdata[oii]][0]:
              selectdata[oii] = evolvedata[selectdata[oii]][1]
              oldpoke = selectdata[oii]
              leveldata[oii] = replace(oldpoke, selectdata[oii], leveldata[oii])
              print(leveldata)
          chars = list(leveldata[oii].keys())
          userdata[oii] = chars
          moves[oii][contento] = movedata[contento]
          print(userdata)
          print('saving files')
          with open('OwO.json', "w") as OwO_file:
            json.dump(userdata, OwO_file)
          with open(file2_name, "w") as bal_file:
            json.dump(baldata, bal_file)
          with open(file4_name, "w") as item_file:
            json.dump(itemdata, item_file)
          with open('select.json', "w") as select_file:
            json.dump(selectdata, select_file)
          with open('levels.json', "w") as level_file:
            json.dump(leveldata, level_file)
          leveldata[oii][contento] = 1
          with open(file1_name, "w") as OwO_file:
            json.dump(userdata, OwO_file)
          with open(file2_name, "w") as bal_file:
            json.dump(baldata, bal_file)
          with open(file4_name, "w") as item_file:
            json.dump(itemdata, item_file)
          with open('moves.json', "w") as move_file:
            json.dump(moves, move_file)
      elif not contento in items:
        await ctx.send("Hmm, this isn't in the shop.")
      else:
        await ctx.send("An unknown error occurred. :(")
    else:
      if 'Developer Token' in itemdata[oii]:
        await ctx.send(f"hello, developer {ctx.message.author.name}")
        chars.append(contento)
        userdata[oii] = chars
        print('saving files')
        with open('OwO.json', "w") as OwO_file:
          json.dump(userdata, OwO_file)
        with open(file2_name, "w") as bal_file:
          json.dump(baldata, bal_file)
        with open(file4_name, "w") as item_file:
          json.dump(itemdata, item_file)
        with open('select.json', "w") as select_file:
          json.dump(selectdata, select_file)
        with open('levels.json', "w") as level_file:
          json.dump(leveldata, level_file)
        with open('moves.json', "w") as move_file:
            json.dump(moves, move_file)
        leveldata[oii][contento] = 1

@bot.command(name = 'select', help = 'select character to be your buddy')
async def aaaaaa(ctx, character):
  auaua = str(ctx.author.id)
  chars = userdata[auaua]
  if decase(character) in chars:
    await ctx.send('Change made')
    selectdata[auaua] = decase(character)
    with open('select.json', "w") as select_file:
      json.dump(selectdata, select_file)
  else:
    await ctx.send('A communication error has occured :angry:')


@bot.command(name = 'info', help = 'get info on a character')
async def infod(ctx, character):
  if invalidation == False:
    oiii = str(ctx.author.id)
    chars = userdata[oiii]
    character = decase(character)
    if character in chars:
      await ctx.send('Pepe info recieved!')
      for i in range(len(stats[character])):
        stufff = ['HP: ', 'Def: ', 'Atk: ']
        await ctx.send(stufff[i] + str(stats[character][i]))
    else:
      await ctx.send('A communications error has occurred.')



@bot.command(name = 'search', help = 'go on the internet to find pepes')
async def hunt9(ctx):
  print('searcgubg')
  if invalidation == False:
    global userdata
    print('glub glub')
    oiyah = str(ctx.author.id)
    if oiyah not in userdata:
      await ctx.send('go do pepe start first')
    chars = userdata[oiyah]
    inv = itemdata[oiyah]
    foundAnimal = random.randrange(1,100)
    if 'Lucky-Charm' in inv:
      pepe = inv.index('Lucky-Charm')
      if foundAnimal < 20:
        selectedChar = random.choice(commonAnimals)
        pokemontype = 'Common'
      elif foundAnimal >= 20 and foundAnimal < 40:
        selectedChar = random.choice(rareAnimals)
        pokemontype = 'Rare'
      elif foundAnimal >= 41 and foundAnimal < 80:
        selectedChar = random.choice(epicAnimals)
        pokemontype = 'Epic'
      else:
        selectedChar = random.choice(legendAnimals)
        pokemontype = 'Legend'
      itemdata[oiyah][pepe] = None
    else:
      print('frog frog')
      if foundAnimal < 59:
        selectedChar = random.choice(commonAnimals)
        pokemontype = 'Common'
      elif foundAnimal >= 59 and foundAnimal < 89:
        selectedChar = random.choice(rareAnimals)
        pokemontype = 'Rare'
      elif foundAnimal >= 89 and foundAnimal < 99:
        selectedChar = random.choice(epicAnimals)
        pokemontype = 'Epic'
      else:
        selectedChar = random.choice(legendAnimals)
        pokemontype = 'Legend'
    chars.append(selectedChar)
    leveldata[oiyah][selectedChar] = 1
    if pokemontype == 'Common':
      await ctx.send(ctx.author.name + ' went surfing the intenet and recieved ' + selectedChar + '!')
    elif pokemontype == 'Rare':
      await ctx.send(ctx.author.name + ' went unto thy internet and recieved ' + selectedChar + ', nice find')
    elif pokemontype == 'Epic':
      await ctx.send('you somehow went onto the internet and recieved a ' + selectedChar + ', h')
    else:
      await ctx.send('HOW?! YOU JUST FOUND A ' + selectedChar + "! THAT'S ONLY APPEARS IN 1 OUT OF 200000000 MEMES!")
    await ctx.send(file=discord.File(icondata[selectedChar]))
    moves[oiyah][selectedChar] = movedata[selectedChar]
    with open(file1_name, "w") as OwO_file:
      json.dump(userdata, OwO_file)
    with open('levels.json', "w") as level_file:
      json.dump(leveldata, level_file)



@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    role = discord.utils.get(member.server.roles, id= "Weakling")
    await bot.add_roles(member, role)
    

@bot.event
async def on_member_leave(member):
  await member.create_dm()
  await member.dm_channel.send(
    f'Goodbye. I hope to see you again :('
  )

@bot.command(name = 'magic8', help = 'Harness the power of the Magic 8 ball')
async def magic8(context, question : str):
  if invalidation == False:
    print(question)
    await context.send("I knoweth all (including your question), ask me.")
    answers = ['Yes', 'No', 'Impossible', 'Certainly', 'Maybe', 'Debatable']
    await context.send("Answer: " + random.choice(answers))

@bot.command(name = 'roll', help = 'Rolls a dice, dumb dumb')
async def roll(context, sides : int):
  if invalidation == False:
    await context.send(str(random.randrange(1, sides)))

@bot.command(name = 'text_channel', help = 'Make a new text channel')
async def create_channel(ctx, channel_name = 'REEEEE'):
  if invalidation == False:
    guild = ctx.guild
    await ctx.send(f'Creating a new channel: {channel_name}')
    await guild.create_text_channel(channel_name)

@bot.command(name = 'voice_channel', help = 'Make a new voice channel')
async def create_channel(ctx, channel_name = 'REEEEE'):
  if invalidation == False:
    guild = ctx.guild
    print(f'Creating a new channel: {channel_name}')
    await ctx.send(f'Creating a new channel: {channel_name}')
    await guild.create_voice_channel(channel_name)


@bot.command(name = 'ping', help = "Screw the kill command, you'll kill them with these pings.")
async def ping(ctx, ping, quantity : int):
    for i in range(1,quantity):
      if invalidation == False:
        await ctx.send(str(ping))
      else:
        break
        return


keep_alive.keep_alive()


bot.run(TOKEN)


