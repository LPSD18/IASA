from abc import ABC,abstractmethod

"""
Interface Estimulo
que irá ser utilizada de base por outras classes
"""
class Estimulo(ABC):

    """
    Interface estimulo de um comportamento
    """

    @abstractmethod
    def detetar(self,percepcao):
        """
        Detetar estimulo numa percepcao
        @param percepcao: percepcao a processar
        @return: intensidade do estimulo
        """