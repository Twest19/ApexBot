import discord
from formatter.bot_response_formatter import BotResponseFormatter


class LinkButtons(discord.ui.View):
    def __init__(self, game_news, index, embed):
        super().__init__(timeout=None)
        self.game_news = game_news
        self.current_index = index
        self.embed = embed
        print("Index = " + self.game_news[self.current_index]["link"])
        self.link_button = discord.ui.Button(label="Link", url=self.game_news[self.current_index]["link"],
                                             style=discord.ButtonStyle.link)
        self.add_item(self.link_button)

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.primary, custom_id="prev_button")
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_index > 0:
            self.current_index -= 1
            embed_resp = BotResponseFormatter.news_formatter(game_news=self.game_news[self.current_index],
                                                             embed=self.embed)
            self.link_button.url = self.game_news[self.current_index]["link"]
            await interaction.response.edit_message(embed=embed_resp, view=self)

    @discord.ui.button(label="Next", style=discord.ButtonStyle.primary, custom_id="next_button")
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_index < len(self.game_news) - 1:
            self.current_index += 1
            print(self.current_index)
            embed = BotResponseFormatter.news_formatter(game_news=self.game_news[self.current_index],
                                                        embed=self.embed)
            self.link_button.url = self.game_news[self.current_index]["link"]
            print(self.link_button.url)
            await interaction.response.edit_message(embed=embed, view=self)
