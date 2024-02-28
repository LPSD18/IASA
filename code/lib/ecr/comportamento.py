from abc import ABC,abstractmethod

"""
Interface Comportamentos
"""
class Comportamento(ABC):


    """
    método abstract da classe Comportamento

    @param percepcao->Percepcao
    @return Accao
    """
    @abstractmethod
    def activar(self,percepcao):
        """
        Activar comportamento
        @param percepcao
        @return Accao
        """
