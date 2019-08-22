def is_digit(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False
