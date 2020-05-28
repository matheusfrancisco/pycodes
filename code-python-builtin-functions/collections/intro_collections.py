from functools import total_ordering
from operator import attrgetter
from abc import ABCMeta, abstractmethod
import numpy as np
import array as arr

class ContaCorrent:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.sado += valor

    def __str__(self):
        return "[>> Codigo {} Saldo {}<<]".format(self.codigo, self.sado)


conta_mat = ContaCorrent(123)
conta_mat.deposita(100)

conta_xico = ContaCorrent(123)
conta_xico.deposita(100)

contas = [conta_mat, conta_xico]


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self.valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>> Codigo {} Saldo {}<<]".format(self._codigo, self._sado)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -=2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass



conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)


arr.array('d', [1, 3.5])
numeros = np.array([1, 3.5])


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContraSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>> Codigo {} Saldo {}<<]".format(self._codigo, self._sado)


class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(31)
conta2 = ContaSalario(31)
print(conta1 == conta2)
print(conta1)

contas = [conta1, conta2]

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

for conta in sorted(contas):
    print(conta)

