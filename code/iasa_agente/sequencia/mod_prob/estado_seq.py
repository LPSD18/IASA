from mod.estado import Estado

'''
Classe EstadoSeq
Herança da classe Estado
'''
class EstadoSeq(Estado):

    '''
    Construtor da classe
    '''
    def __init__(self,array):
        self.__array=array
        # print('Array-->',array)
        self.__id_valor = hash(tuple(self.__array))
        
    '''
    Método para retornar o atributo id_valor
    '''
    def id_valor(self):
        return self.__id_valor
    
    '''
    Get Array
    '''
    @property
    def array(self):
        return self.__array
    
    '''
    método print
    '''
    def __repr__(self):
        return ("\r\n",str(self.__array))