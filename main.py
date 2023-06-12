import os
import discord
from discord.ext import commands
import sqlite3
from bot_db import BotDatabase


class Client(commands.Bot):
    def __init__(self, database):
        self.database = database
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        description = '''A Discord bot meant to display a given Apex Legends accounts stats, as well as game info 
    relating to the store or map rotations.'''
        super().__init__(command_prefix='!',
                         description=description,
                         intents=intents)

        self.cogs_list = ["cogs.game_info_commands", "cogs.bot_help_commands", "cogs.player_commands"]

    async def setup_hook(self):
        print("setting up hook")
        for ext in self.cogs_list:
            await self.load_extension(ext)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        synced = await self.tree.sync()
        print(f'Slash Commands synced: {str(len(synced))}')


if __name__ == "__main__":
    conn = None
    try:
        # Create Database Connection and cursor
        conn = sqlite3.connect('the_apex_bot.db')
        c = conn.cursor()

        # Get our Database Interface
        db = BotDatabase(conn, c)

        # Create discord bot client
        client = Client(db)
        client.remove_command('help')
        TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
        client.run(TOKEN)
    finally:
        # Closes database connection
        conn.close()
