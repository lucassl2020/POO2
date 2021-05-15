class Cliente():
    
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        
    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
    	return self._sobrenome
    

    @property
    def cpf(self):
        return self._cpf
