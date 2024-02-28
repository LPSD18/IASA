from ecr.estimulo import Estimulo
from sae.modelo.ambiente import Elemento
from sae.agente.percepcao import Percepcao

'''
Classe EstimuloOBst
Herança de Estimulo
'''
class EstimuloObst(Estimulo):

    '''
    Método construtor da classe EstimuloObst

    @param direccao
    @ param intensidade , inicialmente com valor 1.0
    '''
    def __init__(self,direccao,intensidade=1.0):
        self.__direccao=direccao
        self.__intensidade=intensidade
        
    '''
    Método que deteta o estimulo e o elemento na percepcao recebida no método
    Se o elemento for o desejado retorna-se a intensidade do estimulo
    Se não retorna-se o valor 0.0

    @param percepcao
    return float
    '''
    def detetar(self, percepcao):
        elemento,_,_ = percepcao.per_dir[self.__direccao]
        return self.__intensidade if elemento==Elemento.OBSTACULO else 0.0