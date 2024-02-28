from mod.operador import Operador
from sequencia.mod_prob.estado_seq import EstadoSeq

'''
Classe OperadorSeq
Herança da classe Operador
'''
class OperadorSeq(Operador):

    '''
    Construtor da classe
    '''
    def __init__(self,indice1,indice2):
        self.__indice1=indice1
        self.__indice2 =indice2
    
    '''
    Get indice1
    '''
    @property
    def indice1(self):
        return self.__indice1
    
    '''
    Get indice2
    '''
    @property
    def indice2(self):
        return self.__indice2
    
    '''
    Método Aplicar
    Neste método verificar-se se o indice1 do array for maior que o indice2 do array
    Troca-se a posição dos valores nesses atributos pelo valor do outro indice
    Return de um novo estado com esse array
    '''
    def aplicar(self,estado):
        array = estado.array.copy()
        if(array[self.indice1]>array[self.indice2]):
            num1=array[self.indice1]
            num2=array[self.indice2]
            array[self.indice1]=num2
            array[self.indice2]=num1
            return EstadoSeq(array)
        '''
        FAZER
        Aqui vai-se alterar os valores no array
        '''
        
    
    def custo(self,estado,estado_suc):
        return abs(self.__indice2-self.__indice1)
        '''
        retorna a subtração entre os dois indices
        '''

    def __repr__(self):
        
        return "Trocar(%s,%s)"%(self.indice1,self.indice2)