# This is the code for the Discord bot on my server, The Potato Kingdom.
# Requirements (pip install):
# discord.py, python-dotenv
# Also create a file called "token.txt" in the same directory as this file to run it using your own token
# (use the Discord developer portal to generate the token)
# And a file called "welcome.txt" which has the ID for the welcome channel in your test server (e.g. 724810199180771358)
# (turn on developer mode in settings, right click your #welcome channel and select Copy ID)

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import random

load_dotenv()

f = open('token.txt', 'r')
token_thing = f.read()
f.close()
TOKEN = token_thing

bot = commands.Bot(command_prefix="!", intents=discord.Intents().all())

f = open('welcome.txt', 'r')
WELCOME_CHANNEL = f.read()
f.close()


def check_channel(ctx):
    if ctx.channel.name == "bot-commands" or ctx.channel.name == "spam":
        return True
    else:
        return False

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! Yeet')
    await bot.change_presence(activity=discord.Game('return to potato'))

@bot.command(
    help="Uses some crazy logic to determine if pong is actually the correct value or not.",
    brief="Prints pong back to the channel."
)
async def ping(ctx):
	await ctx.channel.send("Pong!")

@bot.command(
    help="Eat it",
    brief="Eat it"
)
async def potato(ctx):
	stuff = ["You ate a potato! :potato:",
			"You ate a sweet potato! :sweet_potato:",
			"You ate a potato with a fork! :potato: :fork_and_knife:",
			"You ate a potato with a spoon! :potato: :spoon:",
			"You ate a baked potato!",
			"You ate a hot potato! :fire: :potato:",
			"You ate a :sparkles: GOLDEN POTATO :sparkles:. Wow you got lucky"]

	thing = random.choice(stuff)

	if thing == "You ate a baked potato!":
		bruh = bot.get_emoji(764554710178201611)
		
		await ctx.channel.send(f"You ate a baked potato! {bruh}")
	else:
		await ctx.channel.send(random.choice(stuff))

@bot.command(
    help="Don't eat it",
    brief="Don't eat it",
)
async def banana(ctx):
    await ctx.channel.send("You ate a baked banana! :fire: :banana: Ew, that tasted disgusting.")

@bot.command(
    help="Eat it",
    brief="Eat it"
)
async def hotfood(ctx):
    await ctx.channel.send("Hot Food. We sit down to eat, and the potato's a bit hot. So I only put a little bit on my fork and I blow. *puff-puff* 'Til it's cool. Just cool. Then into the mouth. *hawlp* *click* Noice. And there's my brother, he's doing the same. *puff-puff* 'Til it's cool. Just cool. Into the mouth. *hawlp* *click* Noice! There's my mum, she's doing the same. *puff puff* 'Til it's cool. Just cool. Into the mouth. *hawlp* *click* Noice! But my dad. My dad, what does he do? He stuffs a great big chunk of potato into his mouth and then that really does it. His eyes pop out. He flaps his hands. He blows, he puffs, he yells, he bobs his head up and down. He spits bits of potato all over his plate and he turns to us and he goes, \"Watch out, everybody! The potato's really hot!\"")

