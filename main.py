import discord
from keys import *
import random as rand
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("Bot is online.")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am a Test Bot.")


@bot.event
async def on_member_join(member):
    i = rand.randint(1, 5)
    wishes = ["Welcome on board! ", "Welcome! ", "Nice to meet you, ", "Congratulations and welcome, ",
              "Welcome to the team, "]
    all_channels = bot.get_all_channels()
    for channel in all_channels:
        if str(channel) == "general":
            await channel.send(wishes[i] + str(member))

bot.run(TOKEN)
