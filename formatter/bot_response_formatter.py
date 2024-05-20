import discord
from formatter.color_picker import ColorPicker
from formatter.default_images import DefaultApexImg
current_season = 21


class BotResponseFormatter:
    @staticmethod
    def map_formatter(current_maps, embed):  # Creates Embed for Maps command
        # Mix tape Current
        ltm_current_map = current_maps.get("ltm", {}).get("current", {}).get("map", "Data currently unavailable")
        ltm_current_mode = current_maps.get("ltm", {}).get("current", {}).get("eventName", "Data currently unavailable")
        ltm_current_timer= current_maps.get("ltm", {}).get("current", {}).get("remainingTimer", "Data currently unavailable")
        #Mix tape next
        ltm_next_map = current_maps.get("ltm", {}).get("next", {}).get("map", "Data currently unavailable")
        ltm_next_mode = current_maps.get("ltm", {}).get("next", {}).get("eventName", "Data currently unavailable")

        embed.add_field(name="Mixtape Current:", value=f"{ltm_current_map} - {ltm_current_mode}", inline=True)
        embed.add_field(name="Mixtape Next:", value=f"{ltm_next_map} - {ltm_next_mode}", inline=True)
        embed.add_field(name="Time Remaining:", value=ltm_current_timer, inline=True)

        # Pubs BR
        br_current = current_maps.get("battle_royale", {}).get("current", {}).get("map", "Data currently unavailable")
        br_next_map = current_maps.get("battle_royale", {}).get("next", {}).get("map", "Data currently unavailable")
        br_map_timer = current_maps.get("battle_royale", {}).get("current", {}).get("remainingTimer", "Data currently unavailable")

        embed.add_field(name="BR Current:", value=br_current, inline=True)
        embed.add_field(name="BR Next:", value=br_next_map, inline=True)
        embed.add_field(name="Time Remaining:", value=br_map_timer, inline=True)
        # embed.add_field(name="\u200b", value="\u200b", inline=True)
        # Ranked BR
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

        embed.set_footer(text="Ranked Maps reset daily at 12PM CST.")
        return embed

    @staticmethod
    def crafter_formatter(crafting_rotation, embeds):  # Creates Embed for Crafter command

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
        p_global = player_stats.get("global", {})
        # Basic info name, level, platform
        platform = p_global.get("platform")  # PC, X1, PS5
        p_name = p_global.get("name")
        level = p_global.get("level")
        next_level = p_global.get("toNextLevelPercent")
        # Ranked Stats
        rank = p_global.get("rank")
        rank_score = rank.get("rankScore")
        player_rank = rank.get("rankName")
        player_div = rank.get("rankDiv")
        player_rank_image = rank.get("rankImg")
        rank_top_global = rank.get("ALStopPercentGlobal")
        # BattlePass
        battle_pass = p_global.get("battlepass").get("level")

        # New Sections - RealTime
        realtime = player_stats.get("realtime", {})
        # Lobby
        player_state = realtime.get("currentStateAsText")
        # Section - Legends
        legends = player_stats.get("legends", {})
        # Legends
        leg_name = legends.get("selected", {}).get("LegendName")
        selected_leg_img = legends.get("selected", {}).get("ImgAssets", {}).get("icon")
        

        color = ColorPicker.select(player_rank).upper()
        embed = discord.Embed(color=discord.Color.from_str(f'#{color}'),
                              title=f"__{p_name} - {platform} - LVL {level} - {current_season} BP {battle_pass}__")
        
        if player_state != "Offline":
            current_state = realtime.get("lobbyState")
            embed.description = f":green_circle: {player_state} - {current_state} - {leg_name}"
            embed.set_image(url=selected_leg_img)
        else:
            embed.description = f":red_circle: {player_state}"

        embed.set_thumbnail(url=player_rank_image)
        embed.thumbnail.width = 15
        embed.thumbnail.height = 15
        # Ranked Embeds
        embed.add_field(name=f"{current_season} Rank", value=f"{player_rank} {player_div}", inline=True)
        embed.add_field(name="RP", value=f"{rank_score}", inline=True)
        embed.add_field(name="Top Global", value=f"{rank_top_global}%", inline=True)
        embed.set_footer(text="Stats wrong? Equip the equivalent trackers in game, ie badges.")
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

    @staticmethod
    def predator_formatter(predator, embed):
        pred = predator.get("RP", {})
        # PC
        pc = pred.get("PC")
        pc_val = pc.get("val")
        pc_total = pc.get("totalMastersAndPreds")
        # PS4/5
        ps = pred.get("PS4")
        ps_val = ps.get("val")
        ps_total = ps.get("totalMastersAndPreds")
        # X1
        xbox = pred.get("X1")
        xbox_val = xbox.get("val")
        xbox_total = xbox.get("totalMastersAndPreds")
        # Switch
        switch = pred.get("SWITCH")
        switch_val = switch.get("val")
        switch_total = switch.get("totalMastersAndPreds")
        # Embed PC
        embed.add_field(name="PC", value=f"{pc_val} RP", inline=True)
        embed.add_field(name="Total Masters and Preds", value=f"{pc_total}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        # Embed PS
        embed.add_field(name="PS5", value=f"{ps_val} RP", inline=True)
        embed.add_field(name="Total Masters and Preds", value=f"{ps_total}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        # Embed X1
        embed.add_field(name="X1", value=f"{xbox_val} RP", inline=True)
        embed.add_field(name="Total Masters and Preds", value=f"{xbox_total}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        # Embed Switch
        embed.add_field(name="Switch", value=f"{switch_val} RP", inline=True)
        embed.add_field(name="Total Masters and Preds", value=f"{switch_total}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)

        return embed