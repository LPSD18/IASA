import abc
from abc import ABC, abstractmethod

'''
Interface Heuristica
heurísticas – métodos expeditos de estimação de valores ou de resolução de problemas
'''
class Heuristica(ABC):
    '''
    Custo mínimo do nó n até ao objectivo (percurso óptimo)
    '''
    @abstractmethod
    def h(self,estado):
        # return estado.id_valor()
        '''
        '''