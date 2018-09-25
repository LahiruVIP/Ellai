import discord
from discord.ext import commands
from discord.ext.commands import Bot
import builtins
import asyncio
import time
import aiohttp
import traceback
import chalk
import functools
import inspect
import random
import rule34
from osuapi import OsuApi, AHConnector
import youtube_dl


bot = commands.Bot(command_prefix='ç!')
client = commands.Bot(command_prefix='ç!')
bot.remove_command("help")
builtins.bot = bot
print (discord.__version__)

api = OsuApi("12658bf60124fec4e2817e552b6b7ec559120954", connector=AHConnector())


def __init__(self):
    self.bot = discord.Client(bot)

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name='listening to you', type=3), status=None, afk=False)
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name='ç!help', type=3), status=None, afk=False)
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name='Currently on ' + str(len(bot.guilds)) +
                                                          ' servers', type=3), status=None, afk=False)
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.loop.create_task(status_task())

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(":ping_pong: ping!! xSSS")


@bot.command()
async def everyone(ctx):
    embed = discord.Embed()
    embed.set_image(url='https://media.giphy.com/media/L0NBKBQNnx9x1hcrQy/giphy.gif')
    await ctx.send(embed=embed)
    



@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def roll(ctx, a:int, b: int):
    await ctx.send(random.randint(a,b))

@bot.command()
async def ratewaifu(ctx):
    args = ctx.message.content.split(" ")
    await ctx.send(' {0} gets a {1} /100 from me' .format(" ".join(args[1:]), random.randint(0,100)))

@bot.command()
async def lovemeter(ctx):
    await ctx.send('<@{0}> and <@{1}> are {2}% in love with each other.'\
                   .format(ctx.message.mentions[0].id, ctx.message.mentions[1].id, random.randint(0,100)))


@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
@commands.has_role('Lahiru-VIP')
async def somelove(ctx):
        if ctx.author.id == 194450452950024192 :
            await ctx.send('I love you senpai')
        else:
            await ctx.send('I love you <@{0}>'\
                                   .format(ctx.message.author.id))
            print(ctx.message.author.id)

@bot.command()
async def owner(ctx):
    myid = '<@194450452950024192>'
    await ctx.send(' %s is the best bot owner ' %myid)


@bot.command()
async def darling(ctx):
    authorid = '<@{0}>'.format(ctx.author.id)
    await ctx.send(" {} you are my darling ^w^" .format(authorid))


@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Ellia", description="Ellai stands for: Effective Little Loli Artificial Intelligence", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<LahiruVIP#8485>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=443478651485421598&permissions=8&scope=bot)")

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.guild.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server info")
    embed.add_field(name="Name", value=ctx.message.guild.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.guild.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.guild.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.guild.members))
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title="{}'s info".format(member.display_name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=member.display_name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Highest role", value=member.top_role)
    embed.add_field(name="Joined", value=member.joined_at)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title='bot commands', description="Here are all my commands", color=0x66ff23)
    embed.add_field(name='ç!ratewaifu', value='bot rates your waifu')
    await ctx.send('check your direct messages')
    await ctx.author.send(embed=embed)

@bot.command()
async def callmedarling(ctx):
    if message.author.id == bot.user.id:
        return

    channel = ctx.channel
    await ctx.send('call me darling')

    def check(m):
        return m.content == 'darling' and m.author == ctx.author
    try:
        ctx = await bot.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
       await ctx.send('sad')
    else:
        await channel.send('thank you darling')


@bot.command()
async def reactiontest(ctx):
    await ctx.send('react with :hearts:')

    await bot.wait_for('reaction_add')
    print (str(reaction.emoji))


@bot.command()
async def love(ctx):
    await ctx.send('if you love me react with :hearts:')

    def check(reaction, author):
        return author == ctx.author and reaction.emoji == ':hearts:'

    try:
        reaction, author = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('<@{}> You baka' .format(ctx.author.id))

    else:
        await ctx.send('I love you too :hearts:')




@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def masspurge(ctx, amount: int):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=amount)

    message = await ctx.send('done')
    await asyncio.sleep(10) 
    await bot.delete_message(message)


@bot.command()
async def vote(ctx):
    await ctx.channel.send('you can vote for me here: https://discordbots.org/bot/443478651485421598/vote')

@bot.command()
async def get_peppy_user_id(ctx):
    api = OsuApi("12658bf60124fec4e2817e552b6b7ec559120954", connector=AHConnector())
    results = await api.get_user("peppy")
    await ctx.channel.send(results)

@bot.command()
async def suggest(ctx, message):
    channel = bot.get_channel(491685752082661397)
    await channel.send(message)



@bot.command()
async def id(ctx, victim: discord.User):
    Uid = bot.get_user(id)
    print(Uid)

import mentioncommands
    



"""errors"""



bot.run("NDQzNDc4NjUxNDg1NDIxNTk4.DdN9NQ.o3uzr4ym3v2VZ_rr9IS3NCIk-y8")
