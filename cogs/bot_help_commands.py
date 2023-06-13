import discord
from discord import app_commands
from discord.ext import commands
from formatter.default_images import DefaultApexImg


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.img = DefaultApexImg()

    @app_commands.command(name="help", description="Additional help and solutions.")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Help",
                              description=" ",
                              colour=discord.Colour.dark_teal()
                              )
        embed.set_thumbnail(url=self.img.gibby())
        embed.add_field(name="**How to use?**",
                        value="Simply type / too pull up a list of available commands or type `/command_info`.",
                        inline=False)
        embed.add_field(name="**Improper Registration?**",
                        value="If the wrong account is connected to your `/my commands` simply "
                              "`/register` again with the correct account",
                        inline=False)
        embed.add_field(name="**PC - Can't find your account?**",
                        value="If you are on PC, but play on Steam, try using the Origin account associated "
                              "with your Apex Legends account.",
                        inline=False)
        embed.add_field(name="**Console - Can't find your account?**",
                        value="Check the `name` and `platform` you entered and try again. If playing on PS5, "
                              "select `PS4` from the platform options.",
                        inline=False)
        embed.add_field(name="**How can I delete my registration?**",
                        value="That is simple, just use the `/my_remove` command to delete your registration "
                              "and connected Apex Account. If you wish to change the associated Apex account, "
                              "do `/register` again with the new account you want to associate with.",
                        inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="command_info", description="Displays how to use different bot commands.")
    async def command_info(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Apex Bot Commands",
                              description="Here are all the available `/commands`:",
                              colour=discord.Colour.dark_teal()
                              )
        embed.set_thumbnail(url=self.img.gibby())
        embed.add_field(name="`/map`", value="Displays the current map rotation.", inline=False)
        embed.add_field(name="`/server`", value="Displays the current server status.", inline=False)
        embed.add_field(name="`/news`", value="Displays Apex Legends news with external "
                                              "links to patch notes and update articles", inline=False)
        embed.add_field(name="`/crafter`", value="Displays the daily crafting rotation items.", inline=False)
        embed.add_field(name="`/search_stats`", value="Retrieves stats for a given player.", inline=False)
        embed.add_field(name="`/register`", value="Registers a given apex account to your discord account. "
                                                  "Provides access to `/my commands` for ease of use.", inline=False)
        embed.add_field(name="`/my_stats`", value="Retrieves stats for the account you registered.", inline=False)
        embed.add_field(name="`/my_remove`", value="Deletes your registration and all history.", inline=False)
        embed.add_field(name="`/help`", value="Provides more information and potential solutions.", inline=False)
        embed.add_field(name="`/command_info`", value="Displays all commands associated with this bot.", inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="info", description="Displays bot information.")
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Info",
                              description="A small synopsis for this bot.",
                              colour=discord.Colour.dark_teal()
                              )
        embed.set_thumbnail(url=self.img.gibby())
        embed.add_field(name="**What does this thing do?**",
                        value="This is an Apex Legends Bot that provides game and player information like stats, "
                              "map and crafter rotations. "
                              "Registering is best for repeated stat commands and is deeply encouraged.",
                        inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HelpCommands(bot))
