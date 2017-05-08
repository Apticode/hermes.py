import discord
import logging
import asyncio
import os
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

description = 'Hello you cunts.'

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

hermes_command()


hermes.run("MzEwNTIwMzcwMzc5NjIwMzUz.C-_4GA.Kupqd38QG9s7C-FL41WZ59igJKQ")

