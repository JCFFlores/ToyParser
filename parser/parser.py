from typing import Deque
from lexer import Token, TokenType
from .exceptions import NoMoreTokensException, IncorrectTokenException

def consume_token(token_type: TokenType, token_list: Deque[Token]) -> None:
    try:
        token: Token = token_list.popleft()
        if not token.token_type == token_type:
            raise IncorrectTokenException(token)
    except IndexError:
        raise NoMoreTokensException from None
