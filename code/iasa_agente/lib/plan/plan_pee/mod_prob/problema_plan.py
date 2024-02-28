from mod.problema.problema import Problema


class ProblemaPlan(Problema):

    def __init__(self, modelo_plan,estado_final):
        self.__modelo_plan = modelo_plan
        self.__estado_final = estado_final
        super().__init__(self.__modelo_plan.obter_estado(),self.__modelo_plan.obter_operadores())
        '''
        Construtor da classe
        '''

    def objectivo(self, estado):
        if(estado.posicao == self.__estado_final.posicao):
            return True
        return False
        
        '''
        Vai ver se o estado já é objetivo ou não
        '''