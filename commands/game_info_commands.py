from discord.ext import commands
from apex_api import ApexAPI


class GameInfoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apex_api = ApexAPI()

    @commands.command()
    async def maps(self, ctx):
        current_maps = self.apex_api.map_rotation()

        if current_maps is not None:
            current = current_maps['current']['map']
            next_map = current_maps['next']['map']
            response = f"Current Map: {current}" \
                       f"\nNext Map: {next_map}"
            await ctx.send(response)
        else:
            await ctx.send(f"Error: Unable to retrieve current map rotation, please try again.")

    @commands.command()
    async def crafter(self, ctx):
        crafting_rotation = self.apex_api.crafting_rotation()

        if crafting_rotation is not None:
            response = "\n"
            for item in crafting_rotation:
                response += f"{item['bundle']}\n"
            await ctx.send(response)
        else:
            await ctx.send(f"Error: Unable to retrieve crafting rotation, please try again.")

    @commands.command()
    async def news(self, ctx):
        game_news = self.apex_api.game_news()

        if game_news is not None:
            await ctx.send(game_news[0]['title'])
        else:
            await ctx.send(f"Error: Unable to retrieve current game news, please try again.")

    @commands.command()
    async def server(self, ctx):
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

            await ctx.send(response)
        else:
            await ctx.send(f"Error: Unable to server status, please try again.")

