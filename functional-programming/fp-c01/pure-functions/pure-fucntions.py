"""
Simple - do one thing and do it well

Limited number of arguments, ideal is zero
but if was 3 our more you need to refactoring this
functions.

Output depends on input

same input => same outputs
state not used or modified
no side effects

"""



def get_inits(ints, odd=True, even=True):
    """
     Function was  alot arguments,
     the ciclymatic complexity is high.
     Smell bad..

     Do it all function

    """
    if odd and even:
        return [i for i in ints]
    elif odd:
        return [i for i in ints if i % 2]
    elif even:
        return [i for i in ints if not i % 2]
    else:
        return []



"""
    Refactoring this fucntions to 3 more functions
"""

def get_even_ints(ints):
    return [integer for integer in ints if not integer % 2]


def get_odd_ints(ints):
    return [integer for integer in ints if integer % 2]


def get_all_ints(ints):
    """
      Return a new object if new id
    """
    return list(ints)
