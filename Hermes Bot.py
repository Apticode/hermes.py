import discord
from discord.ext.commands import bot

Hermes_Bot =bot(command_prefix="!")

@Hermes_Bot.event
async def on_read():
    print ("Blast off")

@Hermes_Bot.command()
async def hello (*args):
    return await Hermes_Bot.say ("Alright cunts")

Hermes_Bot.run("{MzEwNTIwMzcwMzc5NjIwMzUz.C-_K7g.wc3TaZqSVOZ0zjyIns33y2jQaCM}")

