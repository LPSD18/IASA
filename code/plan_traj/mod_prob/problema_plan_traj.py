from mod.problema.problema import Problema
from plan_traj.mod_prob.estado_localidade import EstadoLocalidade
from plan_traj.mod_prob.operador_ligacao import OperadorLigacao


class ProblemaPlanTraj(Problema):
    
    '''
    Construtor
    Utilização do super construtor com EstadoLocalidade e OperadorLigacao
    Criação de uma instancia EstadoLocalidade para o estado final

    @param ligacoes
    @param loc_inicial
    @param loc_final
    '''
    def __init__(self,ligacoes,loc_inicial,loc_final):
        super().__init__(EstadoLocalidade(loc_inicial),[OperadorLigacao(ligacao.origem,ligacao.destino,ligacao.custo)for ligacao in ligacoes])
        # self.__loc_final=loc_final
        self.__estado_final = EstadoLocalidade(loc_final)
        '''
        
        '''

    '''
    Método objectivo
    faz return True se o estado for igual ao estado final dado pelo construtor
    '''
    def objectivo(self, estado):
        return (estado==self.__estado_final)
            
        '''
        
        '''