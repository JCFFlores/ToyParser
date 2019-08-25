from lexer import Token

class NoMoreTokensException(Exception):
    pass

class IncorrectTokenException(Exception):


    def __init__(self, token: Token):
        super().__init__(f'Invalid expression on token: "{token.value}"')
