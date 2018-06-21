import random
import math
import time
import discord
from discord.ext.commands import Bot
from discord.ext import commands

#VERSION 3


#start ===========================================================================================================================================================
client = commands.Bot(command_prefix="s!")

client.remove_command("help")

registered_users = ALL_USERS

users_info = ALL_INFOS

#Simple coin system ----------------------------------------------------------------------------------------------------
@client.command(pass_context=True)
async def profile(context):
    if str(context.message.author) in registered_users:
        author_username = str(context.message.author)
        username_length = len(author_username) - 5
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        embed = discord.Embed(title="__ %s __'s Profile" % (str(author_username[0:username_length])), description="**Current Level: " + str(users_info[str(context.message.author)]["lvl"]) + "** \n" + \
                              "Experience Points: " + str(users_info[str(context.message.author)]["exp"]) + "/" + str(max_exp) + " \n" + \
                              "Current Amounts of Shruggy Coins: " + str(users_info[str(context.message.author)]["coins"]) + " ", color=discord.Color.green())
        embed.set_thumbnail(url=context.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        registered_users.insert(len(registered_users), str(context.message.author))
        users_info[str(context.message.author)] = {"exp": 0, "coins": 0, "lvl": 1}
        await client.say("Registering User " + str(context.message.author) + " ...")
        author_username = str(context.message.author)
        username_length = len(author_username) - 5
        embed = discord.Embed(title="__ %s __'s Profile" % (str(author_username[0:username_length])), description="**Current Level: 1** \n" + \
                              "Experience Points: 0/50 \n" + \
                              "Current Amounts of Shruggy Coins: 0 ", color=discord.Color.green())
        embed.set_thumbnail(url=context.message.author.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def seelist(context):
    await client.say(registered_users)
    await client.say(users_info)

#Check for bot's reaction speed ------------------------------------------------------------------------------------
@client.command(name="Ping!",
                description="Check how fast this bot react to your message!",
                brief="Get Reaction Speed",
                aliases=["latency", "react_speed", "reactspeed", "ping"],
                pass_context=True)
async def ping(context):
    possible_responses = [
        "What's up?",
        "Need any help?",
        "Got slow reaction speed?",
        "I am this server's assistant bot!",
        "Exclusive bot only on this server!",
        "Written in async, unable to get bot latency!",
        "What do you want?",
        "This bot is created by user Blue Bird !",
        "Welcome to the Shrug server!",
        "Help you on your demand!",
        "Bot made for helping people in this server!",
        "Try to find the easter egg on this bot???"]
    possible_helps = [
        "Type ``s!help`` if you are new to this server!",
        "Type ``s!serverinfo`` if you are curious to see this server's basic informations!",
        "Type ``s!8ball`` with a yes/no question after it to get a answer from the future!",
        "Type ``s!help`` if you are unfamiliar with this server!",
        "This server is created by user Blue Bird ! Direct Messaging him for help!",
        "This bot is made by user Blue Bird ! Direct Messaging him if you found some errors on this bot!",
        "Please give user Blue Bird feedbacks of your opinion about this server AND the bot!"]
    if str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(1, 3)
    max_exp = users_info[str(context.message.author)]["lvl"] * 50
    if users_info[str(context.message.author)]["exp"] > max_exp - 1 :
        math.floor(float(users_info[str(context.message.author)]["exp"])) == math.floor(float(users_info[str(context.message.author)]["exp"])) - max_exp
        users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
        await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    if random.randint(1,2) == 1:
        await client.say(context.message.author.mention + " Pong ! " + random.choice(possible_responses))
    else:
        await client.say(context.message.author.mention + " Pong ! " + random.choice(possible_helps))

#Troll commands (spawn a arceus, show mega bidoof's info and bal) ------------------------------------------------
@client.command(aliases=["troll"])
async def pokecord_troll():
    possible_trolls = ["https://www.pokecord.com/assets/CLMXnAHoJBHz.png",
                       'https://www.pokecord.com/assets/cZwtyzSpoTGK.png',
                       "https://www.pokecord.com/assets/lUUbmdNYWQGe.png",
                       "https://www.pokecord.com/assets/tsHyEzrFRvvf.png",
                       "https://www.pokecord.com/assets/qwZjNWcRpYeL.png",
                       "https://www.pokecord.com/assets/zLjZxfPivZxG.png",
                       "https://www.pokecord.com/assets/EyrnISUymuXj.png",
                       "https://www.pokecord.com/assets/KFBEarCORUNx.png",
                       "https://www.pokecord.com/assets/NKcRJRyzXtCs.png",
                       "https://www.pokecord.com/assets/FYRxKEoKrDsn.png",
                       "https://www.pokecord.com/assets/gmypxntMuvAg.png",
                       "https://www.pokecord.com/assets/cUlaoIUTYzze.png",
                       "https://www.pokecord.com/assets/iqIDyvqbxkSK.png",
                       "https://www.pokecord.com/assets/swDzioNyoHsd.png",
                       "https://www.pokecord.com/assets/OhHdWsAIonRP.png",
                       "https://www.pokecord.com/assets/qYyBjmtLqNJb.png",
                       "https://www.pokecord.com/assets/XAHqDsmsnYPy.png"]
    e = discord.Embed(title="‌‌A wiId pokémon has appeared!", description="Guess the pokémon and type p!catch <pokémon> to catch it!", color=discord.Color.green())
    e.set_image(url=random.choice(possible_trolls))
    await client.say(embed=e)

@client.command(aliases=["trolll"],
                pass_context=True)
async def pokecord_troll3(context):
    if str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(100, 300)
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        if users_info[str(context.message.author)]["exp"] > max_exp - 1:
            users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] - max_exp
            users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
            await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    e = discord.Embed(title="‌‌A wiId pokémon has appeared!", description="Guess the pokémon and type p!catch <pokémon> to catch it!", color=discord.Color.green())
    e.set_image(url='https://www.pokecord.com/assets/CsaaadfuOlUD.png')
    e.set_footer(text="It's Blue Bird !!! (Easter Egg)")
    await client.say(embed=e)

@client.command(pass_context=True)
async def catch(context):
    await client.say("Congratulations " + context.message.author.mention + "! You caught a level 0 Missngno!")

@client.command(pass_context=True,
                aliases=["congrats", "congrat", "congratulations", "congratulation"])
async def level_up_congrats(context):
    author_username = str(context.message.author)
    username_length = len(author_username) - 5
    await client.say("```Congratulations %s! Your Pokemon is now level 101!```" % (str(author_username[0:username_length])))

@client.command(aliases=["megabidoof"],
                pass_context=True)
async def pokecord_troll2(context):
    embed = discord.Embed(title=" ", color=discord.Color.green())
    embed.set_thumbnail(url=context.message.author.avatar_url)
    embed.set_author(icon_url="https://images-ext-2.discordapp.net/external/oMthNLlPT-Sjg-4nanyqxHDBH4iE7N8CVUh0WFjlxAc/https/i.imgur.com/8ZpM4tb.jpg", name="Professor Oak")
    embed.add_field(name="Level 100 Mega Bidoof", value="**Max Level** \n" + \
                      "**Nature:** Overpowered \n" + \
                      "**HP:** 1000 - IV: 31/31 \n" + \
                      "**Attack:** 1000 - IV: 31/31 \n" + \
                      "**Defense:** 1000 - IV: 31/31 \n" + \
                      "**Sp.Atk:** 1000 - IV: 31/31 \n" + \
                      "**Sp.Def:** 1000 - IV: 31/31 \n" + \
                      "**Speed:** 1000 - IV: 31/31 \n")
    embed.set_image(url='https://cdn.discordapp.com/attachments/443635040690110484/450112010357702668/Untitled379.png')
    embed.set_footer(text="Selected Pokémon: 9001/9001 - Use p!back and p!next to cycle through your pokémon!")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def bal(context):
    author_username = str(context.message.author)
    username_length = len(author_username) - 5
    embed = discord.Embed(title="%s's balance:" % (str(author_username[0:username_length])), description="You currently have 99999999 credits.", color=discord.Color.green())
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/JX4qP7iKLob3oEE-wYIT_VQLyVBMyWB3v901Dys1a94/https/images-ext-2.discordapp.net/external/xlEcYc2ErW6-vD7-nHbk3pv2u4sNwjDVx3jFEL6w9fc/https/emojipedia-us.s3.amazonaws.com/thumbs/120/emoji-one/104/money-bag_1f4b0.png?width=108&height=108")
    await client.say(embed=embed)

@client.command()
async def market():
    embed = discord.Embed(title=" ", color=discord.Color.green())
    embed.add_field(name="Pokécord Market:", value="**Level 101 Mega Bidoof** | ID: 12345678 | Price: 799999 Credits")
    embed.set_footer(text="Showing 1-1 of 1 pokémon matching this search.")
    await client.say(embed=embed)
#test ----------------------------------------------------------------------------------------------------------------
@client.command()
async def test(number=None):
    data_base1.insert(len(data_base1), number)
    await client.say(str(data_base1))

#flip/roll a coin/dice -----------------------------------------------------------------------------------------------
@client.command(pass_context=True)
async def flip(context):
    if random.randint(1,10) == 1:
        if str(context.message.author) in registered_users:
            users_info[str(context.message.author)]["coins"] = users_info[str(context.message.author)]["coins"] + 1
    elif str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(1, 3)
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        if users_info[str(context.message.author)]["exp"] > max_exp - 1:
            users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] - max_exp
            users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
            await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    if random.randint(1,2) == 1:
        await client.say(context.message.author.mention + " just flipped a coin and got heads !")
    else:
        await client.say(context.message.author.mention + " just flipped a coin and got tails !")

