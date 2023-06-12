import sqlite3
from sqlite3 import IntegrityError
from player import Player

# conn = sqlite3.connect('the_apex_bot.db')
#
# c = conn.cursor()
#
# c.execute("""CREATE TABLE player (
#             discordID TEXT UNIQUE,
#             apexID TEXT,
#             platform TEXT
#             )""")
# player_1 = Player(1, 2, "X1")
# player_2 = Player(123, 31235, "PS5")
# player_3 = Player(1234, 646, "PC")


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
#
# print(c.fetchall())
#
# conn.commit()
# conn.close()


