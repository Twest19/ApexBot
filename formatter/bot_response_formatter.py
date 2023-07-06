import discord
from formatter.color_picker import ColorPicker
from formatter.default_images import DefaultApexImg


class BotResponseFormatter:
    @staticmethod
    def map_formatter(current_maps, embed):  # Creates Embed for Maps command

        ranked_map = current_maps.get("ranked", {}).get("current", {}).get("map", "Data currently unavailable")
        ranked_image_url = current_maps.get("ranked", {}).get("current", {}).get("asset", None)
        ranked_map_timer = current_maps.get("ranked", {}).get("current", {}).get("remainingTimer",
                                                                                 "Data currently unavailable")
        ranked_next = current_maps.get("ranked", {}).get("next", {}).get("map", "Data currently unavailable")

        embed.add_field(name="Ranked:", value=ranked_map, inline=True)
        embed.add_field(name="Ranked Next:", value=ranked_next, inline=True)
        embed.add_field(name="Time Remaining:", value=ranked_map_timer, inline=True)
        if ranked_image_url:
            embed.set_image(url=ranked_image_url)

        br_current = current_maps.get("battle_royale", {}).get("current", {}).get("map", "Data currently unavailable")
        br_next_map = current_maps.get("battle_royale", {}).get("next", {}).get("map", "Data currently unavailable")

        embed.add_field(name="BR Current:", value=br_current, inline=True)
        embed.add_field(name="BR Next:", value=br_next_map, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        return embed

    @staticmethod
    def crafter_formatter(crafting_rotation, embed_title):  # Creates Embed for Crafter command

        embeds = [embed_title]

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
                embed.image.width = 10
                embed.image.height = 10
                embeds.append(embed)

        return embeds

    @staticmethod
    def player_stats_formatter(player_stats):  # Creates Embed for Stats command
        print(player_stats)
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

        embed.add_field(name="S17 Rank", value=f"{player_rank} {player_div}", inline=True)
        embed.add_field(name="RP", value=f"{rank_score}", inline=True)

        # embed.set_footer(text=ban_text)

        return embed

    @staticmethod
    def news_formatter(game_news, embed):  # Creates Embed for News command
        # Api indexing
        title = game_news.get("title")
        image = game_news.get("img", None)
        description = game_news.get("short_desc")
        # Embed
        embed.title = title
        embed.description = description
        if image is not None:
            embed.set_image(url=image)
        return embed

    @staticmethod
    def server_formatter(server_status, embed):

        us_central = server_status.get("Origin_login", {}).get("US-Central", {}).get("Status", "Not Available.")
        accounts = server_status.get("EA_accounts", {}).get("US-Central", {}).get("Status", "Not Available.")
        playstation = server_status.get("otherPlatforms", {}).get("Playstation-Network", {}).get("Status",
                                                                                                 "Not Available.")
        xbox = server_status.get("otherPlatforms", {}).get("Xbox-Live", {}).get("Status", "Not Available.")

        embed.add_field(name="**Origin:**", value="\u200b", inline=True)
        embed.add_field(name="**US-Central**", value=f"{us_central}", inline=False)
        embed.add_field(name="**Xbox**", value=f"{xbox}", inline=False)
        embed.add_field(name="**Playstation**", value=f"{playstation}", inline=False)
        embed.add_field(name="**EA Accounts**", value=f"{accounts}", inline=False)

        return embed
