from heapq import heappush , heappop
'''
biblioteca heapq transforma uma lista numa lista com prioridade 
    dois metodos --> heappush insere um elemento na lista-- introduz pela ordem do valor do elemento(prioridade)
                     heappop remove um elemento da lista
'''


from pee.mec_proc.fronteira.fronteira import Fronteira


'''
Classe FronteiraPrioridade
Herança de Fronteira

'''
class FronteiraPrioridade(Fronteira):

    '''
    Método construtor

    @param avaliador
    '''
    def __init__(self,avaliador):
        super().__init__()
        self.__avaliador=avaliador
        
        '''
        '''
    
    '''
    getter do atributo avaliador    
    '''
    @property
    def avaliador(self):
        return self.__avaliador

    '''
    Método inserir
    Insere na lista de nos o no com a prioridade deste no
    a lista de nos vem da super classe Fronteira()

    @param no
    '''    
    def inserir(self,no):
        prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos,(prioridade,no))

        '''
        '''

    '''
    Método remover
    Remover da lista de nos o nó com a prioridade mais pequena
    _ --> significa que não vai ser utilizada - prioridade anonima
    a lista de nos vem da super classe Fronteira()

    @return No
    '''
    def remover(self):
        (_,no)=heappop(self._nos)
        return no
        '''
        '''