# from intertools import chain
from pprint import pprint

A = list(range(2,11))+ 'Q J K A'.split()
B = ['E', 'O', 'P', 'C']

baralho = [(carta, naipe) for carta in A for naipe in B]
pprint(baralho)

baralho = {(carta, naipe) for carta in A for naipe in B if carta == 'K'}
pprint(baralho)

#from itertools import combinations
#list(combinations([1,2,3,4,5], 3))
