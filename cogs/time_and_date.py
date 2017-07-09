import time
from discord.ext import commands

current_time = (time.strftime("%H:%M:%S"))
current_date = (time.strftime("%d/%m/%Y"))

class Time_and_Date():
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command()
    async def date(self):
        await self.hermes.say(current_date)

    @commands.command()
    async def time(self):
        await self.hermes.say(current_time)

def setup(hermes):
    hermes.add_cog(Time_and_Date(hermes))
