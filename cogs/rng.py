import random
from discord.ext import commands
from other.rng_variables import *


class RNG():
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command()
    async def coinflip(self):
        await self.hermes.say(random.choice(coin))

    @commands.command(name="8ball")
    async def ball(self):
        await self.hermes.say(random.choice(ball_answers))

    @commands.command()
    async def rateme(self,):
        await self.hermes.say(random.choice(rate_answers))

    @commands.command(name="quote")
    async def randomquote(self):
        await self.hermes.say(random.choice(quotes))
    
    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, *choices: str):
        await self.hermes.say(random.choice(choices))    


def setup(hermes):
    hermes.add_cog(RNG(hermes))
