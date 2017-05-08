import discord
import logging
import asyncio
import os
import sys
import time
import random

from discord.ext import commands

def log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
log()

description = 'As fast as the Greek God and as flexible as the Jamaican.'

hermes = commands.Bot(command_prefix='?', description=description)

currentTime = (time.strftime("%H:%M:%S"))

currentDate = (time.strftime("%d/%m/%Y"))

answers = [
    "The answer lies in your heart.",
    "I do not know.",
    "Almost certainly.",
    "No.",
    "Yes.",
    "Why do you need to ask?",
    "Go away. I do not wish to answer at this time.",
    "Time will only tell.",
]

coin = [
    "Heads.",
    "Tails.",
]

quotes = [
    "Hermes: \"Sweet something...of...someplace..\"",
    "Hermes: \"Sweet giant anteater of Santa Anita!\"",
    "Hermes: \"Sweet llamas of the Bahamas!\"",
    "Hermes: \"You're just a giant lump of fat. Do you even have an ass under there?\"",
    "Hermes: \"On the bright side, I'll never see Zoidberg again.\"",
    "Hermes: \"It was Zoidberg!\"",
    "Hermes: \"Come on, woman! Just pick something.\"",
    "Hermes: \"Oh, Bender's a model employee.\"",
]

client = discord.Client()

def event():
    @client.event
    async def on_member_join(member):
        server = member.server
        welcome_message = 'Welcome {0.mention} to {1.name}!'
        await client.send_message(server, welcome_message.format(member, server))

    @hermes.event
    async def on_ready():
        print('Logged in as:\n{0} (ID: {0.id})'.format(hermes.user))
        await hermes.change_presence(game=discord.Game(name="Futurama"))\

event()

def hermes_command():
    @hermes.command()
    async def hello():
        await hermes.say("Greetings!")

    @hermes.command()
    async def info():
        return await hermes.say("This bot was produced in collaboration between darkhunters and jenk "
                                " \n For further information please private message one of the "
                                "developers or moderators available")

    @hermes.command()
    async def time():
        await hermes.say(currentTime)

    @hermes.command()
    async def date():
        await hermes.say(currentDate)

    @hermes.command(name="8ball")
    async def ball():
        await hermes.say(random.choice(answers))

    @hermes.command()
    async def coinflip():
        await hermes.say(random.choice(coin))

    @hermes.command(name="quote")
    async def randomquote():
        await hermes.say(random.choice(quotes))

hermes_command()

hermes.run("MzEwNTIwMzcwMzc5NjIwMzUz.C-_4GA.Kupqd38QG9s7C-FL41WZ59igJKQ")