@bot.command(
    help="The worse version of hot food",
    brief="The worse version of hot food"
)
async def friedfood(ctx):
    await ctx.channel.send("We sit down to YEET :joy::100: and the potato's :potato: a bit HOT :fire::joy::rofl::skull:, so I only put a little bit :pinching_hand: on my fork :fork_and_knife: and I blow :cloud: puff :loud_sound: puff :wind_blowing_face:, 'til it's cool :sunglasses:, just cool :cool:, into the mouth :lips: *hawlp* :astonished: *click* :point_up_2: NOICE :ok_hand::joy::rofl::thinking::grin:. And there's my brother :boy:, he's doing the same :potato: :cloud: puff :loud_sound: puff :wind_blowing_face:, 'til it's cool :snowflake:, just cool :ice_cube:, into the mouth :lips:, *hawlp* :astonished: *click* :point_up_2: NOICE :ok_hand::joy::rofl::thinking::grin:. There's my mum :woman:, she's doing the same :potato:, 'til it's cool :gem:, just cool :v:, into the mouth :lips: *hawlp* :astonished: *click* :point_up_2: NOICE :ok_hand::joy::rofl::thinking::grin:. But my dad :man:, my dad, what does he do? He stuffs :stuffed_flatbread: a great :grin: :b:ig chunk :poop: of potato :sweet_potato::potato: into his mouth :lips: and that really does it :boom:. His eyes :eyes: pop :balloon: out :outbox_tray:. He flaps :door: his hands :raised_hand::raised_back_of_hand:. He blows :wind_blowing_face: he puffs :cloud: he yells :loudspeaker: he bobs his head :skull: up :chart_with_upwards_trend: and down :chart_with_downwards_trend:. He spits :wind_blowing_face: bits :pinching_hand: of potato :potato: all over his plate :fork_knife_plate: and he turns :point_left: to us :flag_us: and he goes :goal:, \"Watch out :outbox_tray: everybody! The potato's :potato: really :boom: HOT! :fire::rocket::sparkles::rofl::joy:\"")

@bot.command(
    help="The worse version of hot food",
    brief="The worse version of hot food"
)
async def coldfood(ctx):
    await ctx.channel.send("Cold Food. We sit down to _BRRRRRRRRRR_ **AHHHH IT'S SO COLD** __HELPP!!!!!!!!!!!__ :cold_face::cold_sweat::ice_cube::snowflake::gem:")

