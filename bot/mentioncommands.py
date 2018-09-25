import discord
from discord.ext import commands
from discord.ext.commands import Bot
from builtins import bot
import asyncio
import random


@bot.command(pass_context=True)
async def hug(ctx):
    await ctx.send('<@{0}> hugged <@{1}>.'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))

@bot.command(pass_context=True)
async def lick(ctx):
    await ctx.send('<@{0}> licked <@{1}>.'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))

@bot.command(pass_context=True)
async def kiss(ctx):
    await ctx.send('<@{0}> kissed <@{1}>.'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))
@bot.command(pass_context=True)
async def slap(ctx):
    await ctx.send('<@{0}> slapped <@{1}>. I hope you learned your lesson.'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))

@bot.command(pass_context=True)
async def cuddle(ctx):
    await ctx.send('<@{0}> cuddled <@{1}>. awww so  cute.'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))

@bot.command(pass_context=True)
async def jail(ctx):
    await ctx.send('<@{0}> put <@{1}> in jail. What did you do wrong?'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))

@bot.command(pass_context=True)
async def kill(ctx):
    await ctx.send('<@{0}> killed <@{1}>. That\'s not nice.'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))


@bot.command()
async def swat(ctx):
    swatgif = ['https://media.giphy.com/media/4IygCzR7kkoWk/giphy.gif', 'https://media.giphy.com/media/3o6wNPIj7WBQcJCReE/giphy.gif', 'https://media.giphy.com/media/3osBLaQjYdcuVYpgXu/giphy.gif', 'https://media.giphy.com/media/1qYEntySk1sUfYVmyB/giphy.gif' ]
    rswatgif = random.choice(swatgif)
    embed = discord.Embed()
    embed.set_image(url=rswatgif)
    
    await ctx.send('<@{0}> Swatted <@{1}>. Freaking lolicon. '\
                                   .format(ctx.author.id, ctx.message.mentions[0].id), embed=embed)

@bot.command()
async def suicide(ctx, message):
    if ctx.message.content == 'ç!suicide':
        await ctx.send('<@{0}> wants to commit suicide. Don\'t do it it\'s bad.'\
                       .format(ctx.author.id))
    else:
        await ctx.send('<@{0}> wants <@{1}> to commit suicide. Don\'t follow his advice.'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))

    print (message)

@bot.command(pass_context=True)
async def pat(ctx):
    await ctx.send('<@{0}> Patted <@{1}>'\
                                   .format(ctx.author.id, ctx.message.mentions[0].id))
    print (ctx.author.id)
    print(discord.user.id)

@bot.command()
async def spam(ctx, victim: discord.User, amount: int, message):
    for _ in range(amount):
        await victim.send(message)

    await ctx.send('spammed {victim}')

    print (bot.get_victim(id))