@client.command(pass_context=True)
async def roll(context):
    if str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(1, 3)
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        if users_info[str(context.message.author)]["exp"] > max_exp - 1:
            users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] - max_exp
            users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
            await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    dice_number = random.randint(1,6)
    await client.say(context.message.author.mention + " just rolled a dice and got %s ! " % (dice_number))
    

#8balls --------------------------------------------------------------------------------------------------------------
@client.command(name="8ball",
                description="Answers a yes/no question.",
                brief="Answers from the beyond",
                aliases=["eight_ball", "eightball"],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        "That is a no",
        "It is not looking likely",
        "It's too hard to tell",
        "It is quite possible",
        "Definitely",
        "Too unpredictable, try again",
        "Let's see... wait, I forgot the answer that I was about to tell you",
        "I am just a bot, go flip a coin yourself, I am too lazy to answer that",
        "Go follow what you believed in",
        "Definitely No, truth are always more painful than lies",
        "Yes, duh! What else do you expect",
        "Well... maybe",
        "Of course it is a yes"
    ]
    if str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(1, 3)
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        if users_info[str(context.message.author)]["exp"] > max_exp - 1:
            users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] - max_exp
            users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
            await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


#Bot's basic stats ----------------------------------------------------------------------------------------------------
@client.command(name="ServerStats",
                aliases=["server_info", "server_stats", "serverinfo", "serverstats"],
                description="Check the basic information about this server",
                brief="Server's basic stats",
                pass_context=True)
