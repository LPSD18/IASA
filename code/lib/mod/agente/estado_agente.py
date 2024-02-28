from mod.estado import Estado

class EstadoAgente(Estado):
    def __init__(self,posicao):
        self.__posicao=posicao
        self.__id_valor = hash(self.__posicao)
        '''
        Construtor da classe
        '''

    @property
    def posicao(self):
        return self.__posicao
        '''
        Getter posicao
        '''


    def id_valor(self):
        return self.__id_valor
        '''     
        Método id_valor da função retorna o atributo id_valor buscado no construtor
        '''