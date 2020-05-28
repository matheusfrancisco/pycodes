from intertools import chain, count

a = [1,2,3,4]
b = [6,7,8,9]
c = [10,11,12]


s = chain(a,b,c)


def _chain(*iters):
    for l in iters:
        for val in l:
            yield val


def _in(val, seq):
    """_contains_"""
    c = count()
    for el in seq:
        print(next(c))
        if el == val:
            return True
    return False


