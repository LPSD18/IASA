from plan.plano import Plano

'''
Classe PlanoPDM
'''
class PlanoPDM(Plano):


    '''
    Construtor da classe
    @param utilidade
    @param politica
    '''
    def __init__(self,utilidade,politica):
        self.__utilidade = utilidade
        self.__politica = politica

        

    '''
    verificar se o atributo estado faz parte do dicionario politica
    se sim retornar a ação da politica para o estado 

    @param estado
    '''
    def obter_accao(self, estado):
        if estado and estado in self.__politica:
            return self.__politica[estado]
        
    
    '''
    método para mostrar na interface gráfica
    @param vista
    '''
    def mostrar(self, vista):
        if(self.__utilidade)and(self.__politica):
            vista.mostrar_valor(self.__utilidade)
            vista.mostrar_politica(self.__politica)
        