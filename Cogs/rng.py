import random
from discord.ext import commands
from rng_variables import *


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


def setup(hermes):
    hermes.add_cog(RNG(hermes))