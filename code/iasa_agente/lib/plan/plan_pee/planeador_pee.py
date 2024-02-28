from pee.melhor_prim.procura_AA import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador
from pee.tipo_procura import TipoProcura


class PlaneadorPEE(Planeador):

    def __init__(self,procura):
        self.__tipo = TipoProcura(procura)
        self.__mec_pee = None
        if(self.__tipo.AA==self.__tipo):
            self.__mec_pee = ProcuraAA()
        elif(self.__tipo.CUSTO_UNIFORME==self.__tipo):
            self.__mec_pee = ProcuraCustoUnif()
        elif(self.__tipo.SOFREGA==self.__tipo):
            self.__mec_pee = ProcuraSofrega()
        '''
        Construtor da classe
        '''
    
    def planear(self,modelo_plan,objectivos):
        solucao=None
        if(self.__tipo.SOFREGA==self.__tipo or self.__tipo.AA==self.__tipo):
            solucao = self.__mec_pee.procurar(ProblemaPlan(modelo_plan,objectivos[0]),HeurDist(objectivos[0]))
        else:
            solucao = self.__mec_pee.procurar(ProblemaPlan(modelo_plan,objectivos[0]))
        
        print(self.__tipo)
        print('Complexidade temporal',self.__mec_pee.complexidade_temporal())
        print('Complexidade espacial',self.__mec_pee.complexidade_especial())
        
        return PlanoPEE(solucao)
        '''
        planear para o primeiro item do objetivos
        utilizar o mecanismo de procura inicializado no construtor 
        usar o método procurar desse mecanismo e criar
        uma instancia e PlanoPEE com a solução que se retorna desse método
        '''