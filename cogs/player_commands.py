import discord
from discord import app_commands
from discord.ext import commands
from apex_api import ApexAPI
from formatter.bot_response_formatter import BotResponseFormatter
from player import Player


class PlayerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apex_api = ApexAPI()

    """Command for unregistered users or to find other players stats."""
    @app_commands.command(name="search_stats", description="Search a player on of PC, X1, or PS4 and display their "
                                                           "stats")
    @app_commands.describe(platform="Platforms to choose from:")
    @app_commands.choices(platform=[
        discord.app_commands.Choice(name="PC", value=1),
        discord.app_commands.Choice(name="X1", value=2),
        discord.app_commands.Choice(name="PS4", value=3),
        discord.app_commands.Choice(name="Switch", value=4)
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

    """Command to register with the bot to make user experience better."""
    @app_commands.command(name="register", description="Registers user to the database for access to /my commands.")
    @app_commands.describe(platform="Platforms to choose from:")
    @app_commands.choices(platform=[
        discord.app_commands.Choice(name="PC", value=1),
        discord.app_commands.Choice(name="X1", value=2),
        discord.app_commands.Choice(name="PS4", value=3),
        discord.app_commands.Choice(name="Switch", value=4)
    ])
    async def register(self, interaction: discord.Interaction, player_name: str,
                       platform: discord.app_commands.Choice[int]):
        print(player_name)

        name_uid = self.apex_api.name_to_uid(player_name, platform.name)
        print(name_uid)

        # Add discord id, apex id, platform to database. Then cogs can be used without needing to type name
        if name_uid is not None:
            apex_uid = name_uid['uid']
            discord_id = interaction.user.id

            new_player = Player(discord_id, apex_uid, platform.name)
            self.bot.database.insert_player(new_player)

            await interaction.response.send_message(
                content=f'Success, {player_name} registered for {platform.name}!')
        else:
            await interaction.response.send_message(
                content=f"Unable to register {player_name}. Check name and try again.")

    """Command for registered user to get their stats."""
    @app_commands.command(name="my_stats", description="Displays a registered users stats.")
    async def my_stats(self, interaction: discord.Interaction):
        result = self.bot.database.get_player_apex_id(str(interaction.user.id))

        if result is not None:  # Make sure a matching player was found
            apex_id = result[0]
            platform = result[1]

            # Gets stats for a given player from the Apex Legends API
            player_stats = self.apex_api.uid_data(apex_id, platform)
            embed_response = BotResponseFormatter.player_stats_formatter(player_stats)
            # Sends the retrieved response back to the discord channel
            await interaction.response.send_message(embed=embed_response)
        else:
            embed = discord.Embed(color=discord.Color.dark_red(),
                                  title="Error:",
                                  description=f"Looks like you might not be in the database. "
                                              f"Use the /register command to get registered!")
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PlayerCommands(bot))