async def application_info(context):
    total_members = str(sum(1 for x in client.get_all_members()) - len([m.id for m in client.get_all_members() if m.bot]))
    total_bots = str(len([m.id for m in client.get_all_members() if m.bot]))
    total_online = str(len({m.id for m in client.get_all_members() if m.status is not discord.Status.offline}))
    total_servers = str(len(client.servers))
    embed = discord.Embed(title="__Shrug's Server LIVE Stats__ : ", color = discord.Color.green())
    embed.add_field(name="Current Users in this server: ", value=str(total_members) + " users", inline=False)
    embed.add_field(name="Current Bots in this server: ", value=str(total_bots) + " bots", inline=False)
    embed.add_field(name="Current Online Users in this server: ", value=str(total_online) + " users", inline=False)
    embed.add_field(name="Amount of space of this bot: ", value="35 KB", inline=False)
    embed.set_footer(text="Both this server and this bot are created by user Blue Bird#8805 !")
    await client.say(embed=embed)
#All commands listed ----------------------------------------------------------------------------------------------------
@client.command(description="Listing all the commands this bot can do!",
                brief="Listing all the commands",
                aliases=["commands", "all_commands", "allcommands"],
                pass_context=True)
async def list_commands(context):
    if str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(1, 3)
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        if users_info[str(context.message.author)]["exp"] > max_exp - 1:
            users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] - max_exp
            users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
            await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    embed = discord.Embed(title="__All the commands__ : ", description="Where all the commands this bot can do are listed here !", color= discord.Color.green())
    embed.add_field(name=" ``s!ping`` -- basic command", value="Aliases : ``latency``, ``react_speed``, ``reactspeed``, ``ping``. \n" + \
                    "Uses : You cannot get latency numbers from this command because I did not wrote this bot in rewrite version of python. You will ususally get a different reply each time!")
    embed.add_field(name=" ``s!help`` -- basic command", value="Aliases : ``s!help``. \n" + \
                    "Uses : Get a better understanding of this server!")
    embed.add_field(name=" ``s!server_info`` -- basic command", value="Aliases : ``s!server_info``, ``s!serverinfo``, ``s!server_stats``, ``s!serverstats``. \n" + \
                    "Uses : See the basic LIVE stats of this server!")
    embed.add_field(name=" ``s!commands`` -- basic command", value="Aliases : ``commands``, ``all_commands``, ``allcommands``. \n" + \
                    "Uses : You are using this command right now! Check all the commands this bot have!")
    embed.add_field(name=" ``s!8ball`` -- fun command", value="Aliases : ``8ball``, ``eight_ball``, ``eight_ball``. \n" + \
                    'Uses : Put a yes/no question after the command and you will get a answer from the "future" ! 10 possible replies !')
    embed.add_field(name=" ``s!warn`` -- fun command", value="Aliases : ``s!warn``, ``s!warns``. \n" + \
                    "Uses : DON'T take it seriously, meant to make people laugh! You can get different warn message almost each time!")
    embed.add_field(name=" ``s!flip`` & ``s!roll`` -- fun commands", value="Aliases : ``s!flip``, ``s!roll``. \n" + \
                    "Uses : ``s!flip`` will flip a coin for you (two different results), ``s!roll`` will roll a dice for you (six different results) !")
    await client.say(embed=embed)
    
