from collections import deque


class Pilha:
    def __init__(self):
        self.lista = deque()

    def insere(self, val):
            self.lista.append(val)

    def remove(self, val):
        return self.lista.pop()

    def __repr__(self):
        return 'Lista [{}]'.format(', '.join(str(x) for x in self.lista))


