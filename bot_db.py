from sqlite3 import IntegrityError


class BotDatabase:
    """Database commands for the discord bot. Uses a 'Player' type for inputs"""
    def __init__(self, conn, cursor):
        self.conn = conn
        self.c = cursor

    def insert_player(self, player):
        try:
            with self.conn:
                self.c.execute("INSERT INTO player VALUES (:discord, :apex, :platform)",
                          {'discord': player.discord_id, 'apex': player.apex_id, 'platform': player.platform})
            print("SUCCESS!!")
        except IntegrityError:
            # This Discord ID is already in the DB, only want one Discord ID assigned to one Apex Account
            # This will update the player instead
            self.update_player(player)

    def update_player(self, player):
        with self.conn:
            self.c.execute("""UPDATE player 
            SET discordID=:discord, apexID=:new_apex, platform=:new_platform 
            WHERE discordID=:discord""",
                      {'discord': player.discord_id, 'new_apex': player.apex_id, 'new_platform': player.platform})

    def get_player_by_discord_id(self, player):
        self.c.execute("SELECT * FROM player WHERE discordID=:discord", {'discord': player})
        return self.c.fetchone()

    def get_player_apex_id(self, player):
        self.c.execute("SELECT apexID, platform FROM player WHERE discordID=:discord", {'discord': player})
        print("Works!")
        return self.c.fetchone()

    def delete_player(self, player):
        with self.conn:
            self.c.execute("DELETE FROM player WHERE discordID=:discord", {'discord': player})
