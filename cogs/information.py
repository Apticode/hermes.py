from discord.ext import commands
import time

class Information():
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command()
    async def website(self):
        await self.hermes.say("You can find our official website @ https://hermespy.apticode.co.uk")


    @commands.command()
    async def info(self):
        return await self.hermes.say("This hermes was produced in collaboration between <@216666694582534145> and <@184361521558716418> "
                                     " \n For further information please contact us on our discord @ "
                                     "https://discord.gg/qvNDzZg/ or visit our website, use the ?website command")
    @commands.command(pass_context=True)

    # makeshift ping for now
    async def ping(self,ctx):
        """pseudo-ping time"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.hermes.send_typing(channel)
        t2 = time.perf_counter()
        await self.hermes.say("ping: {}ms".format(round((t2-t1)*1000)))


def setup(hermes):
    hermes.add_cog(Information(hermes))
