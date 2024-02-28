from mod.estado import Estado

'''
Classe EstadoValor
Herança de Estado
'''
class EstadoValor(Estado):
    '''
    Método construtor
    '''
    def __init__(self,valor):
        self.valor=valor
    
    
    '''
    Método id_valor
    '''
    def id_valor(self):
        return hash(self.valor)
    
