import discord
from discord.ext import commands
from apex_api import ApexAPI
from discord import app_commands
from formatter.bot_response_formatter import BotResponseFormatter
from formatter.default_images import DefaultApexImg
from buttons import LinkButtons


class GameInfoCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.apex_api = ApexAPI()
        self.img = DefaultApexImg()

    @app_commands.command(name="map", description="Displays the current map rotation.")
    async def maps(self, interaction: discord.Interaction):
        embed = discord.Embed(color=0xff0000, title="Map Rotation", description="Apex Legends current map rotation")
        embed.set_thumbnail(url=self.img.gibby())
        current_maps = self.apex_api.map_rotation()

        if current_maps is not None:
            embed_response = BotResponseFormatter.map_formatter(current_maps, embed)
            await interaction.response.send_message(embed=embed_response)
        else:
            embed.add_field(name="**Error:**",
                            value="Unable to retrieve current map rotation, please try again.", inline=False)
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="crafter", description="Displays current crafting rotation.")
    async def crafter(self, interaction: discord.Interaction):
        embed_title = discord.Embed(color=0x098d8d,
                                    title="Crafting Rotation",
                                    description="Apex Legends current crafting rotation")

        crafting_rotation = self.apex_api.crafting_rotation()

        if crafting_rotation is not None:
            embed_response = BotResponseFormatter.crafter_formatter(crafting_rotation, embed_title)
            await interaction.response.send_message(embeds=embed_response)
        else:
            embed_title.add_field(name="**Error**",
                                  value="Crafting rotation, currently unavailable. "
                                        "Check `/server` for potential Apex Legends issues and try again later.",
                                  inline=False)
            await interaction.response.send_message(embed=embed_title)

    @app_commands.command(name="news",
                          description="Displays most recent Apex Legends news and old older news with buttons.")
    async def news(self, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.dark_red(),
                              title="Apex News")

        game_news = self.apex_api.game_news()

        if game_news is not None and "title" in game_news[0]:
            embed_response = BotResponseFormatter.news_formatter(game_news[0], embed)
            view = LinkButtons(game_news, 0, embed)
            await interaction.response.send_message(embed=embed_response, view=view)
        else:
            embed.description = "News currently Unavailable"
            embed.set_thumbnail(url=self.img)
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="server", description="Displays Apex Legends server status.")
    async def server(self, interaction: discord.Interaction):
        embed = discord.Embed(color=0x098d8d, title="Server Status", url="https://apexlegendsstatus.com")
        embed.set_thumbnail(url=self.img.gibby())

        server_status = self.apex_api.server_status()

        if server_status is not None:
            embed_response = BotResponseFormatter.server_formatter(server_status, embed)
            await interaction.response.send_message(embed=embed_response)
        else:
            embed.add_field(name="**Error:**", value="Unable to server status, please try again.", inline=True)
            await interaction.response.send_message(embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GameInfoCommands(bot))
