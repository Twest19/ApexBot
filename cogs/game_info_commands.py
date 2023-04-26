import discord
from discord.ext import commands
from apex_api import ApexAPI
from discord import app_commands
from formatter.bot_response_formatter import BotResponseFormatter
from buttons import LinkButtons


class GameInfoCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.apex_api = ApexAPI()

    @app_commands.command(name="map", description="Displays the current map rotation.")
    async def maps(self, interaction: discord.Interaction):
        current_maps = self.apex_api.map_rotation()

        if current_maps is not None:
            embed_response = BotResponseFormatter.map_formatter(current_maps)
            await interaction.response.send_message(embed=embed_response)
        else:
            await interaction.response.send_message(
                content=f"Error: Unable to retrieve current map rotation, please try again.")

    @app_commands.command(name="crafter", description="Displays current crafting rotation.")
    async def crafter(self, interaction: discord.Interaction):
        crafting_rotation = self.apex_api.crafting_rotation()

        if crafting_rotation is not None:
            embed_response = BotResponseFormatter.crafter_formatter(crafting_rotation)
            await interaction.response.send_message(embeds=embed_response)
        else:
            await interaction.response.send_message(
                content=f"Error: Unable to retrieve crafting rotation, please try again.")

    @app_commands.command(name="news",
                          description="Displays most recent Apex Legends news and old older news with buttons.")
    async def news(self, interaction: discord.Interaction):
        game_news = self.apex_api.game_news()

        if game_news is not None:
            embed_response = BotResponseFormatter.news_formatter(game_news[0])
            view = LinkButtons(game_news, 0)
            await interaction.response.send_message(embed=embed_response, view=view)
        else:
            await interaction.response.send_message(
                content=f"Error: Unable to retrieve current game news, please try again.")

    @app_commands.command(name="server", description="Displays Apex Legends server status.")
    async def server(self, interaction: discord.Interaction):
        server_status = self.apex_api.server_status()

        if server_status is not None:
            login = server_status["Origin_login"]["US-Central"]["Status"]
            accounts = server_status["EA_accounts"]["US-Central"]["Status"]
            playstation = server_status["otherPlatforms"]["Playstation-Network"]["Status"]
            xbox = server_status["otherPlatforms"]["Xbox-Live"]["Status"]

            response = f"""
                    \nLogin: {login}
                    \nAccounts: {accounts}
                    \nPlaystation Network: {playstation}
                    \nXbox Live: {xbox}
                """

            await interaction.response.send_message(content=response)
        else:
            await interaction.response.send_message(content=f"Error: Unable to server status, please try again.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GameInfoCommands(bot))
