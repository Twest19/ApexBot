import os
import requests
from apex_error import ApexError


class ApexAPI:
    def __init__(self):
        self.base_url = 'https://api.mozambiquehe.re/'
        self.key = os.environ.get('LEGEND_KEY')
        self.api_error = ApexError()

    def player_data(self, player_name, platform):
        player_stats_url = f"{self.base_url}bridge?auth={self.key}&player={player_name}&platform={platform}"
        response = requests.get(player_stats_url)

        return self.__get_code_response(response)

    def uid_data(self, player_uid, platform):
        player_stats_url = f"{self.base_url}bridge?auth={self.key}&uid={player_uid}&platform={platform}"
        response = requests.get(player_stats_url)

        return self.__get_code_response(response)

    def map_rotation(self):
        current_rotation = f"{self.base_url}maprotation?auth={self.key}&version=2"
        response = requests.get(current_rotation)

        return self.__get_code_response(response)

    def predator(self):
        predator = f"{self.base_url}predator?auth={self.key}"
        response = requests.get(predator)

        return self.__get_code_response(response)

    # def store_info(self): # MUST BE WHITELISTED ON DISCORD SERVER
    #     store = f"{self.base_url}store?auth={self.key}"
    #     response = requests.get(store)
    #
    #     return self.__get_code_response(response)

    def crafting_rotation(self):
        crafting = f"{self.base_url}crafting?auth={self.key}"
        response = requests.get(crafting)

        return self.__get_code_response(response)

    def game_news(self):
        news = f"{self.base_url}news?auth={self.key}"
        response = requests.get(news)

        return self.__get_code_response(response)

    def server_status(self):
        status = f"{self.base_url}servers?auth={self.key}"
        response = requests.get(status)

        return self.__get_code_response(response)

    def name_to_uid(self, player_name, platform):
        uid_info = f"{self.base_url}nametouid?auth={self.key}&player={player_name}&platform={platform}"
        response = requests.get(uid_info)
        return self.__get_code_response(response)

    def __get_code_response(self, response):
        code = response.status_code

        if code == 200:
            return response.json()
        else:
            return f"Request failed with status code {code}: {self.api_error.meaning(code)}"
