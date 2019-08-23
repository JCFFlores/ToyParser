from lexer import tokenize, Token, TokenType, InvalidTokenException, TokenGenerator
from typing import List


def assert_tokenize(token_list: List[Token], input_string: str) -> None:
    assert token_list == list(tokenize(input_string))


def test_sum():
    input_string: str = "(+ 1 2)"
    token_list: List[Token] = [
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
            TokenType.NUMBER,
            '2'),
        Token(
            TokenType.RIGHT_PARENTHESIS,
            ')')]
    assert_tokenize(token_list, input_string)
