from apex_error import ApexError


class ApexException(Exception):
    def __init__(self, code, *args, **kwargs):
        self.code = code
        self.message = ApexError().meaning(code)
        super().__init__(self.message, *args, **kwargs)