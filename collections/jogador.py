from collections import namedtuple

#jogador = namedtuple('Jogador', 'nome time camisa n')

#n = namedtuple('ABC', 'slot1 slot2 slot3')

carta = namedtuple('Carta', 'naipe valor')

baralho = [carta(naipe, valor) for naipe in naipes for valor in valores]



