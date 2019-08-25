from typing import Deque, Callable
from lexer import Token, TokenType
from .exceptions import NoMoreTokensException, IncorrectTokenException

TokenList = Deque[Token]
ConsumerFunction = Callable[[TokenList], None]

def consume_token(token_type: TokenType, token_list: TokenList) -> None:
    try:
        token: Token = token_list.popleft()
        if not token.token_type == token_type:
            raise IncorrectTokenException(token)
    except IndexError:
        raise NoMoreTokensException from None


consume_number: ConsumerFunction = partial(consume_token, TokenType.NUMBER)
consume_left_parenthesis: ConsumerFunction = partial(consume_token, TokenType.LEFT_PARENTHESIS)
consume_right_parenthesis: ConsumerFunction = partial(consume_token, TokenType.RIGHT_PARENTHESIS)
consume_operator: ConsumerFunction = partial(consume_token, TokenType.OPERATOR)
consume_variable: ConsumerFunction = partial(consume_token, TokenType.VARIABLE)
