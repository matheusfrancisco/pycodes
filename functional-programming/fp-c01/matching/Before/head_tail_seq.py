from itertools import islice, chain, tee
def head(it):
    try:
        return next(islice(it, 0, 1))

    except StopIteration:
        return (i for i in [])
        
def tail(it):
    try:
        head = next(islice(it, 0, 1))
        return chain((head,), it)

    except StopIteration:
        return (i for i in [])

g = (i for i in range(10) if i%2)
print(head(g))
print([i for i in tail(g)])