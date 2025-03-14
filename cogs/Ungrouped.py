import discord
import discord.ext.commands as extCommands
from discord import ApplicationContext, Option, slash_command

from LTLBot import LTLBot


class CogUngrouped(extCommands.Cog, name=__name__):
    def __init__(self, bot: LTLBot):
        self.BOT = bot
        self.__cog_guild_ids__ = [bot.config.guild_id]
    
    
    # Application commands
    @slash_command()
    async def hello_world(self, ctx: ApplicationContext):
        """Hello world!"""
        await ctx.respond("Hello world from the ungrouped group!", ephemeral=True)


# Extension related functions
def setup(bot: LTLBot):
    bot.add_cog(CogUngrouped(bot))

def teardown(bot: LTLBot):
    bot.remove_cog(__name__)
