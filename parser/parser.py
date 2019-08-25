from typing import Deque, Callable
from lexer import Token, TokenType, TokenGenerator
from functools import partial
from collections import deque
from .exceptions import NoMoreTokensException, IncorrectTokenException, ExcedingTokensException

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
consume_left_parenthesis: ConsumerFunction = partial(
    consume_token, TokenType.LEFT_PARENTHESIS)
consume_right_parenthesis: ConsumerFunction = partial(
    consume_token, TokenType.RIGHT_PARENTHESIS)
consume_operator: ConsumerFunction = partial(consume_token, TokenType.OPERATOR)
consume_variable: ConsumerFunction = partial(consume_token, TokenType.VARIABLE)


def parse_expression(token_list: TokenList) -> None:
    try:
        next_token: Token = token_list[0]
        if next_token.token_type is TokenType.LEFT_PARENTHESIS:
            consume_left_parenthesis(token_list)
            consume_operator(token_list)
            parse_expression(token_list)
            parse_expression(token_list)
            consume_right_parenthesis(token_list)
        elif next_token.token_type is TokenType.VARIABLE:
            consume_variable(token_list)
        else:
            consume_number(token_list)
    except IndexError:
        raise NoMoreTokensException from None


def parse_start(token_list: TokenList) -> None:
    consume_left_parenthesis(token_list)
    consume_operator(token_list)
    parse_expression(token_list)
    parse_expression(token_list)
    consume_right_parenthesis(token_list)


def parse(token_list: TokenList) -> None:
    parse_start(token_list)
    if not len(token_list) == 0:
        raise ExcedingTokensException
