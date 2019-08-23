from enum import Enum
from typing import Mapping, Union, Generator, Callable
from dataclasses import dataclass
from functools import partial
from .exceptions import InvalidTokenException
from .utils import is_digit, is_operator, is_letter


class TokenType(Enum):
    NUMBER = 1
    VARIABLE = 2
    LEFT_PARENTHESIS = 3
    RIGHT_PARENTHESIS = 4
    OPERATOR = 5


class ComplexCharacter(Enum):
    DIGIT = 1
    LETTER = 2
    OPERATOR = 3


class NonTerminalState(Enum):
    START = 1
    VARIABLE_INTERMEDIATE = 2


@dataclass
class Token:
    token_type: TokenType
    vaue: str


State = Union[TokenType, NonTerminalState]
Character = Union[str, ComplexCharacter]
Automata = Mapping[State, Mapping[Character, State]]
TokenGenerator = Generator[Token, None, None]

automata: Automata = {
    NonTerminalState.START: {
        ComplexCharacter.DIGIT: TokenType.NUMBER,
        '$': NonTerminalState.VARIABLE_INTERMEDIATE,
        '(': TokenType.LEFT_PARENTHESIS,
        ')': TokenType.RIGHT_PARENTHESIS,
        ComplexCharacter.OPERATOR: TokenType.OPERATOR,
        ' ': NonTerminalState.START,
    },
    TokenType.NUMBER: {
        ComplexCharacter.DIGIT: TokenType.NUMBER
    },
    NonTerminalState.VARIABLE_INTERMEDIATE: {
        ComplexCharacter.LETTER: TokenType.VARIABLE
    },
    TokenType.VARIABLE: {
        ComplexCharacter.LETTER: TokenType.VARIABLE,
        ComplexCharacter.DIGIT: TokenType.VARIABLE
    }
}


def convert_character(s: str) -> Character:
    if is_digit(s):
        return ComplexCharacter.DIGIT
    if is_letter(s):
        return ComplexCharacter.LETTER
    if is_operator(s):
        return ComplexCharacter.OPERATOR
    return s


def token_or_exception(state: State, token: str) -> Token:
    if isinstance(state, TokenType):
        return Token(state, token)
    raise InvalidTokenException(token) from None


def tokenize_helper(automata: Automata,
                    text: str) -> TokenGenerator:
    token: str = ""
    current_state: State = NonTerminalState.START
    for current_char, next_char in zip(text, text[1:] + ' '):
        current_character: Character = convert_character(current_char)
        next_character: Character = convert_character(next_char)
        try:
            next_state: State = automata[current_state][current_character]
            token += current_char
            current_state = next_state
            automata[current_state][next_character]
        except KeyError:
            yield token_or_exception(current_state, token.strip())
            token = ""
            current_state = NonTerminalState.START


tokenize: Callable[[str], TokenGenerator] = partial(tokenize_helper, automata)
