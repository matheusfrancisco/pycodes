

def isPair(val: int) -> bool:
    """
    This function check whether the number is even

    Arg:
        - val : Value is int number
    """
    if isinstance(val, int) or isinstance(val, float):
        return True if val % 2 == 0 else False
    else:
        return False


