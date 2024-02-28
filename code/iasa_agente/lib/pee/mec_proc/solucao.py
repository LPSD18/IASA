
'''
Solução vai ser uma sequencia de nos
Criar uma lista dos nos utilizados
'''

class Solucao:

    '''
    Criar uma lista de nos -->percurso de nos (vazia no inicio)
    ciclo while para adicionar à lista de nos os nos antecessores ao nó atual do ciclo

    '''
    def __init__(self,no_final):
        self.__percurso =[]
        no = no_final
        while no:
            self.__percurso.insert(0,no)
            no = no.antecessor
        

    '''
    propriedade read only
    return do tamanho da lista de nos percurso

    @return int
    '''
    @property
    def dimensao(self):
        return len(self.__percurso)
    '''
    se a lista percurso não for vazia remover o primeiro indice da lista e fazer return desse no

    @return No
    '''
    def remover(self):
        if self.__percurso:
            return self.__percurso.pop(0)
        '''
        '''
    
    '''
    return de um iterador do percurso da solucao 
    iter-->Get an iterator from an object. 
    In the first form, the argument must supply its own iterator, or be a sequence. 
    In the second form, the callable is called until it returns the sentinel.

    @return Iterator<No>
    '''
    def __iter__(self):
        return iter(self.__percurso)
        

    '''
    faz return do No pretendido pelo index dado no método
    ao fazer no=Solucao[1] chama esta função (exemplo)


    @param index: Int
    @return No
    '''
    def __getitem__(self,index):
        return self.__percurso[index]
        '''
        '''

