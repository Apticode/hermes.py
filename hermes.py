import discord
import logging
import asyncio
import os


from discord.ext import commands


def log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
log()

description = 'Hello you cunts.'

Hermes_Bot = commands.Bot(command_prefix='?', description=description)

client = discord.Client()
member = discord.Member

def event():
    @Hermes_Bot.event

    async def on_ready():
        print('Logged in as:\n{0} (ID: {0.id})'.format(Hermes_Bot.user))
        await Hermes_Bot.change_presence(game=discord.Game(name="Futurama"))

    async def on_member_join(member):
        server = member.server
        fmt = 'Welcome {0.mention} to {1.name}!'
        await client.send_message(server, fmt.format(member, server))



event()


def commands():
    @Hermes_Bot.command()
    async def hello():
        return await Hermes_Bot.say ("Alright cunts")

    async def joined(member: discord.member):
        """Fatty has arrived"""
        await Hermes_Bot.say('{0.name} joined in {0.joined_at}'.format(member))


commands()


Hermes_Bot.run("MzEwNTIwMzcwMzc5NjIwMzUz.C-_4GA.Kupqd38QG9s7C-FL41WZ59igJKQ")
