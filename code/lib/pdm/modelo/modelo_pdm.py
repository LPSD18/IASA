from abc import ABC
from abc import abstractmethod

'''
    Necessário funções para conjunto de estados
                            conjunto de ações possiveis
                            probabilidade de transição de s para s' através de a

    '''
class ModeloPDM(ABC):
    

    '''
    Método abstract
    S – conjunto de estados do mundo
    '''
    @abstractmethod
    def S(self):
        ''''''

    '''
    Método abstract
    A(s) – conjunto de acções possíveis no estado s pertencente a S
    '''
    @abstractmethod
    def A(self,s):
        ''''''

    '''
    Método abstract
    T(s,a,s’) – probabilidade de transição de s para s’ através de a
    '''
    @abstractmethod
    def T(self,s,a,sn):
        ''''''

    '''
    Método abstract
    R(s,a,s’) – retorno esperado na transição de s para s’ através de a
    '''
    @abstractmethod
    def R(self,s,a,sn):
        ''''''

    '''
    Método abstract
    Buscar os estados sucessores o conjunto de estados
    '''
    @abstractmethod
    def Suc(self,s,a,):
        ''''''
    