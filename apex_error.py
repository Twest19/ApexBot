
class ApexError:
    def __init__(self):
        self.__error_dict = {
            '400': 'Try again in a few minutes.',
            '403': 'Unauthorized / Unknown API key.',
            '404': 'The player could not be found.',
            '405': 'External API error.',
            '410': 'Unknown platform provided.',
            '429': 'Rate limit reached.',
            '500': 'Internal error.',
        }

    def meaning(self, code):
        if code in self.__error_dict:
            return self.__error_dict[f'{code}']
        else:
            return self.__error_dict[f'404']
