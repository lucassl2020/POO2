class Historico():
    
    def __init__(self):
        self._transacoes = {}
        
    def add_transacao(self, transacao, valor):
        try:
            self._transacoes[transacao] = valor
            return True
        except:
            return False
        
    def imprimir(self):
        print('Historico:')
        for key in self._transacoes.keys():
            print(f'- {key} - {self._transacoes[key]}')
