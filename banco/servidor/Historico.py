class Historico():
    
    def __init__(self):
        self._transacoes = []
        
    def add_transacao(self, transacao, valor):
        try:
            self._transacoes.append(transacao + '  ' + str(valor) + '\n\n')
            return True
        except:
            return False

    @property
    def transacoes(self):
        return self._transacoes
