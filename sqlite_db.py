import sqlite3
from player import Player

conn = sqlite3.connect('player.db')

c = conn.cursor()

# c.execute("""CREATE TABLE player (
#             discordID text,
#             apexID text,
#             platform text
#             )""")
player_1 = Player(1, 2, "X1")
player_2 = Player(123, 31235, "PS5")
player_3 = Player(1234, 646, "PC")


def insert_player(player):
    with conn:
        c.execute("INSERT INTO player VALUES (:discord, :apex, :platform)",
                  {'discord': player.discord_id, 'apex': player.apex_id, 'platform': player.platform})


def update_player(player):
    with conn:
        c.execute("""UPDATE player 
        SET discordID=:discord, apexID=:new_apex, platform=:new_platform 
        WHERE discordID=:discord""",
                  {'discord': player.discord_id, 'apexID': player.apex_id, 'platform': player.platform})


def get_player_by_discord_id(player):
    c.execute("SELECT * FROM player WHERE discordID=:discord", {'discord': player.discord_id})
    return c.fetchone()


def get_player_apex_id(player):
    c.execute("SELECT apexID FROM player WHERE discordID=:discord", {'discord': player.discord_id})
    return c.fetchone()


def delete_player(player):
    with conn:
        c.execute("DELETE FROM player WHERE discordID=:discord", {'discord': player.discord_id})


# insert_player(player_1)
# insert_player(player_2)
# insert_player(player_3)

# print(get_player_by_discord_id(player_3))
# print(get_player_apex_id(player_3))
# delete_player(player_3)

# # Proper way to insert number 1
# c.execute("INSERT INTO player VALUES (?, ?, ?)", (player_1.discord_id, player_1.apex_id, player_1.platform))
#
# conn.commit()
#
# # Proper way to insert number 2
# c.execute("INSERT INTO player VALUES (:discord, :apex, :platform)",
#           {'discord': player_2.discord_id, 'apex': player_2.apex_id, 'platform': player_2.platform})
#
# conn.commit()
#
# # Player 3
# c.execute("INSERT INTO player VALUES (:discord, :apex, :platform)",
#           {'discord': player_3.discord_id, 'apex': player_3.apex_id, 'platform': player_3.platform})
#
# conn.commit()

# c.execute("DELETE FROM player")

# c.execute("SELECT * FROM player WHERE platform=:platform", {'platform': 'PS5'})
# c.execute("SELECT * FROM player")

# print(c.fetchall())

c.execute("ALTER TABLE player ALTER COLUMN discordID TEXT UNIQUE")

conn.commit()
conn.close()


