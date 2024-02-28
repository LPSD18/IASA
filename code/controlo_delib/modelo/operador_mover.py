import math
import numpy as np
from mod.agente.estado_agente import EstadoAgente
from mod.operador import Operador
from sae import Accao

'''
Guardar angulo,
'''
class OperadorMover(Operador):


    def __init__(self,modelo_mundo,direcao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direcao.value
        self.__accao = Accao(direcao)
        '''
        guardar o modelo do mundo no atributo
        guardar o angulo pelo direcao.value
        guardar atributo acao (vem do sae) passar a direção que vem do construtor
        '''
    
    @property
    def accao(self):
        return self.__accao

    @property
    def ang(self):
        return self.__ang
    
    def _translacao(self,posicao,distancia,angulo):
        x,y = posicao
        dx = round(distancia*math.cos(angulo))
        dy = -round(distancia*math.sin(angulo))
        nova_posicao = (x+dx,y+dy)
        return nova_posicao
        '''
        Função para criar uma nova posição com a distancia e o angulo desde a 
        posição inicial
        '''
    
    def aplicar(self,estado):
        nova_pos = self._translacao(estado.posicao,self.__accao.passo,self.__ang)
        novo_estado = EstadoAgente(nova_pos)
        if(novo_estado in self.__modelo_mundo.obter_estados()):
            return novo_estado
        '''
        1-Criar uma nova posição com a função translação desta classe
        2-Criar um novo EstadoAgente com essa posição
        3-Verificar se esse estado faz parte dos estados do atributo modelo mundo
        4-Se for True return desse estado
        '''

    def custo(self,estado, est_sucessor):
        if(est_sucessor):
            return max(1,math.dist(estado.posicao,est_sucessor.posicao))
        '''
        proporcional
        return da distancia
        '''