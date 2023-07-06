import discord
from discord.ext import commands
from apex_api import ApexAPI
from discord import app_commands
from apex_exception import ApexException
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

        try:
            current_maps = self.apex_api.map_rotation()
            embed = BotResponseFormatter.map_formatter(current_maps, embed)
        except ApexException as e:
            embed.add_field(name=f"**Error: {e.code}**",
                            value=f"{e.message}\n\nUnable to retrieve current map rotation, please try again.", inline=False)
        finally:            
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="crafter", description="Displays current crafting rotation.")
    async def crafter(self, interaction: discord.Interaction):
        embed = discord.Embed(color=0x098d8d,
                                    title="Crafting Rotation",
                                    description="Apex Legends current crafting rotation")
        embeds = [embed]
        try:
            crafting_rotation = self.apex_api.crafting_rotation()
            embeds = BotResponseFormatter.crafter_formatter(crafting_rotation, embeds)
        except ApexException as e:
            embed.add_field(name=f"**Error {e.code}**",
                                  value=f"{e.message} \nCrafting rotation, currently unavailable. "
                                        "Check `/server` for potential Apex Legends issues and try again later.",
                                  inline=False)
            embeds[0] = embed
        finally:
            await interaction.response.send_message(embeds=embeds)

    @app_commands.command(name="news",
                          description="Displays most recent Apex Legends news and old older news with buttons.")
    async def news(self, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.dark_teal(),
                              title="Apex News")

        try:
            game_news = self.apex_api.game_news()
            embed_response = BotResponseFormatter.news_formatter(game_news[0], embed)
            view = LinkButtons(game_news, 0, embed)
            await interaction.response.send_message(embed=embed_response, view=view)
        except ApexException as e:
            embed.description = f"News currently Unavailable. \n\n{e.code}: {e.message}"
            embed.set_thumbnail(url=self.img)
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="server", description="Displays Apex Legends server status.")
    async def server(self, interaction: discord.Interaction):
        embed = discord.Embed(color=0x098d8d, title="Server Status", url="https://apexlegendsstatus.com")
        embed.set_thumbnail(url=self.img.gibby())

        try: 
            server_status = self.apex_api.server_status()
            embed = BotResponseFormatter.server_formatter(server_status, embed)
        except ApexException as e:
            embed.add_field(name=f"**Error: {e.code}**", value=f"{e.message}\n Apex Servers or API may be down,"
                            "click the link for more info.", inline=True)
        finally:
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="predator", description="Displays RP needed for predator on all platforms.")
    async def predator(self, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.dark_red(), 
                              title="Predator", 
                              description="RP needed to reach Apex Predator in BR on all platforms.")
        embed.set_thumbnail(url=self.img.pred())

        try: 
            pred_points = self.apex_api.predator()
            embed = BotResponseFormatter.predator_formatter(pred_points, embed)
        except ApexException as e:
            embed.add_field(name=f"**Error: {e.code}**", value=f"{e.message}\n Apex Servers or API may be down,"
                            "try again later.", inline=True)
        finally:
            await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GameInfoCommands(bot))
