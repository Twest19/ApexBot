import discord
from discord import app_commands
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = '''A Discord bot meant to display a given Apex Legends accounts stats, as well as game info 
relating to the store or map rotations.'''

    @app_commands.command(name="help", description="Displays how to use different bot commands.")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Apex Bot Commands",
                              description="Here are all the available cogs:",
                              colour=discord.Colour.dark_teal()
                              )
        command_dict = {
            "stats": "Retrieves stats for a given player"
                     "\nExample: !stats <PLAYERNAME> <PLATFORM>"
                     "\t\t\n<PLAYERNAME> = The player's username, if on PC use Origin ID."
                     "\t\t\n<PLATFORM> = The platform the player is playing on like PC, PS4 or PS5, X1",
            "info": "Provides a description of the bot and a prompt for more cogs",
            "MORE": "COMING SOON, NOT A COMMAND!"
        }

        for command_name, command_description in command_dict.items():
            embed.add_field(name=command_name, value=command_description, inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="info", description="Displays bot information.")
    async def info(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content=self.description + "\nFor a list of commands type !help")

    # @app_commands.command(name="commands", description="Displays all available commands.")
    # async def commands(self, interaction: discord.Interaction):
    #     await self.help.invoke(interaction)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HelpCommands(bot))
