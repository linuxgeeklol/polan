#Polskabot made by Borkductions.
#Bork
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("Horace, thanks for making me alive!")
    print ("bork bork")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: :flag_mc: ping!! xSSS! Kurwa!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)
#development
@bot.command(pass_context=True)
async def facepalm(ctx, user: discord.Member):
    await bot.say("Ouch! :sob: Do not of hittings Polska plox!") 

@bot.command(pass_context=True)
async def anschluss(ctx):
    await bot.say("Kurwa!")
    
@bot.command(pass_context=True)
async def syskey(ctx):
    await bot.say("**I am not a scammer!**")

@bot.command(pass_context=True)
async def space(ctx):
    await bot.say("Poland can into space? **Into space!**")

@bot.command(pass_context=True)
async def introduce(ctx):
    await bot.say("Hello. I am Polskabot. Kurwa!")
    await bot.say("I was created by **Horace Leung** in Hong Kong using the Python programming language. Thanks Horace for making me alive")
    await bot.say("I was designed to imitate **Polandball**, a character in a type of comic in the same name.")

@bot.command(pass_context=True)
async def dick(ctx, user: discord.Member):
    bot.say("**This guy's dick is "+str(random.randint(1, 999999999999999999999))+" inches long. Kurwa**")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def gay(ctx,user: discord.Member):
    await bot.say("**{} is ".format(user.name)+str(random.randint(1, 100))+"% gay. :gay_pride_flag: :gay_pride_flag: :gay_pride_flag: **")  

@bot.command(pass_context=True)
async def systeminfo32(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def wotispolandball(ctx):
    await bot.say("Polandball is a kind of webcomic.")
    await bot.say("https://polandball.cc/wp-content/uploads/2014/04/mxzUpoS.png")
    
@bot.command(pass_context=True)
async def bolan(ctx):
    await bot.say("Braise Allah!")
    print ("{} has became a terrorist".format(user.name))

@bot.command(pass_context=True)
async def slap(ctx, user:discord.Member):
    await bot.say("You are arrested for assaulting a fellow member ,{}.".format(user.name))
    await bot.say("**@Administrator press charges of violence againt {}".format(user.name))

@bot.command(pass_context=True)
async def communism(ctx):
    await bot.say("***Союз нерушимый республик свободных, Сплотила навеки Великая Русь. Да здравствует созданный волей народов, Единый, могучий Советский Союз!**")

@bot.command(pass_context=True)
async def communist(ctx, user:discord.Member):
    await bot.say("this guy is "+str(random.randint(1,100)+"%% percent communist."))
    await bot.say("Now go to gulag.")

@bot.command(pass_context=True)
async def cube(ctx, user:discord.Member):
    await bot.say("Congratulations. {} is officially a cube according to jewish physics. Oy Vey.".format(user.name)) 
    await bot.say("https://vignette.wikia.nocookie.net/steven-universe/images/9/95/Israelcube_0.png/revision/latest?cb=20151201160030")

async def detection(message):
    if not message.channel.is_private:
        try:
            workin = message.content.lower()
            still_workin = workin.split(" ")
            if bot.user.id == message.author.id:
                pass
            elif "germany" and "germoney" in still_workin:
                await bot.send_message(message.channel, "Nie.....debt collection!")
            elif "greece" and "debt" in still_workin:
                await bot.send_message(message.channel, "debt mate, yay!")
            elif "wrong" in still_workin:
                await bot.send_message(message.channel, "The only thing I did wrong in my life is running *fdisk* on my computer.")
            elif "eu" in still_workin:
                await bot.send_message(message.channel, "B A D")
            elif "european" and "union" in still_workin:
                await bot.send_message(message.channel, "B A D")
            elif "polan" and "poland" and "polen" in still_workin:
                await bot.send_message(message.channel, ":wave: Czecz")
            elif "ball" in still_workin:
                await bot.send_message(message.channel, ":wave: Czecz")
            elif "<@207883755392729088>" in still_workin:
                await bot.send_message(message.channel, ":wave: Czecz")
            elif "anschluss" and "annex" and "reich" in still_workin:
                await bot.send_message(message.channel, "KURWA!")
            elif "soviet" and "russia" in still_workin:
                await bot.send_message(message.channel, "*spits*")
        except:
            pass
            

bot.add_listener(detection, 'on_message')


    
bot.run(code)
