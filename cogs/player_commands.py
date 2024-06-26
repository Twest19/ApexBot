import discord
from discord import app_commands
from discord.ext import commands
from apex_api import ApexAPI
from apex_exception import ApexException
from formatter.bot_response_formatter import BotResponseFormatter
from formatter.default_images import DefaultApexImg
from player import Player


class PlayerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apex_api = ApexAPI()
        self.img = DefaultApexImg()

    """Command for unregistered users or to search players stats."""
    @app_commands.command(name="search_stats", description="Search a player on of PC, X1, or PS4 and display their "
                                                           "stats")
    @app_commands.describe(platform="Platforms to choose from:")
    @app_commands.choices(platform=[
        discord.app_commands.Choice(name="PC", value=1),
        discord.app_commands.Choice(name="X1", value=2),
        discord.app_commands.Choice(name="PS4", value=3),
        discord.app_commands.Choice(name="Switch", value=4)
    ])
    async def search_stats(self, interaction: discord.Interaction,
                           player_name: str,
                           platform: discord.app_commands.Choice[int]):
        try:
            # Gets stats for a given player from the Apex Legends API
            player_stats = self.apex_api.player_data(player_name, platform.name)
            embed_response = BotResponseFormatter.player_stats_formatter(player_stats)
            await interaction.response.send_message(embed=embed_response)
            # Sends the retrieved response back to the discord channel
        except ApexException as e:
            embed = discord.Embed(color=discord.Color.dark_red(),
                                  title=f"**Error: {e.code}**",
                                  description=f"{e.message}\n\n Unable to find stats for {player_name}. \n\nCheck the `name` and "
                                              f"`platform`, then try again...")
            embed.set_thumbnail(url=self.img.gibby())
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

        embed = discord.Embed(color=0xff0000, title="Registration")
        embed.set_thumbnail(url=self.img.gibby())
        embeds = [embed]

        try:
            # First need to make sure this a valid apex account, so do a query
            player = self.apex_api.player_data(player_name, platform.name) # Raises an exception
            # Add discord id, apex id, platform to database. Then cogs can be used without needing to type name
            apex_uid = player.get("global", {}).get("uid")
            discord_id = interaction.user.id
            new_player = Player(discord_id, apex_uid, platform.name)

            if self.bot.database.insert_player(new_player):
                embed.color = discord.Color.green()
                embed.add_field(name="**Success!**", value=f"{player_name} registered for {platform.name}! "
                                                           f"You can now use the `/my commands` and "
                                                           "check out your stats below.", inline=True)
                embed.add_field(name="\u200b", value="\u200b", inline=True)
                embed.set_footer(text="Something Wrong? Do `/help` for potential solutions.")
                current_stats = BotResponseFormatter().player_stats_formatter(player)
                embeds.append(current_stats)
            else:
                embed.add_field(name="**Database Error**", value=f'Unable to register {player_name}. '
                                                         f'Check `name` and `platform`, then try again!')
        except ApexException as e:
            embed.description = f"Unable to register {player_name}."
            embed.add_field(name=f"**Error {e.code}**", value=f'{e.message}')
            embed.set_footer(text="Check `name` and `platform`, then try again.")
        finally:
            embeds[0] = embed
            await interaction.response.send_message(embeds=embeds)
        
    """Command for registered user to get their stats."""
    @app_commands.command(name="my_stats", description="Displays a registered users stats. To register /register")
    async def my_stats(self, interaction: discord.Interaction):
        result = self.bot.database.get_player_apex_id(str(interaction.user.id))
        
        if result is not None:  # Make sure a matching player was found
            apex_id = result[0]
            platform = result[1]

            try:
                # Gets stats for a given player from the Apex Legends API
                player_stats = self.apex_api.uid_data(apex_id, platform)
                embed = BotResponseFormatter.player_stats_formatter(player_stats)
            except ApexException as e:
                embed = discord.Embed(color=discord.Color.dark_red(),
                                  title=f"**Error {e.code}**",
                                  description=f"{e.message}")
        else:
            embed = discord.Embed(color=discord.Color.dark_red(),
                                  title="Error:",
                                  description=f"Looks like you might not be in the database. "
                                              f"Use the `/register` command to get registered!")
        # Sends the retrieved response back to the discord channel
        await interaction.response.send_message(embed=embed)

    """Command for to remove registered users."""
    @app_commands.command(name="my_remove", description="Removes registered account information.")
    async def my_remove(self, interaction: discord.Interaction):
        result = self.bot.database.delete_player(str(interaction.user.id))

        if result:  # Deletion was successful in the db
            embed = discord.Embed(color=discord.Color.green(),
                                  title="**Success!**",
                                  description=f"You have been successfully removed. If you wish to "
                                              f"register again do `/register` at any time.")
        else:
            embed = discord.Embed(color=discord.Color.dark_red(),
                                  title="Error:",
                                  description=f"Looks like you might not be registered. "
                                              f"You must be registered to remove yourself. "
                                              f"Use the `/register` command to get registered!")
        # Sends the retrieved response back to the discord channel
        await interaction.response.send_message(embed=embed)    


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PlayerCommands(bot))
