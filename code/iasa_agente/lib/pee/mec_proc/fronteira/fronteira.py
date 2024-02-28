from abc import ABC, abstractmethod


'''
criar uma propriedade dimensão para substituir o len da lista de nos
'''

class Fronteira(ABC):

    '''
    Construtor da classe
    utilizar o método iniciar() para a criação da lista vazia de nos
    '''
    def __init__(self):
        
        self.iniciar()
    

    '''
    propriedade read only
    verifica o tamanho da lista de nos
    se for vazio return True
    se não return False
    '''
    @property
    def vazia(self):
        return len(self._nos)==0
            
    '''
    Iniciar a fronteira de nós com uma lista vazia
    Utilizar este método no construtor da classe
    return de uma lista vazia de nos
    '''
    def iniciar(self):
        self._nos = []
    
    def len_nos(self):
        return len(self._nos)
    
    '''
    método abstrato da classe
    Dependendo da classe filha que utiliza este método pode fazer append ou insert do no na lista de nos
    '''
    @abstractmethod
    def inserir(self,no):
        '''
        
        '''
    '''
    return do primeiro indice da lista de nos e remove esse no da lista 
    '''
    def remover(self):
        return self._nos.pop(0)
        '''
        '''