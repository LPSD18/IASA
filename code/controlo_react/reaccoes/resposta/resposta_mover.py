from sae.agente.accao import Accao
from sae.ambiente.direccao import Direccao
from ecr.resposta import Resposta

'''
Classe RespostaMover
Herança de Resposta
'''

class RespostaMover(Resposta):

    '''
    Método construtor da classe RespostaMover
    utiliza o método construtor da classe Resposta
    
    @param Direccao
    '''
    def __init__(self,direccao):
        super().__init__(Accao(direccao))
        