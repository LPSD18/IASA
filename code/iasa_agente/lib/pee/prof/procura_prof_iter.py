from pee.prof.procura_prof_lim import ProcuraProfLim

'''
Classe ProcuraProfIter
Herança de ProcuraProfLim

'''
class ProcuraProfIter(ProcuraProfLim):


    '''
    Procura em profundidade iterativa:
        • Para um limite de profundidade crescente
        • Realizar procura com o limite actual
        • Se existe solução, retornar solução

    
    @param problema
    @param inc_prof
    @param limite_prof
    '''
    def procurar(self,problema,inc_prof=1,limite_prof=100):
        # solucao = None
        for i in range(0,limite_prof+1,inc_prof):
            self.prof_max = i
            solucao = super().procurar(problema)
            if solucao:
                return solucao
            
            

        