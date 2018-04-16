import discord
from discord.ext import commands


class Moderator():
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command(pass_context=True)
    async def kick(self, ctx, userName: discord.User):
        await self.hermes.kick(userName)
        await self.hermes.say("__** User has been successfully kicked!**__")

    @commands.command(pass_context=True)
    async def ban(self, ctx, userName: discord.User):
        await self.hermes.ban(userName)
        await self.hermes.say("__** User has been successfully banned!**__")




def setup(hermes):
    hermes.add_cog(Moderator(hermes))