#bot's Server's helping page ---------------------------------------------------------------------------------------------
@client.command(description="List all the commands and description",
                brief="Just a help command",
                pass_context=True)
async def help(context, number=None):
    if str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(1, 3)
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        if users_info[str(context.message.author)]["exp"] > max_exp - 1:
            users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] - max_exp
            users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
            await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    try:
        number = math.floor(float(number))
    except:
        if number is not None:
            await client.say(context.message.author.mention + " ! You can only type numbers as inputs! For the command ``s!help`` !")
        elif number is None:
            number = 1
    number = math.floor(float(number))
    if number == 1:
        embed = discord.Embed(title="__Server Helping Page 1__ ( Table of contents ) : ", color = discord.Color.green())
        embed.add_field(name=" Table of contents", value="You are reading this page right now ! ")
        embed.add_field(name=" Questions", value="Go to page 2 by typing ``s!help 2`` !")
        embed.add_field(name=" **Basic** Roles", value="Go to page 3 by typing ``s!help 3`` !")
        embed.add_field(name=" **Special** Roles", value="Go to page 4 by typing ``s!help 4`` !")
        embed.add_field(name=" **Exclusive** Roles", value="Go to page 5 by typing ``s!help 5`` !")
        embed.add_field(name=" **News** Category", value="Go to page 6 by typing ``s!help 6`` !")
        embed.add_field(name=" **Chat** Category", value="Go to page 7 by typing ``s!help 7`` !")
        embed.add_field(name=" **Bots Section** Category", value="Go to page 8 by typing ``s!help 8`` !")
        embed.add_field(name="  **Games Section** Category", value="Go to page 9 by typing ``s!help 9`` !")
        embed.add_field(name=" **Homework Solver** Category",value="Go to page 10 by typing ``s!help 10`` !")
        embed.add_field(name=" **SECRET Section** Category", value="Go to page 11 by typing ``s!help 11`` !")
        embed.add_field(name=" OTHER COMMANDS you can use", value="Type ``s!commands `` to see a list of cool commands this bot can do beside ``s!help`` !", inline=False)
        await client.say(embed=embed)
    elif number == 2:
        embed = discord.Embed(title="__Server Helping Page 2__ ( Questions ) : ", color=discord.Color.green())
        embed.add_field(name="Who is the creator of this server? ", value="It is <@!344292024486330371> .", inline=False)
        embed.add_field(name="Who made this bot? ", value="It is also created by <@!344292024486330371> !", inline=False)
        embed.add_field(name="What is this bot made for? ", value="Made this bot so hopefully people who are new to this server can get their questions solved even when admins are not online.", inline=False)
        embed.add_field(name="Why you name this server as ``shrug`` ?", value="I think I just named it shrug because I like to use that shrug emoticons alot.", inline=False)
        embed.add_field(name="What if I still have questions that this bot cannot solve yet?", value="Just Direct Messaging <@!344292024486330371> , when he got online he will probably able to solve it.", inline=False)
        await client.say(embed=embed)
    elif number == 3:
        embed = discord.Embed(title="__Server Helping Page 3__ ( Basic Roles ) : ", color = discord.Color.green())
        embed.add_field(name=" Visitors: ", value="Unable to do anything except instant invite, view history, allowed to be mentioned and leave the chat.", inline=False)
        embed.add_field(name=" Members: ", value="Able to type messages, speak, enable links, instant invite, view history, allow to post files, able to add reactions, allowed to be mentioned, view audit log and leave the chat.", inline=False)
        embed.add_field(name=" Officers: ", value="Have the same power as a member but also able to kick members, nickname him/her self, able to nickname other people as well.", inline=False)
        embed.add_field(name=" Managers: ", value="Have the same power as a officer but also able to mention everyone, ban members, mute/deafen members, delete messages as well.", inline=False)
        embed.add_field(name=" Directors: ", value="Have the same power as the General except they does not have the permissions of administration, manage the server, manage roles and manage channels.", inline=False)
        embed.add_field(name=" General: ", value="Notta admin")
        await client.say(embed=embed)
    elif number == 4:
        embed = discord.Embed(title="__Server Helping Page 4__ ( Special Roles ) : ", color=discord.Color.green())
        embed.add_field(name=" Poll Makers: ", value="(Unlocked by solving more than 10 questions on the HomeWorks Solver Category) \n" + \
                        "Able to make polls on <#443635040690110484> !", inline=False)
        embed.add_field(name=" Elders: ", value="(Unlocked by being active in this server for more than 3 weeks) \n" + \
                        "ABLE to text in a SECRET HIDDEN category!", inline=False)
        embed.add_field(name=" VIPs: ", value="(Unlocked by being active in this server for more than 2 months) \n" + \
                        "Able to text AND edit in a SECRET HIDDEN category!", inline=False)
        embed.add_field(name=" Advisors: ", value="(Unlocked by post least 10 reasonable suggestions on the <#442794963458326540> ) \n" + \
                        "Able to text in the <#446106943635849217> !", inline=False)
        embed.add_field(name=" Giveaways: ", value="(Unlocked when the General feels like it) \n" + \
                        "Able to make giveaways on the <#451528400201449472> !", inline=False)
        embed.add_field(name=" Participants: ", value="(Unlocked by do the pinged polls) \n" + \
                        "Able to get pinged when a event came!", inline=False)
        await client.say(embed=embed)
    elif number == 5:
        embed = discord.Embed(title="__Server Helping Page 5__ ( EXCLUSIVE Roles ) : ", color=discord.Color.green())
        embed.add_field(name=" Top Twenty", value="Only the first twenty people who joined this server are able to get it.")
        await client.say(embed=embed)
    elif number == 6:
        embed = discord.Embed(title="__Server Helping Page 6__ ( News Category )", color=discord.Color.green())
        embed.add_field(name="Basic Information Channel : ", value="If you are too lazy to use these ``s!help`` commands, you can also check out the roles description there!", inline=False)
        embed.add_field(name="Polls Channel ; ", value="Where you can vote, and check out the updates that might added in the future for this server!", inline=False)
        embed.add_field(name="Updates Channel : ", value="Where <@!344292024486330371> post the latest updates to this server!", inline=False)
        embed.add_field(name="Advertisements Channel : ", value="Where you can join other servers, and see ads if you are interested.", inline=False)
        embed.add_field(name="Giveaways Channel : ", value="Where people want go crazy and giveaway free stuffs XD.", inline=False)
        await client.say(embed=embed)
    elif number == 7:
        embed = discord.Embed(title="__Server Helping Page 7__ ( Chat Category ) : ", color=discord.Color.green())
        embed.add_field(name="Random Stuff Channel : ", value="Where you can talk any topic, see who joined/left the server, and the dyno bot's log.", inline=False)
        embed.add_field(name="Suggestions For Server Channel : ", value="Where you can suggest some new updates that can be added to this server or some flaws in this server that you wanted admins to fix.", inline=False)
        embed.add_field(name="Guess Codes Channel : ", value="Where you can get good prize from breaking the code set by admins, you can also take extra hints as well!", inline=False)
        await client.say(embed=embed)
    elif number == 8:
        embed = discord.Embed(title="__Server Helping Page 8__ ( Bots Section Category ) : ", color=discord.Color.green())
        embed.add_field(name="Shruggy Bot Testing Channel : ", value="A channel where <@!344292024486330371> test the new commands or to see if this shruggy is bot is functional!", inline=False)
        embed.add_field(name="Pokemon Spam Channel One : ", value="A channel for getting some quick xp for your pokemons by spamming!", inline=False)
        embed.add_field(name="Pokemon Spam Channel Two : ", value="Function basicly the as the <#443208134920634368> , this channel was made because you don't want a channel to be way spammy!", inline=False)
        embed.add_field(name="Pokemon Trading & Dueling Channel : ", value="A channel for you to trade and dueling pokemons with other players!", inline=False)
        embed.add_field(name="Dank Memer Bo Channel : ", value="A channel for you to spam dank memer bot's commands !", inline=False)
        embed.add_field(name="BotBot Bot Channel : ", value="A channel for you to play the BoxBot bot and their commands !", inline=False)
        embed.add_field(name="Coinmaster Bot Channel : ", value="A channel where you can earn coins with coinsmaster bot !", inline=False)
        await client.say(embed=embed)
    elif number == 9:
        embed = discord.Embed(title="__Server Helping Page 9__ ( Games Section Category ) : ", color=discord.Color.green())
        embed.add_field(name="Minecraft Channel : ", value="A channel for minecraft fans to talk about their game experiences about minecraft !", inline=False)
        embed.add_field(name="Battle Royale Games Channel : ", value="A channel where you can talk about Fortnite, PUBG and other battle royale games !", inline=False)
        embed.add_field(name="Supercell Games : ", value="A channel where you can talk about supercell's games, like Clash Royale, Clash of clan, Boom Beach etc... !", inline=False)
        await client.say(embed=embed)
    elif number == 10:
        embed = discord.Embed(title="__Server Helping Page 10__ ( Homework Solver Category ) : ", color=discord.Color.green())
        embed.add_field(name="Math Channel : ", value="A channel where you can post/share/answer math questions, like algebra, geometry and trigonometry! Not yet answered questions will be pinged!", inline=False)
        embed.add_field(name="English Channel : ", value="A channel where you can post/share/answer questions that is related to English, like essays, and vocabs ! Unanswered questions will be pinged !", inline=False)
        embed.add_field(name="Other Subjects Channel : ", value="A channel where you can post/share/answer questions that is about other topics beside math and English, like programming, arts, and science ! Unanswered questions will be pinged !", inline=False)
        await client.say(embed=embed)
    elif number == 11:
        title = discord.Embed(title="__Server Helping Page 11__ ( SERCRET Section Category ) : ", description="Hey ! What are you Looking at ? \n" + \
                              "You can't check this page if you do not have a Elder or a VIP role yet!", color=discord.Color.green())
        await client.say(embed=title)
    elif number < 1:
        await client.say("Hey " + context.message.author.mention + " ! You can't put a number less than 1 as input for ``s!help`` command yet !")
    elif number > 1:
        await client.say("Hey " + context.message.author.mention + " ! You can't put a number greater than 11 as input for ``s!help`` command yet !")

