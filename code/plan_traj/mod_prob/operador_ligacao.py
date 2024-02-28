from mod.operador import Operador
from plan_traj.mod_prob.estado_localidade import EstadoLocalidade


class OperadorLigacao(Operador):

    '''
    Método Construtor

    @param origem
    @param destino
    @param custo
    '''
    def __init__(self,origem,destino,custo):
        self.__estado_origem = EstadoLocalidade(origem)
        self.__estado_destino = EstadoLocalidade(destino)
        self.__custo = custo
        '''
        

        '''

    '''
    Método aplicar
    se o estado for igual ao estado da origem return do estado do destino

    @param estado
    @return EstadoLocalidade
    '''
    def aplicar(self,estado):
        if estado == self.__estado_origem:
            # print('saf')
            return self.__estado_destino

        '''
        
        '''

    '''
    Método custo
    Retorna o custo do operador dado no construtor

    @param estado
    @param est_sucessor
    @return int
    '''
    def custo(self,estado, est_sucessor):
        return self.__custo
        '''
        
        '''
    '''
    método para print
    '''
    def __repr__(self):
        return "%s -> %s" %(self.__estado_origem.localidade,self.__estado_destino.localidade)