from discord.ext import commands


class Information():
    def __init__(self, hermes):
        self.hermes = hermes

    @commands.command()
    async def website(self):
        await self.hermes.say("You can find our official website @ https://hermespy.tk/")

    @commands.command()
    async def helpme(self,):
        await self.hermes.say("```Here is a list of some of the commands you can use by using ? then the command\n"
                              "1:) commands \n"
                              "2:) hello \n"
                              "3:) info \n"
                              "4:) time \n"
                              "5:) date \n"
                              "6:) 8ball \n"
                              "7:) coinflip \n"
                              "8:) quote \n```"
                              )

    @commands.command()
    async def info(self):
        return await self.hermes.say("This hermes was produced in collaboration between darkhunters and jenk "
                                     " \n For further information please private message one of the "
                                     "developers or moderators available")


def setup(hermes):
    hermes.add_cog(Information(hermes))