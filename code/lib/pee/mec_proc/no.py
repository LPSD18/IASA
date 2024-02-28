from mod.operador import Operador

'''
Classe No

'''
class No:

    '''
    Método construtor
    dois construtores, recebe sempre um estado e pode receber tambem um operador e um nó antecessor
    se existir antecessor o valor da profundidade é antecessor+1 e o custo é o valor do custo do antecessor+ o custo do operador entre o estado do antecessor e o estado atual 

    '''
    def __init__(self,estado,operador=None,antecessor=None):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        
        if antecessor:
            self.__profundidade = antecessor.profundidade+1
            self.__custo = antecessor.custo + operador.custo(antecessor.estado,estado) 
            
        else:
            self.__profundidade =0
            self.__custo =0
        

    '''
    propriedade read only
    @return do atributo estado da classe
    '''
    @property
    def estado(self):
        return self.__estado
    
    '''
    propriedade read only
    @return do atributo operador da classe
    '''
    @property
    def operador(self):
        return self.__operador
        
    
    '''
    propriedade read only
    @return do atributo custo da classe
    '''
    @property
    def custo(self):
        return self.__custo

    '''
    propriedade read only
    @return do atributo profundidade da classe
    '''
    @property
    def profundidade(self):
        return self.__profundidade
    
    '''
    propriedade read only
    @return do atributo antecessor da classe
    '''
    @property
    def antecessor(self):
        return self.__antecessor
    

    '''
    verifica qual é o maior custo entre o nó atual e um diferente e retorna o valor boolean dessa comparação

    @param no
    @return boolean
    '''
    def __lt__(self,no):
        return self.__custo < no.custo
        '''
        '''