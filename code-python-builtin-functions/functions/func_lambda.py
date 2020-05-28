

'f(x) | x + 2'
'usar um valor'

#print(list(map(lambda x: x+ 2, [1,2,3])))

#lambda x: x + 2


soma = lambda x: x +2
print(soma)

#func class
class classe_soma:
    def __call__(self, x, y):
        return x + y

#need to instanced class
#print(classe_soma(2,2))

