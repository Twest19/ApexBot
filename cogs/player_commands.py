import discord
from discord import app_commands
from discord.ext import commands
from apex_api import ApexAPI


class PlayerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apex_api = ApexAPI()

    @app_commands.command(name="stats", description="Displays player stats format: NAME PLATFORM")
    async def stats(self, interaction: discord.Interaction, player_name: str, player_platform: str):
        # Gets stats for a given player from the Apex Legends API
        player_stats = self.apex_api.player_data(player_name, player_platform)

        if player_stats is not None:
            platform = player_stats["global"]["platform"]
            level = player_stats["global"]["level"]
            p_name = player_stats["global"]["name"]
            next_level = player_stats["global"]["toNextLevelPercent"]

            response = f"{player_name} stats for {player_platform}:" \
                       f"\nPlatform = {platform}" \
                       f"\nlevel = {level}" \
                       f"\nname = {p_name}"
            await interaction.response.send_message(content=response)
            # Sends the retrieved response back to the discord channel
        else:
            await interaction.response.send_message(
                content=f"Unable to find stats for {player_name}. If on PC try using your Origin name.")

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
