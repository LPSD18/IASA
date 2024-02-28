import math
from pee.melhor_prim.heuristica import Heuristica


class HeurDist(Heuristica):

    def __init__(self,estado_final):
        self.__estado_final=estado_final
        '''
        Construtor da classe
        '''

    def h(self,estado):
        # xn, yn = estado.posicao
        # xobj,yobj = self.__estado_final.posicao
        # return math.sqrt((xn-xobj)**2+(yn-yobj)**2)
        return math.dist(self.__estado_final.posicao,estado.posicao)
        '''
        return da distancia entre a posição do estado final e a posição do estado 
        dado como atributo
        '''