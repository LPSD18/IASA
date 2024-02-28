from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar
from ecr.comport_comp import ComportComp
from ecr.hierarquia import Hierarquia

'''
Classe Recolher
Esta classe reúne as três reações utilizadas para serem utilizadas no simulador 
Segue a base da hierarquia onde a  primeira reação no array é a principal
Herança de Hierarquia
'''
class Recolher(Hierarquia):

    '''
    Método construtor da classe
    Inicialização de instancias das três reações e utiliza-se o super construtor da classe Recolher para a sua inicialização
    '''
    def __init__(self):
    
        self.aproximar = AproximarAlvo()
        self.evitar = EvitarObst()
        self.explorar = Explorar()
        reaccoes = [self.aproximar,self.evitar,self.explorar]
        #reaccoes = [self.explorar]
        super().__init__(reaccoes)