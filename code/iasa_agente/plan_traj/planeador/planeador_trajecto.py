from pee.larg.procura_largura import ProcuraLargura
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj


class PlaneadorTrajecto:

    '''
    fazer o mesmo que se fez no outro teste
    instanciar um problema
    instanciar um mecanismo procura
    procurar uma solução para o problema
    
    '''

    def planear(self,ligacoes,loc_inicial,loc_final):

        problema = ProblemaPlanTraj(ligacoes,loc_inicial,loc_final)
        # mec_proc = ProcuraProfLim()
        # mec_proc = ProcuraProfIter()
        # mec_proc = ProcuraLargura()
        mec_proc = ProcuraCustoUnif()
        solucao = mec_proc.procurar(problema)
        
        return solucao
        '''
        
        '''