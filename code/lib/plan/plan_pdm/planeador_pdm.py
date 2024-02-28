from pdm.pdm import PDM
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

'''
Classe PlaneadorPDM
Herança de Planeador
'''
class PlaneadorPDM(Planeador):
    
    '''
    Método construtor

    @param gama float
    @param delta_max float
    '''
    def __init__(self,gama=0.85, delta_max=1):
        self.__gama=gama
        self.__delta_max=delta_max


    '''
    @param modelo_plan
    @param objectivos
    @return PlanoPDM
    necessário de uma instancia de um ModeloPDMPlan
    instanciar um atributo da classe PDM
    ir buscar a utilidade e politica ao método resolver da classe PDM
    instanciar um planoPDM com U e pol
    return de um PlanoPDM com os atributos de U e pol
    '''
    def planear(self,modelo_plan,objectivos):
        modelo_plan = ModeloPDMPlan(modelo_plan,objectivos)
        pdm = PDM(modelo_plan,self.__gama,self.__delta_max)
        U,pol = pdm.resolver()
        if U and pol:
            return PlanoPDM(U,pol)
        
    
    