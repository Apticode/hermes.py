from other.core_variables import *
from other.log_function import *
import sys
sys.path.append ('/root/hermes.py/cogs')


def event():
    @client.event
    async def on_member_join(member):
        server = member.server
        welcome_message = 'Welcome {0.mention} to {1.name}!'
        await client.send_message(server, welcome_message.format(member, server))

    @hermes.event
    async def on_ready():
        print("------------------------")
        print('Logged in as:\n{0} (ID: {0.id})'.format(hermes.user))
        print("------------------------")
        await hermes.change_presence(game=discord.Game(name="Futurama|?help"))


@hermes.command()
async def load(extension_name : str):
    try:
        hermes.load_extension(extension_name)
    except (AttributeError, ImportError) as h:
        await hermes.say("```py\n{}: {}\n```".format(type(h).__name__, str(h)))
        return
    await hermes.say("{} loaded.".format(extension_name))


@hermes.command()
async def unload(extension_name : str):
    hermes.unload_extension(extension_name)
    await hermes.say("{} unloaded.".format(extension_name))


@hermes.command(pass_context=True)
async def purge(ctx, number):
    messages = []
    number = int(number)
    async for p in hermes.logs_from(ctx.message.channel, limit=number):
        messages.append(p)
    await hermes.delete_messages(messages)

if __name__ == "__main__":

    for extension in modular_initiation:
        try:
            hermes.load_extension(extension)
        except Exception as h:
            exc = '{}: {}'.format(type(h).__name__, h)
            print('Failed to load module {}\n{}'.format(extension, exc))


event()
log()
hermes.run("token")