@bot.command(
    help="LOL i'm so random!!!1",
    brief="Prints a random number",
    name="randomnumber"
)
async def lolrandom(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send(random.randint(0, 10))
    elif len(args) == 1:
        await ctx.channel.send(random.randint(0, int(args[0])))
    else:
        await ctx.channel.send(random.randint(int(args[0]), int(args[1])))

@bot.command(
    help="Displays approximately how long ago Bongs uploaded his latest video",
    brief="Displays approximately how long ago Bongs uploaded his latest video",
    name="whenlastvideo",
    aliases=["whenlatestvideo", "whenlastvid", "whenlatestvid"]
)
async def asdfjklasdfjkl(ctx):
    y = random.randint(100, 10000000)

    await ctx.channel.send("Bongs uploaded his latest video **" + str(f'{y:,}') + "** years ago :cry:")

@bot.command(
    help="hi",
    brief="Displays Minecraft player heads",
    name="head"
)
async def playerhead(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send("Usage: !head <player name>")
    elif len(args[0]) > 20:
        await ctx.channel.send("**:x: Username is too long!**")
    elif len(args[0]) < 3:
        await ctx.channel.send("**:x: Username is too short!**")
    else:
        await ctx.channel.send("https://minotar.net/helm/" + str(args[0]) + "/128")

@bot.command(
    help="Get free candy!!!!1",
    brief="Get free candy!!!!1",
)
async def freecandy(ctx):
    await ctx.channel.send("Nope.")
    await ctx.channel.send("https://media1.giphy.com/media/Ju7l5y9osyymQ/200.gif")

@bot.command(
    help="Do some quick maffs(TM)",
    brief="Do some quick maffs(TM)",
    name="1+1"
)
async def quickmath(ctx):
    numberthing = random.randint(0, 10)
    
    if numberthing == 2:
        if random.randint(0, 1) == 0:
            await ctx.channel.send("Uhhhh... it's... sorry, I'm too busy programming the potato and eating the computer.")
        else:
            await ctx.channel.send("Uhhhh... it's... sorry, I'm too busy cleaning the lawn and mowing my room.")
    else:
        await ctx.channel.send(str(numberthing))

'''
@bot.command(
    help="dont say no no words",
    brief="don't say no no words",
    name="language",
    aliases=['l'],
)
async def lllll(ctx):
    asdfjkl = random.randint(0, 2)

    if asdfjkl == 0:
        await ctx.channel.send("LANGUAGE")
    elif asdfjkl == 1:
        await ctx.channel.send("**LANGUAGE**")
    else:
        await ctx.channel.send(
'''

@bot.command(
    help="Da ba dee, da ba die!!!",
    brief="Generates random misheard lyrics for the song I'm Blue"
)
async def imblue(ctx):
    first_words = [
	{
		"word":"dee",
		"p":"n"
	},
	{
		"word":"bleed",
		"p":"v"
	},
	{
		"word":"green",
		"p":"a"
	},
	{
		"word":"beat",
		"p":"v"
	},
	{
		"word":"need",
		"p":"v"
	},
	{
		"word":"yeet",
		"p":"v"
	},
	{
		"word":"meme",
		"p":"n"
	},
	{
		"word":"geek",
		"p":"n"
	},
	{
		"word":"dream",
		"p":"n"
	},
	{
		"word":"eat",
		"p":"v"
	},
	{
		"word":"heat",
		"p":"v"
	},
	{
		"word":"pee",
		"p":"v"
	},
	{
		"word":"tree",
		"p":"n"
	},
	{
		"word":"believe",
		"p":"v",
		"twoSyllables":True
	},
	{
		"word":"diseased",
		"p":"n",
		"twoSyllables":True
	},
	{
		"word":"deceased",
		"p":"n",
		"twoSyllables":True
	},
	{
		"word":"indeed",
		"p":"n",
		"twoSyllables":True
	}
    ]

    second_words = [
	{
		"word":"dye",
		"p":"n"
	},
	{
		"word":"die",
		"p":"v"
	},
	{
		"word":"guy",
		"p":"n"
	},
	{
		"word":"fly",
		"p":"v"
	},
	{
		"word":"pie",
		"p":"n"
	},
	{
		"word":"mine",
		"p":"n"
	},
	{
		"word":"guy",
		"p":"n"
	},
	{
		"word":"diet",
		"p":"n"
	},
	{
		"word":"diamond",
		"p":"n"
	},
	{
		"word":"lie",
		"p":"n"
	},
	{
		"word":"dime",
		"p":"n"
	},
	{
		"word":"why",
		"p":"all"
	},
        {
		"word":"guide",
		"p":"n"
	}
    ]

    stuff = {
	"n":[
		"I'm a",
		"up a",
		"apple",
		"I'm in",
		"on a"
	],
	"v":[
		"I will",
		"I would",
		"I can",
		"I could",
		"I will",
		"imma",
		"I must"
	],
	"a":[
		"I am"
	],
	"all":[
		"da ba",
		"cobble"
	]
    }

    lyric = ""

    first = random.choice(first_words)
    first_phrase = ""

    second = random.choice(second_words)
    second_phrase = ""

    if "twoSyllables" in first:
        if first["p"] == "n":
            first_phrase = "I'm"
        else:
            first_phrase = "I"
    else:
        first_phrase = random.choice(stuff[first["p"]])
        if random.random() <= 0.1:
            first_phrase = random.choice(stuff["all"])

    second_phrase = random.choice(stuff[second["p"]])
    if random.random() <= 0.1:
        second_phrase = random.choice(stuff["all"])
    
    lyric = first_phrase.capitalize() + " " + first["word"] + " " + second_phrase + " " + second["word"]
    
    await ctx.channel.send(lyric)

@bot.event
async def on_member_join(member):
    await bot.get_channel(WELCOME_CHANNEL).send(f"**Hey {member.mention}, welcome to Bongs237's server!**\nHere's a free potato: :potato:" + test_msg)

@bot.event
async def on_message(message):
    if message.content.lower() == "i like potatoes" or message.content.lower() == "i like potatos" or message.content.lower() == "i love potatoes" or message.content.lower() == "i love potatos":
        await message.channel.send("Same!")

    # INCLUDES THE COMMANDS FOR THE BOTS. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)

bot.run(TOKEN)

