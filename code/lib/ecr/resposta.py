from sae import Accao
import sae

"""
Classe Resposta
"""
class Resposta:

    """
    método construtor
    @param accao ->Accao
    """
    def __init__(self,accao):
        self._accao=accao

        """
        método Activar da classe Resposta
        Depende da percepcao e intensidade ativa a accao
        @param percepcao
        @param intensidade
        @return Accao
        """
    def activar(self,percepcao,intensidade=0):
        self._accao.prioridade = intensidade
        return self._accao
        

