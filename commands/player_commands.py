from discord.ext import commands
from apex_api import ApexAPI


class PlayerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apex_api = ApexAPI()

    @commands.command()
    async def stats(self, ctx, player_name: str, player_platform: str):
        # Gets stats for a given player from the Apex Legends API
        player_stats = self.apex_api.player_data(player_name, player_platform)

        if player_stats is not None:
            platform = player_stats["global"]["platform"]
            level = player_stats["global"]["level"]
            p_name = player_stats["global"]["name"]
            response = f"{player_name} stats for {player_platform}:" \
                       f"\nPlatform = {platform}" \
                       f"\nlevel = {level}" \
                       f"\nname = {p_name}"
            await ctx.send(response)  # Sends the retrieved response back to the discord channel
        else:
            await ctx.send(f"Unable to find stats for {player_name}. If on PC try using your Origin name.")

    @commands.command()
    async def register(self, ctx, player_name, platform):
        name_uid = self.apex_api.name_to_uid(player_name, platform)
        # Add discord id, uid, platform to database. Then commands can be used without needing to type name
        # consider just an SQLLite DB

        if name_uid is not None:
            uid = name_uid['uid']
            await ctx.send(f'Success! uid {uid} was added for {player_name} on {platform}')
        else:
            await ctx.send(f"Unable to register {player_name}. Check name and try again.")
