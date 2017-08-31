import discord.utils
from discord.ext import commands

# Credits for this goes to tuxbot and red bot which can be found at:
# https://github.com/outout14/tuxbot-bot
# https://github.com/Cog-Creators/Red-DiscordBot

def is_owner_check(message):
    owner = message.author.id in ['216666694582534145', '184361521558716418']
    return owner  # Owner of the bot


def is_owner(warn=True):
    def check(ctx, warn):
        owner = is_owner_check(ctx.message)
        if not owner and warn:
                print(ctx.message.author.name + "You are not the owner" + ctx.message.content)
        return owner

    owner = commands.check(lambda ctx: check(ctx, warn))
    return owner

def check_permissions(ctx, perms):
    if is_owner_check(ctx):
        return True
    elif not perms:
        return False

    ch = ctx.message.channel
    author = ctx.message.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())


def serverowner_or_permissions(**perms):
    def predicate(ctx):
        if ctx.message.server is None:
            return False
        server = ctx.message.server
        owner = server.owner

        if ctx.message.author.id == owner.id:
            return True

        return check_permissions(ctx,perms)
    return commands.check(predicate)
