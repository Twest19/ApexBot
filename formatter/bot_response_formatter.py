import discord
from formatter.color_picker import ColorPicker


class BotResponseFormatter:
    @staticmethod
    def map_formatter(current_maps):  # Creates Embed for Maps command
        embed = discord.Embed(color=0xff0000, title="Map Rotation", description="Apex Legends current map rotation")
        embed.set_thumbnail(url="https://i.imgur.com/pdS1ONm.png")

        try:
            ranked_map = current_maps['ranked']['current']['map']
            ranked_image_url = current_maps['ranked']['current']['asset']

            ranked_map_timer = current_maps['ranked']['current']['remainingTimer']
            ranked_next = current_maps['ranked']['next']['map']

            embed.add_field(name="Ranked:", value=f"{ranked_map}", inline=True)
            embed.add_field(name="Ranked Next:", value=f"{ranked_next}", inline=True)
            embed.add_field(name="Time Remaining:", value=f"{ranked_map_timer}", inline=True)
            embed.set_image(url=f"{ranked_image_url}")
        except KeyError:
            embed.add_field(name="Ranked:", value="Data currently unavailable", inline=True)
            embed.add_field(name="Ranked Next:", value="Data currently unavailable", inline=True)
            embed.add_field(name="Time Remaining:", value="Data currently unavailable", inline=True)

        try:
            br_current = current_maps['battle_royale']['current']['map']
            br_next_map = current_maps['battle_royale']['next']['map']

            embed.add_field(name="BR Current:", value=f"{br_current}", inline=True)
            embed.add_field(name="BR Next:", value=f"{br_next_map}", inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=True)
        except KeyError:
            embed.add_field(name="BR Current:", value="Data currently unavailable", inline=True)
            embed.add_field(name="BR Next:", value="Data currently unavailable", inline=True)

        return embed

    @staticmethod
    def crafter_formatter(crafting_rotation):  # Creates Embed for Crafter command
        embed_title = discord.Embed(color=0x098d8d,
                                    title="Crafting Rotation",
                                    description="Apex Legends current crafting rotation")

        embeds = [embed_title]

        if crafting_rotation is not None:
            for bundle in crafting_rotation[:2]:
                for item in bundle["bundleContent"]:
                    hex_color = item["itemType"]["rarityHex"]

                    # item_name = item['itemType']['name']
                    item_rarity = item["itemType"]["rarity"]
                    item_image = item["itemType"]["asset"]
                    item_cost = item["cost"]

                    if item_rarity == "Epic":
                        item_rarity = item_rarity.ljust(16)
                    elif item_rarity == "Rare":
                        item_rarity = item_rarity.ljust(15)

                    embed = discord.Embed(color=discord.Color.from_str(f"{hex_color}"),
                                          description=None,
                                          title=f"{item_rarity}\nCost: {item_cost} ")

                    embed.set_thumbnail(url=item_image)
                    # embed.set_image(url=item_image)
                    embed.image.width = 10
                    embed.image.height = 10
                    embeds.append(embed)
        else:
            embed_title.add_field(name="**Error**",
                                  value="Crafting rotation, currently unavailable. "
                                        "Check `/server` for potential Apex Legends issues and try again later.",
                                  inline=False)

        return embeds

    @staticmethod
    def player_stats_formatter(player_stats):  # Creates Embed for Stats command
        p_global = player_stats["global"]
        platform = p_global["platform"]  # PC, X1, PS5
        level = p_global["level"]
        p_name = p_global["name"]
        next_level = p_global["toNextLevelPercent"]

        rank = p_global["rank"]
        player_rank_image = rank["rankImg"]
        player_rank = rank["rankName"]
        player_div = rank["rankDiv"]
        rank_score = rank["rankScore"]

        # ban = p_global["bans"]
        # ban_info = ban["isActive"]
        # ban_seconds = ban["remainingSeconds"]
        # ban_last = ban["last_banReason"]
        # ban_text = "Ban: "

        color = ColorPicker.select(player_rank).upper()

        # if ban_info is True:
        #     ban_text += f"{ban_last} {ban_seconds}s remaining "
        # else:
        #     ban_text += f"NONE  Last Ban: {ban_last}"

        embed = discord.Embed(color=discord.Color.from_str(f'#{color}'),
                              title=f"Stats for {p_name} - {platform}",
                              description=None)

        embed.set_thumbnail(url=player_rank_image)
        embed.thumbnail.width = 10
        embed.thumbnail.height = 10

        embed.add_field(name="Level", value=f"{level}", inline=True)
        embed.add_field(name=f"To Next", value=f"{next_level}%", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)

        embed.add_field(name="S16 Rank", value=f"{player_rank} {player_div}", inline=True)
        embed.add_field(name="RP", value=f"{rank_score}", inline=True)

        # embed.set_footer(text=ban_text)

        return embed

    @staticmethod
    def news_formatter(game_news):  # Creates Embed for News command

        if game_news is not None and "title" in game_news:
            title = game_news["title"]
            image = game_news["img"]
            description = game_news["short_desc"]

            embed = discord.Embed(color=discord.Color.dark_red(),
                                  title=title,
                                  description=description)

            embed.set_image(url=image)
            return embed
        else:
            embed = discord.Embed(color=discord.Color.dark_red(),
                                  title="Apex News",
                                  description="News currently Unavailable")
            embed.set_thumbnail(url="https://i.imgur.com/pdS1ONm.png")
            return embed
