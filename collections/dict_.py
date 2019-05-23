
"""
dict.items()
dict.values()
dict.keys()
"""

def _dict(**kwargs):
    return kwargs


digitos = [0,1,2,3]
strings = ['zero', 'um', 'dois', 'três']

numeros = {digito:string for digito, string in zip(digitos, strings)}


class Pessoa:
    def __init__(self,nome):
        self.nome =nome
    def __hash__(self):
        return hash(self.nome)

xico = Pessoa('Xico')
xicao = Pessoa('Xico')


