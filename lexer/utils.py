import re

def is_digit(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_operator(s: str) -> bool:
    return s in "+-*/"

regex = re.compile('[a-zA-Z]')

def is_letter(s: str) -> bool:
    return regex.fullmatch(s) is not None
