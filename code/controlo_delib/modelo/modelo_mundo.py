import math
from controlo_delib.modelo.operador_mover import OperadorMover
from mod.agente.estado_agente import EstadoAgente
from plan.modelo.modelo_plan import ModeloPlan
from sae import Direccao


class ModeloMundo(ModeloPlan):

    def __init__(self):
        self.__alterado =False
        self.__estado = None
        self.__estados =[]
        self.__elementos = {}
        self.__operadores = [OperadorMover(self,direccao) for direccao in Direccao]


        '''
        
        '''
    
    '''
    Getter do atributo booleano alterado
    '''
    @property
    def alterado(self):
        return self.__alterado
    
    
    '''
    Getter do atributo elementos
    '''
    @property
    def elementos(self):
        return self.__elementos
    
    
    def obter_estado(self):
        return self.__estado
        '''
        return estado
        '''
    
    def obter_estados(self):
        return self.__estados
        '''
        return estados
        '''

    def obter_operadores(self):
        return self.__operadores
        '''
        return operadores
        '''

    def obter_elemento(self,estado):
        return self.__elementos.get(estado.posicao)
        '''
        return elemento para a direção do estado
        '''

    def distancia(self,estado):
        return math.dist(estado.posicao,self.__estado.posicao)
        '''
        return distancia do estado atual do agente a comparar com
        a posição do estado dado
        '''

    def actualizar(self,percepcao):
        newEstado = EstadoAgente(percepcao.posicao)
        self.__estado=newEstado
        if(self.__elementos != percepcao.elementos):
            newEstados = [EstadoAgente(posicao)for posicao in percepcao.posicoes]
            self.__elementos = percepcao.elementos
            self.__estados = newEstados
            self.__alterado=True
        else:
            self.__alterado = False
        '''
        percepcao tem atributo posicao
        atualizar o atributo estado no construtor com um novo agente e essa posicao
        se elementos da percepcao forem diferentes dos elementos pre existentes-->atualizar a estrutura interna do agente com os novos elementos para o agente
        atualizar o conjunto de estados com um novo conjunto de estados
        mudar o atributo alterado para True
        no else --> alterado=False
        '''

    def mostrar(self,vista):
        
        vista.mostrar_alvos_obst(self.__elementos)
        vista.marcar_posicao(self.__estado.posicao)
        '''
        utilizar biblioteca sae para mostrar alvos e marcar posicao
        '''