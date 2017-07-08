from discord.ext import commands


class Trivia():
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command()
    async def hello(self):
        await self.hermes.say("WAGWAN")

    @commands.command()
    async def trivia(self):
        await self.hermes.say("byeee")


def setup(hermes):
    hermes.add_cog(Trivia(hermes))