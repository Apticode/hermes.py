import datetime
from discord.ext import commands


class Time_and_Date():
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command()
    async def date(self):
        await self.hermes.say(datetime.datetime.now().date().strftime("%d/%m/%Y"))

    @commands.command()
    async def time(self):
        await self.hermes.say(str(datetime.datetime.now().time())[:8])

def setup(hermes):
    hermes.add_cog(Time_and_Date(hermes))
