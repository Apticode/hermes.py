import discord
import logging
import asyncio
import random
import sys
import time

from discord.ext import commands


def log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
log()

description = 'As fast as the Greek God and as flexible as the Jamaican.'

current_time = (time.strftime("%H:%M:%S"))

current_date = (time.strftime("%d/%m/%Y"))

ball_answers = [
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

hermes = commands.Bot(command_prefix='?', description=description)


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
        await hermes.say("WAGWAN")

    @hermes.command()
    async def info():
        return await hermes.say("This bot was produced in collaboration between darkhunters and jenk "
                                " \n For further information please private message one of the "
                                "developers or moderators available")

    @hermes.command()
    async def time():
        await hermes.say(current_time)

    @hermes.command(name="commands")
    async def command_list():
        await hermes.say("```Here is a list of some of the commands you can use by using ? then the command\n"
                         "1:) commands \n"
                         "2:) hello \n"
                         "3:) info \n"
                         "4:) time \n "
                         "5:) date \n"
                         "6:) 8ball \n"
                         "7:) coinflip \n"
                         "8:) quote \n"
                         )

    @hermes.command()
    async def date():
        await hermes.say(current_date)

    @hermes.command(name="8ball")
    async def ball():
        await hermes.say(random.choice(ball_answers))

    @hermes.command()
    async def coinflip():
        await hermes.say(random.choice(coin))

    @hermes.command(name="quote")
    async def randomquote():
        await hermes.say(random.choice(quotes))

hermes_command()


hermes.run("MzEwNTIwMzcwMzc5NjIwMzUz.C-_4GA.Kupqd38QG9s7C-FL41WZ59igJKQ")
