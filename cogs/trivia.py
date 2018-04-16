from discord.ext import commands
import time

class Trivia:
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hey' + str(ctx.author))

    @commands.command()
    async def trivia(self):
        await self.hermes.say("byeee")

    @commands.command()
    async def test(self, arg):
        await self.hermes.say(arg)

    # makeshift ping for now
    async def ping(self, ctx):
        """pseudo-ping time"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.hermes.send_typing(channel)
        t2 = time.perf_counter()
        await self.hermes.say("ping: {}ms".format(round((t2 - t1) * 1000)))


def setup(hermes):
    hermes.add_cog(Trivia(hermes))
