import discord
from discord.ext import commands
from apex_api import ApexAPI
from discord import app_commands
from formatter.bot_response_formatter import BotResponseFormatter


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

    @app_commands.command(name="news", description="Displays most recent Apex Legends news.")
    async def news(self, interaction: discord.Interaction):
        game_news = self.apex_api.game_news()

        if game_news is not None:
            await interaction.response.send_message(content=game_news[0]['title'])
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



# {
#     "battle_royale": {
#         "current": {
#             "start": 1681770600,
#             "end": 1681774200,
#             "readableDate_start": "2023-04-17 22:30:00",
#             "readableDate_end": "2023-04-17 23:30:00",
#             "map": "Storm Point",
#             "code": "storm_point_rotation",
#             "DurationInSecs": 3600,
#             "DurationInMinutes": 60,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Storm_Point.png",
#             "remainingSecs": 2826,
#             "remainingMins": 47,
#             "remainingTimer": "00:47:06"
#         },
#         "next": {
#             "start": 1681774200,
#             "end": 1681777800,
#             "readableDate_start": "2023-04-17 23:30:00",
#             "readableDate_end": "2023-04-18 00:30:00",
#             "map": "Broken Moon",
#             "code": "broken_moon_rotation",
#             "DurationInSecs": 3600,
#             "DurationInMinutes": 60,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Broken_Moon.png"
#         }
#     },
#     "arenas": {
#         "current": {
#             "start": 1681770600,
#             "end": 1681771500,
#             "readableDate_start": "2023-04-17 22:30:00",
#             "readableDate_end": "2023-04-17 22:45:00",
#             "map": "Drop Off",
#             "code": "arenas_composite",
#             "DurationInSecs": 900,
#             "DurationInMinutes": 15,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arenas_Dropoff.png",
#             "remainingSecs": 126,
#             "remainingMins": 2,
#             "remainingTimer": "00:02:06"
#         },
#         "next": {
#             "start": 1681771500,
#             "end": 1681772400,
#             "readableDate_start": "2023-04-17 22:45:00",
#             "readableDate_end": "2023-04-17 23:00:00",
#             "map": "Encore",
#             "code": "arenas_encore",
#             "DurationInSecs": 900,
#             "DurationInMinutes": 15,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arena_Encore.png"
#         }
#     },
#     "ranked": {
#         "current": {
#             "start": 1681750800,
#             "end": 1681837200,
#             "readableDate_start": "2023-04-17 17:00:00",
#             "readableDate_end": "2023-04-18 17:00:00",
#             "map": "Broken Moon",
#             "code": "broken_moon_rotation",
#             "DurationInSecs": 86400,
#             "DurationInMinutes": 1440,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Broken_Moon.png",
#             "remainingSecs": 65826,
#             "remainingMins": 1097,
#             "remainingTimer": "18:17:06"
#         },
#         "next": {
#             "start": 1681837200,
#             "end": 1681923600,
#             "readableDate_start": "2023-04-18 17:00:00",
#             "readableDate_end": "2023-04-19 17:00:00",
#             "map": "Olympus",
#             "code": "olympus_rotation",
#             "DurationInSecs": 86400,
#             "DurationInMinutes": 1440,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Olympus.png"
#         }
#     },
#     "arenasRanked": {
#         "current": {
#             "start": 1681770600,
#             "end": 1681771500,
#             "readableDate_start": "2023-04-17 22:30:00",
#             "readableDate_end": "2023-04-17 22:45:00",
#             "map": "Drop Off",
#             "code": "arenas_composite",
#             "DurationInSecs": 900,
#             "DurationInMinutes": 15,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arenas_Dropoff.png",
#             "remainingSecs": 126,
#             "remainingMins": 2,
#             "remainingTimer": "00:02:06"
#         },
#         "next": {
#             "start": 1681771500,
#             "end": 1681772400,
#             "readableDate_start": "2023-04-17 22:45:00",
#             "readableDate_end": "2023-04-17 23:00:00",
#             "map": "Encore",
#             "code": "arenas_encore",
#             "DurationInSecs": 900,
#             "DurationInMinutes": 15,
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arena_Encore.png"
#         }
#     },
#     "ltm": {
#         "current": {
#             "start": 1681770600,
#             "end": 1681771500,
#             "readableDate_start": "2023-04-17 22:30:00",
#             "readableDate_end": "2023-04-17 22:45:00",
#             "map": "Skulltown",
#             "code": "freedm_tdm_skulltown",
#             "DurationInSecs": 900,
#             "DurationInMinutes": 15,
#             "isActive": true,
#             "eventName": "TDM",
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/",
#             "remainingSecs": 126,
#             "remainingMins": 2,
#             "remainingTimer": "00:02:06"
#         },
#         "next": {
#             "start": 1681771500,
#             "end": 1681772400,
#             "readableDate_start": "2023-04-17 22:45:00",
#             "readableDate_end": "2023-04-17 23:00:00",
#             "map": "Estates",
#             "code": "freedm_gungame_estates",
#             "DurationInSecs": 900,
#             "DurationInMinutes": 15,
#             "isActive": true,
#             "eventName": "Gun Run",
#             "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/"
#         }
#     }
# }
