from enum import Enum
from typing import Mapping, Union


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


State = Union[TokenType, int]
Character = Union[str, ComplexCharacter]
START = 0
INTERMEDIATE = 1

automaton: Mapping[State, Mapping[Character, State]] = {
    START: {
        ComplexCharacter.DIGIT: TokenType.NUMBER,
        '$': INTERMEDIATE,
        '(': TokenType.LEFT_PARENTHESIS,
        ')': TokenType.RIGHT_PARENTHESIS,
        ComplexCharacter.OPERATOR: TokenType.OPERATOR
    },
    TokenType.NUMBER: {
        ComplexCharacter.DIGIT: TokenType.NUMBER
    },
    INTERMEDIATE: {
        ComplexCharacter.LETTER: TokenType.VARIABLE
    },
    TokenType.VARIABLE: {
        ComplexCharacter.LETTER: TokenType.VARIABLE,
        ComplexCharacter.DIGIT: TokenType.VARIABLE
    }
}
