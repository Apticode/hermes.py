import discord
from discord.ext import commands


description = 'As fast as the Greek God and as flexible as the Jamaican.'

modular_initiation = ["cogs.rng", "cogs.information","cogs.time_and_date", "cogs.trivia"]

hermes = commands.Bot(command_prefix='?', description=description)


client = discord.Client()
