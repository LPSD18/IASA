from ecr.estimulo import Estimulo
from sae.agente.percepcao import Percepcao
#from lib.sae.agente.percepcao import PerDir
from sae.ambiente.elemento import Elemento

'''
Classe EstimuloAlvo
Herança de Estimulo
'''
class EstimuloAlvo(Estimulo):

    '''
    Construtor da classe EstimuloAlvo

    @param Direccao direccao
    @param float gama
    '''
    def __init__(self,direccao,gama=0.9):
        self.__direccao=direccao
        self.__gama=gama
        
        

    ''' 
    quando a distancia é minima dá o valor máximo e inversamente
    0.9 elevado à distancia quanto maior a distancia menor a prioridade
    percepcao direcional
    Verificar se o elemento é um alvo
        Se sim ver distancia e fazer a conta para o gama
        Se não gama=0.0

    @param Percepcao percepcao
    @return float
    '''
    def detetar(self,percepcao):
        
        (elemento,distancia,_) = percepcao.per_dir[self.__direccao]
        return self.__gama**distancia if elemento == Elemento.ALVO else 0.0