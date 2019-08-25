from lexer import Token, TokenType
from parser import parse, TokenList, IncorrectTokenException, NoMoreTokensException, ExcedingTokensException
from collections import deque


def test_basic_expression():
    token_list: TokenList = deque([
        Token(
            TokenType.LEFT_PARENTHESIS,
            '('),
        Token(
            TokenType.OPERATOR,
            '+'),
        Token(
            TokenType.NUMBER,
            '1'),
        Token(
            TokenType.VARIABLE,
            '$var'),
        Token(
            TokenType.RIGHT_PARENTHESIS,
            ')'),
    ])
    parse(token_list)
