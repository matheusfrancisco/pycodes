'''
Functors, funções, sequências e lazy evaluation
map
filter
list comp
dict comp
set comp
gen expr

Functor
Associa para cada objeto x em um conjunto C um objeto F(x) em um conjunto D
F(x)
C ={1,2,3}
F(1) = 2
F(2) = 3
F(3) = 4

(lambda x: x+2)(2)


lazy evaluation - Avaliação preguiçosa
São retornos (as vezes de funções) que só são computados quando chamados 
Comumente são chamados pelo método

Map
f(x), aplicada a uma sequência S, retorna uma nova sequências
map(f,S)-> map(lambda x :x*2, [1,2,3]) -> [2,4,6]


Filter
filter(f,S) -> Z => filter(lambda x: x>2, [1,2,3])-> [3]
Aqui o operdador lógico é usado
retorna apartir do true

filter(lambda x:x>2, [1,2,3,4,5,6])->[3,4,5,6]

'''

'''
List --> list(map(func, iter)) --> [func(x) for x in iter]
Gen --> map(func, iter) --> (func(x)  for x in iter)
Set --> set(map(func, iter)) --> {func(x) for x in iter}
Dict --> dict(map(func, iter)) --> {func(x):func(y) for x,y in iter}


filters

list list(filter(func,iter)) --> [x for x in iter if func(x)]
gen filter(func,iter) --> (x for x in iter if func(x))
set  set(filter(func,iter)) {x for in iter if func(x)}
dict dict(filter(func,iter))  {x:y for x,y in iter if func(x) and func(y)}


'''
