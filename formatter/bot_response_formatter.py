import discord


class BotResponseFormatter:
    @staticmethod
    def map_formatter(current_maps):
        br_current = current_maps['battle_royale']['current']['map']
        br_next_map = current_maps['battle_royale']['next']['map']

        ranked_map = current_maps['ranked']['current']['map']
        ranked_image_url = current_maps['ranked']['current']['asset']
        ranked_map_timer = current_maps['ranked']['current']['remainingTimer']
        ranked_next = current_maps['ranked']['next']['map']

        embed = discord.Embed(color=0xff0000, title="Map Rotation", description="Apex Legends current map rotation")
        embed.set_thumbnail(url="https://imgur.com/IzjT3Xh")
        embed.add_field(name="Ranked:", value=f"{ranked_map}", inline=True)
        embed.add_field(name="Ranked Next:", value=f"{ranked_next}", inline=True)
        embed.add_field(name="Time Remaining:", value=f"{ranked_map_timer}", inline=True)
        embed.add_field(name="BR Current:", value=f"{br_current}", inline=True)
        embed.add_field(name="BR Next:", value=f"{br_next_map}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.set_image(url=f"{ranked_image_url}")

        return embed

    @staticmethod
    def crafter_formatter(crafting_rotation):
        embed_title = discord.Embed(color=0x098d8d,
                                    title="Crafting Rotation",
                                    description="Apex Legends current crafting rotation")

        embeds = [embed_title]

        for bundle in crafting_rotation[:2]:
            for item in bundle['bundleContent']:
                hex_color = item['itemType']['rarityHex']
                print("COLOR = " + hex_color)
                # item_name = item['itemType']['name']
                item_rarity = item['itemType']['rarity']
                item_image = item['itemType']['asset']
                item_cost = item['cost']

                if item_rarity == 'Epic':
                    item_rarity = item_rarity.ljust(16)

                embed = discord.Embed(color=discord.Color.from_str(f'{hex_color}'),
                                      description="\u200b",
                                      title=f"{item_rarity}\nCost: {item_cost} ")

                embed.set_thumbnail(url=item_image)
                # embed.set_image(url=item_image)
                embed.image.width = 10
                embed.image.height = 10
                embeds.append(embed)

        return embeds
