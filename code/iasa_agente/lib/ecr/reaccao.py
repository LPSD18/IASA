from .estimulo import Estimulo
from .resposta import Resposta
from .comportamento import Comportamento

"""
Classe Reaccao
"""

class Reaccao:

    """
    método construtor da classe Reaccao

    @param estimulo ->Estimulo
    @param resposta ->Resposta
    """
    def __init__(self,estimulo,resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
        
        
    """
    método activar da classe Reaccao
    recebe uma percepção e a utilizar o método detectar da classe Estimulo descobre a sua intensidade
    Se a intensidade for >0 faz return de uma Accao utilizando o método activar da Classe Resposta

    @param percepcao-> percepcao
    @return Accao
    """         
    def activar(self,percepcao):
        intensidade =self.__estimulo.detetar(percepcao)
        if(intensidade>0):
            return self.__resposta.activar(percepcao,intensidade)
        