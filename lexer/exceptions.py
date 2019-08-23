class InvalidTokenException(Exception):
    def __init__(self, token: str):
        super().__init__(f'Error while processing "{token}"')
