def is_digit(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_operator(s: str) -> bool:
    return s in "+-*/"
