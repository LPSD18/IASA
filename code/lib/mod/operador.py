from abc import ABC, abstractmethod

'''
Classe abstrata
Representa uma acção (transformação de estado) 
'''
class Operador(ABC):


    '''
    Método que aplica a ação necessária para o estado atual
    @param estado
    '''
    @abstractmethod
    def aplicar(estado):
        
        '''
        '''

    '''
    Métood que verifica o custo da transição de um estado para o sucessor
    @param estado
    @param est_sucessor
    '''    
    @abstractmethod
    def custo(estado, est_sucessor):
        '''
        '''