#get some jokes -----------------------------------------------------------------------------------------------------------
@client.command(aliases=["warn", "warns"],
                pass_context=True)
async def get_a_joke(context):
    if str(context.message.author) in registered_users:
        users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] + random.randint(1, 3)
        max_exp = users_info[str(context.message.author)]["lvl"] * 50
        if users_info[str(context.message.author)]["exp"] > max_exp - 1:
            users_info[str(context.message.author)]["exp"] = users_info[str(context.message.author)]["exp"] - max_exp
            users_info[str(context.message.author)]["lvl"] = users_info[str(context.message.author)]["lvl"] + 1
            await client.say("Congratulations " + context.message.author.mention + "! You are now Level " + str(users_info[str(context.message.author)]["lvl"]) + " !")
    if random.randint(1,10) == 1:
        embed = discord.Embed(title="Real Life Experience by someone (Half serious Half jokes)", description="NEVER take these warns so seriously!", color=discord.Color.green())
        await client.say(embed=embed)
    elif random.randint(1,10) == 1:
        embed = discord.Embed(title="Real Life Experience by someone (All serious)", description="Never playing these cool commands without invite your friends to this server! Type ``shrug`` to get a server link invite !", color=discord.Color.green())
        await client.say(embed=embed)
    else:
        possible_jokes = ["Never spending hours typing codes for your bot and forgot to save the file.",
                          "Never turn in your homework when you forgot to write your names on them.",
                          "Never forget to use something to cover your phone from teacher's sight when you are playing it during class period.",
                          "Never ride a bike in the forest without brakes on.",
                          "Never expect that you can actually slap a fly with a fly swatter full of holes",
                          "Never step on some banana peels near a swimming pool when you are only wearing a normal set of shirts, pants, and shoes.",
                          "Never believe in sweet lies than ugly truths, especially when you trying to see if you have enough money to buy something like a car.",
                          "Never say never!",
                          "Never fall to the opposite direction from your friends when you are doing a trust fall with them.",
                          "Never even try to find out how Gods pray.",
                          "Never read this message! Ha, I made you read it!"]
        embed = discord.Embed(title="Real Life Experience by Someone (Half serious Half jokes)", description=random.choice(possible_jokes), color=discord.Color.green())
        await client.say(embed=embed)
        if 1 == 2:
            await client.say(len(possible_jokes))
        
#if online ------------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():
    print("Bot is online!")
    for messages in client.messages:
        print(messages)

#end ========================================================================================================================================================

client.run("TOKEN")
