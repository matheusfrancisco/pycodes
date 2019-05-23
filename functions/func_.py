"""

1- Functions named (def)
2- Functions anonimous (lambda)
3- Functions class (class)

"""

def named_sum(x,y):
    return x + y

anonymous = lambda x, y: x + y


class classe_sum:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __call__(self):
        return self.x + self.y


