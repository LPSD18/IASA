from abc import ABC


'''
Classe abstrata
'''

class ModeloPlan(ABC):
    
    
    def obter_estado(self):
        '''
        return do atributo estado
        '''

    def obter_estados(self):
        '''
        return de uma lista com estados
        '''
    
    def obter_operadores(self):
        '''
        return de uma lista com operadores
        '''