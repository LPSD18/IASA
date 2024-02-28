from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

'''
Classe ModeloPDMPlan
Herança de ModeloPDM e ModeloPlan
'''
class ModeloPDMPlan(ModeloPDM,ModeloPlan):

    '''
    Construtor da classe
    '''
    def __init__(self,modelo_plan,objectivos,rmax=1000.0):
        self.__modelo_plan=modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
        self.__transicoes = {}
        if self.obter_estados() and self.obter_operadores(): 
            for s in self.obter_estados():
                for a in self.obter_operadores():
                    # Modelo determinista
                    sn = a.aplicar(s)
                    if sn is not None:
                        self.__transicoes[(s,a)] = sn
    

    '''
    return do atributo estado
    '''
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
        

    '''
    return de uma lista com estados
    '''
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
        
    
    '''
    return de uma lista com operadores
    '''
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
        
    '''
    conjunto de estados do mundo
    '''

    def S(self):
        return self.obter_estados()
        
    '''
    conjunto de acções possíveis no estado s pertencentes a S
    '''
    def A(self,s):
        return self.obter_operadores()
        

    '''
    prob de transição para s' através de a
    Se no array de transicoes com os atributos de s e a der o valor de sn 
    return 1
    se não return 0 
    '''
    def T(self,s,a,sn):
        if sn and (sn == self.__transicoes[(s,a)]):
            return 1
        return 0
        

    '''
    Recompensa
    primeiro verifica-se o custo da ação
    a recompensa é o valor negativo desse custo
    se sn for um objetivo adicionar a recompensa máxima à recompensa
    return da recompensa
    '''
    def R(self,s,a,sn):
        r=0
        if(sn):
            r = -(a.custo(s,sn))
            if self.__objectivos and  sn in self.__objectivos:
                r=r+self.__rmax
        return r

        
    
    '''
    Verificar se nas transições existem as que correspondem ao s e a dado como atributos
    devolve uma lista de sucessores
    '''
    def Suc(self, s, a):
        sn=[]
        if(self.__transicoes.get((s,a))):
            sn.append(self.__transicoes.get((s,a)))
        return sn