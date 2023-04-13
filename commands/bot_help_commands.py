import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = '''A Discord bot meant to display a given Apex Legends accounts stats, as well as game info 
relating to the store or map rotations.'''

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Apex Bot Commands",
                              description="Here are all the available commands:",
                              colour=discord.Colour.dark_teal())
        command_dict = {
            "stats": "Retrieves stats for a given player"
                     "\nExample: !stats <PLAYERNAME> <PLATFORM>"
                     "\t\t\n<PLAYERNAME> = The player's username, if on PC use Origin ID."
                     "\t\t\n<PLATFORM> = The platform the player is playing on like PC, PS4 or PS5, X1",
            "info": "Provides a description of the bot and a prompt for more commands",
            "commands": "Gives a list off all the commands available",
        }

        for command_name, command_description in command_dict.items():
            embed.add_field(name=command_name, value=command_description, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        await ctx.send(self.description)
        await ctx.send("\nFor a list of commands type !help or !commands")

    @commands.command()
    async def commands(self, ctx):
        await self.help.invoke(ctx)
