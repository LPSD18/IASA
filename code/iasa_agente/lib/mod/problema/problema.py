from abc import ABC, abstractmethod

'''
Classe Problema
Abstract
Esta classe verifica e analisa o problema atual, o seu estado inicial e o objetivo do problema
'''
class Problema(ABC):

    '''
    Método construtor da classe

    @param estado_inicial
    @param operadores
    '''
    def __init__(self,estado_inicial,operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    '''
    propriedade read only
    @return estado_inicial
    '''
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    '''
    propriedade read only
    @return operadores List<Operator>
    '''
    @property
    def operadores(self):
        return self.__operadores


    '''
    Verifica se o estado é o objetivo
    @param Estado estado
    @return boolean
    '''
    @abstractmethod
    def objectivo(self,estado):
        '''
        '''