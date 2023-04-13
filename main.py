import asyncio
import os
import discord
from discord.ext import commands
from commands.bot_help_commands import HelpCommands
from commands.player_commands import PlayerCommands
from commands.game_info_commands import GameInfoCommands


if __name__ == "__main__":
    description = '''A Discord bot meant to display a given Apex Legends accounts stats, as well as game info 
    relating to the store or map rotations.'''

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', description=description, intents=intents)
    # Remove the default help command to implement a custom one
    bot.remove_command('help')
    # apex_api = ApexAPI()
    TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')


    async def main(a_bot):
        await a_bot.add_cog(HelpCommands(a_bot))
        await a_bot.add_cog(PlayerCommands(a_bot))
        await a_bot.add_cog(GameInfoCommands(a_bot))

    asyncio.run(main(bot))
    bot.run(TOKEN)
