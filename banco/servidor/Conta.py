from Historico import Historico

class Conta():
    
    _qtd_de_contas = 0
    
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_senha']
    
    def __init__(self, titular, senha,  saldo=0, limite=1000):
        Conta._qtd_de_contas += 1
        self._numero = str(Conta._qtd_de_contas)
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._senha = senha
        
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

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        self._limite = valor

    @property
    def senha(self):
        return self._senha

    @property
    def historico(self):
        return self._historico
    
        
    def deposita(self, valor):
        try:
            if valor > 0 and self.saldo + valor <= self.limite:
                self._saldo += valor
                self._historico.add_transacao('Deposito', valor)
                return True
            return False
        except:
            return False
                
    def saca(self, valor):
        try:
            if valor > 0 and valor <= self.saldo:
                self._saldo -= valor
                self._historico.add_transacao('Saque', valor)
                return True
            return False
        except:
            return False
    
    def extrato(self):
        historico = ''
        transacoes = self._historico.transacoes

        for transacao in transacoes:
            historico += transacao

        return historico
        
    def transfere(self, conta, valor):
        try:
            if self != conta:
                if valor > 0 and valor <= self.saldo:
                    self._saldo -= valor
                    if valor > 0 and conta.saldo + valor <= conta.limite:
                        conta.saldo += valor 
                        self.historico.add_transacao(f'Transferencia para {conta.titular.nome}', valor)
                        conta.historico.add_transacao(f'Transferencia recebida de {self.titular.nome}', valor)
                        return True
            return False
        except:
            return False
    
    @staticmethod
    def qtd_de_contas():
        return Conta._qtd_de_contas
