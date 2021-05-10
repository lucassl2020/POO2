from Historico import Historico

class Conta():
    
    _qtd_de_contas = 0
    
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']
    
    def __init__(self, numero, titular, saldo, limite=1000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._qtd_de_contas += 1
        
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, novo_numero):
        self._numero = novo_numero
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        self._limite = valor
        
    def deposita(self, valor):
        if valor > 0 and self.saldo + valor <= self.limite:
            self._saldo += valor
            self._historico.add_transacao('Deposito', valor)
            return True
        return False
            
    def saca(self, valor):
        if valor > 0 and valor <= self.saldo:
            self._saldo -= valor
            self._historico.add_transacao('Saque', valor)
            return True
        return False
    
    def extrato(self):
        print(f'Numero - {self.numero}')
        print(f'Titular - {self.titular.nome}')
        print(f'Saldo - {self.saldo}')
        print(f'Limite - {self.limite}')
        self._historico.imprimir()
        print()
        
    def transfere(self, conta, valor):
        try:
            if self.saca(valor):
                if conta.deposita(valor):
                    self._historico.add_transacao(f'Transferencia para {conta.titular.nome}', valor)
                    return True
                else:
                    self.deposita(valor)
            return False
        except:
            return False
    
    @staticmethod
    def qtd_de_contas():
        return Conta._qtd_de_contas
