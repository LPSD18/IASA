from mod.estado import Estado


class EstadoLocalidade(Estado):
    '''
    Construtor

    @param localidade
    '''
    def __init__(self,localidade):
        self.__localidade=localidade
        self.__id_valor = hash(self.__localidade)
        '''
        
        '''

    '''
    get atributo localidade
    '''
    @property
    def localidade(self):
        return self.__localidade
    
    '''
    Método id_valor
    
    @return int
    '''
    def id_valor(self):
        return self.__id_valor
        '''
        
        '''
    '''
    Método para print
    '''
    def __repr__(self):
        return self.__localidade