from lexer import tokenize, Token, TokenType, InvalidTokenException, TokenGenerator
from typing import List
import pytest


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
            ')'),
    ]
    assert_tokenize(token_list, input_string)


def test_long_token():
    input_string: str = "(- 1544 8693)"
    token_list: List[Token] = [
        Token(
            TokenType.LEFT_PARENTHESIS,
            '('),
        Token(
            TokenType.OPERATOR,
            '-'),
        Token(
            TokenType.NUMBER,
            '1544'),
        Token(
            TokenType.NUMBER,
            '8693'),
        Token(
            TokenType.RIGHT_PARENTHESIS,
            ')'),
    ]
    assert_tokenize(token_list, input_string)


def test_invalid_variable():
    input_string: str = "$1234"
    with pytest.raises(InvalidTokenException):
        list(tokenize(input_string))


def test_invalid_number():
    input_string: str = "12a5"
    with pytest.raises(InvalidTokenException):
        list(tokenize(input_string))


def test_nested_expression():
    input_string: str = "(* (/ 4 2) 1)"
    token_list: List[Token] = [
        Token(
            TokenType.LEFT_PARENTHESIS,
            '('),
        Token(
            TokenType.OPERATOR,
            '*'),
        Token(
            TokenType.LEFT_PARENTHESIS,
            '('),
        Token(
            TokenType.OPERATOR,
            '/'),
        Token(
            TokenType.NUMBER,
            '4'),
        Token(
            TokenType.NUMBER,
            '2'),
        Token(
            TokenType.RIGHT_PARENTHESIS,
            ')'),
        Token(
            TokenType.NUMBER,
            '1'),
        Token(
            TokenType.RIGHT_PARENTHESIS,
            ')'),
    ]
    assert_tokenize(token_list, input_string)
