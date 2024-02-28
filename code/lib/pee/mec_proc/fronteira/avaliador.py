from abc import ABC

'''
Define o contrato funcional (interface) de avaliação da prioridade de um nó para
ordenação da fronteira por prioridade, é concretizado de acordo o tipo de procura
'''

class Avaliador(ABC):

    '''
    Método de interface
    Vai ser desenvolvido pelas sub-classes da classe Avaliador

    @param no
    '''
    def prioridade(self,no):
        
        '''
        '''
