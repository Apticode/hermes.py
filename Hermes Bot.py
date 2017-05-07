import discord
import logging


from discord.ext.commands import Bot


def log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
log()

Hermes_Bot = Bot(command_prefix="!")


@Hermes_Bot.event
async def on_ready():
    print("Blast off")


def commands():
    @Hermes_Bot.command()
    async def hello(*args):
        return await Hermes_Bot.say ("Alright cunts")

Hermes_Bot.run("MzEwNTIwMzcwMzc5NjIwMzUz.C-_4GA.Kupqd38QG9s7C-FL41WZ59igJKQ")

