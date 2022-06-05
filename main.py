import discord
import random

from discord.ext import commands
from code_forces_checker import checker

print('Бот запускается...')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Бот готов к работе!')
    
@bot.command()
async def check(ctx, *arg): # Работает по команде "/check {логины через пробел}"
    logins = []
    for argum in arg:
        logins.append(str(argum))
    await ctx.reply(checker(logins))

token = open('token.txt', 'r').readline()
bot.run(token)
