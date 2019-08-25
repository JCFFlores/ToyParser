from lexer import Token, TokenType
from parser import parse, TokenList, IncorrectTokenException, NoMoreTokensException, ExcedingTokensException
from collections import deque
import pytest


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


def test_nested_expression():
    token_list: TokenList = deque([
        Token(
            TokenType.LEFT_PARENTHESIS,
            '('),
        Token(
            TokenType.OPERATOR,
            '-'),
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
        Token(
            TokenType.NUMBER,
            '3'),
        Token(
            TokenType.RIGHT_PARENTHESIS,
            ')'),
    ])
    parse(token_list)


def test_incomplete_expression():
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
    ])
    with pytest.raises(NoMoreTokensException):
        parse(token_list)


def test_bad_expression():
    token_list: TokenList = deque([
        Token(
            TokenType.LEFT_PARENTHESIS,
            '('),
        Token(
            TokenType.NUMBER,
            '1'),
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
    with pytest.raises(IncorrectTokenException):
        parse(token_list)
