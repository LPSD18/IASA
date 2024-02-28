from plan.plano import Plano


'''
Classe PlanoPEE
Herança da classe Plano
Utilizada para a pesquisa por espaço de estados
'''
class PlanoPEE(Plano):


    '''
    Construtor da classe
    ''' 
    def __init__(self,solucao):
        self.__solucao = solucao
        


    '''
    Método que obtêm o operador do estado caso este esteja na solução
    Verificar a dimensão da solução e enquanto for maior que 1
    confirmar que o estado do primeiro nó da solução é igual ao estado dado pelo método
    se for igual remove-se o primeiro nó com o operador nulo
    retorna-se depois o operador do primeiro nó da solução atualizada
    '''
    def obter_accao(self,estado):
        #sem verificar a dimensão o código para de correr,precisa de ter pelo menos dois nós
        if self.__solucao.dimensao>1:
            estadoSolucao = self.__solucao[0].estado
            if(estado==estadoSolucao):
                self.__solucao.remover()
                no = self.__solucao[0]
                return no.operador
        
            

    '''
    método para mostrar a solução na interface gráfica
    '''
    def mostrar(self,vista):
        
        vista.mostrar_solucao(self.__solucao)
        