from abc import ABC, abstractmethod


'''
Classe abstrata
-Representa uma situação (configuração) na resolução de um problema
– Identificação única

'''

class Estado(ABC):

    '''
    Método abstract
    este método deve gerar um identificador unico de estado

    @return int
    '''
    @abstractmethod
    def id_valor(self):
        '''
        '''

    '''
    Método __hash__ --> int – Define identificação única de um objecto
    '''
    def __hash__(self):
        return self.id_valor()
        
    '''
    Método que verifica se um estado é igual a outro estado
    '''
    def __eq__(self,other):
        return self.__hash__() == other.__hash__()
        '''
        '''
