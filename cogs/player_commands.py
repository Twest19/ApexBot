import discord
from discord import app_commands
from discord.ext import commands
from apex_api import ApexAPI
from formatter.bot_response_formatter import BotResponseFormatter


class PlayerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apex_api = ApexAPI()

    @app_commands.command(name="stats", description="Displays player stats for on of PC, X1, PS4")
    @app_commands.describe(platform="Platforms to choose from:")
    @app_commands.choices(platform=[
        discord.app_commands.Choice(name="PC", value=1),
        discord.app_commands.Choice(name="X1", value=2),
        discord.app_commands.Choice(name="PS4", value=3)
    ])
    async def stats(self, interaction: discord.Interaction,
                    player_name: str,
                    platform: discord.app_commands.Choice[int]):
        # Gets stats for a given player from the Apex Legends API
        player_stats = self.apex_api.player_data(player_name, platform.name)

        try:
            embed_response = BotResponseFormatter.player_stats_formatter(player_stats)
            await interaction.response.send_message(embed=embed_response)
            # Sends the retrieved response back to the discord channel
        except Exception as err:
            embed = discord.Embed(color=discord.Color.dark_red(),
                                  title="Error:",
                                  description=f"unable to find stats for {player_name}. Try again later")
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="register", description="WORK IN PROGRESS!", )
    async def register(self, interaction: discord.Interaction, player_name: str, platform: str):
        name_uid = self.apex_api.name_to_uid(player_name, platform)
        # Add discord id, uid, platform to database. Then cogs can be used without needing to type name
        # consider just an SQLLite DB

        if name_uid is not None:
            uid = name_uid['uid']
            await interaction.response.send_message(
                content=f'Success! uid {uid} was added for {player_name} on {platform}')
        else:
            await interaction.response.send_message(
                content=f"Unable to register {player_name}. Check name and try again.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PlayerCommands(bot))
