from collections import ChainMap
from os import environ
from argparse import ArgumentParser

#Unir dois dict

#a = {1:'a', 2:'b', 3:'c'}
#b = {2:'x', 3:'z'}

# Resposta no primeiro, dict com chain 
#c = ChainMap(a,b)


defaults = {'cor': 'vermelho','user':'Convidado'}
parser = ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--cor')

namespace = parse.parse_args()

linha_comando = {k:v for k, v in vars(namespace).items() if v}
comb = ChainMap(linha_comando, environ, defaults)

print(comb['cor'])
print(comb['user'])

