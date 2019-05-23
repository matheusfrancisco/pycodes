"""

Decorador simples

"""
def decorator_(func):
    def interna(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x,y)
        else:
            raise ValueError('Insira somente inteiros')
    return interna


"""

decorador -> interna -> funcao decorada

"""

@decorator_
def soma(x,y):
    return x + y



print(soma(2,2))
