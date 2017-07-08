import discord
from discord.ext import commands


description = 'As fast as the Greek God and as flexible as the Jamaican.'

modular_initiation = ["rng", "information","time_and_date", "trivia"]

hermes = commands.Bot(command_prefix='?', description=description)


client = discord.Client()