"""
closure
"""

def externa(id):
    dic = {'pt': 'Olá'}

    def interna(nome):
        print('{} {}'.format(dic[id], nome))
    return interna

func = externa('pt')

fun('Matheus')
