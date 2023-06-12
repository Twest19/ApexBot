

class Player:
    def __init__(self, discord_id, apex_id, platform):
        self.discord_id = discord_id
        self.apex_id = apex_id
        self.platform = platform

    @staticmethod
    def _validate_and_strip(value):
        return str(value).strip()

    @property
    def discord_id(self):
        return self._discord_id

    @property
    def platform(self):
        return self._platform

    @property
    def apex_id(self):
        return self._apex_id

    @discord_id.setter
    def discord_id(self, user_id):
        self._discord_id = self._validate_and_strip(user_id)

    @platform.setter
    def platform(self, platform):
        self._platform = self._validate_and_strip(platform)

    @apex_id.setter
    def apex_id(self, user_id):
        self._apex_id = self._validate_and_strip(user_id)
