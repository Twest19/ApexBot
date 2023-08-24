# Apex Legends Discord Bot

## Description
Created to simplify the process of retrieving in-game information for "Apex Legends," this Discord bot allows players and fans to access real-time game data without needing to be in-game. With features like map rotations, player stats, and in-game shop updates, the bot serves as a handy tool for any player looking to stay updated.

## Screenshots
COMING SOON

## Technologies Used
- **Language:** Python
- **Library:** ![discord.py](https://discordpy.readthedocs.io/en/stable/)
- **API:** ![Apex Legends AP](https://apexlegendsapi.com/#introduction)
- **Hosting:** Can be hosted both locally or on a server. My personal use of this bot is hosted on a Digital Ocean Droplet for continuous uptime. Make use of those GitHub Student pack credits!

## Prerequisites
- A Discord API key
- An Apex Legends API key

## Features
- **Game Information Retrieval:** Provides real-time data such as map rotations, player stats, and in-game shop items.
- **User Registration System:** Users can link their in-game IDs to Discord for simplified repeated commands, thanks to an integration with an SQLite database.

## Slash Commands
All commands are executed as slash commands. Simply type `/` in a server with the bot, and a pop-up will display available commands.
Examples:
- `/search_stats [player_name] [platform]`: Retrieve player statistics of your friends or foes.
- `/crafter`: Display current items in the in-game crafter.
- `/register [player_name] [platform]`: Register with the bot to seamlessly excute commands pertaining to your Apex Legends account.
... and so on.

## Note
Ensure your Discord server has appropriate permissions set for the bot to function properly. All of this will be taken care of in your initial setup and invitation of your bot!

## Acknowledgements
This bot was developed as a personal project and is not affiliated with or endorsed by the official "Apex Legends" game or its creators. The same applies to the unofficial "Apex Legends API" that aided in the creation of this bot for personal use. You can visit that API via the hyperlink provided above.
