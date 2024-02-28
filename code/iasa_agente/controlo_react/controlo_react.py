from ecr.comportamento import Comportamento
from sae import Controlo

'''
Classe ControloReact
Herança da classe Controlo da package sae
'''

class ControloReact(Controlo):

    '''
    Método construtor da classe ControlReact
    
    @param Comportamto
    '''
    def __init__(self,comportamento):

        self.__comportamento = comportamento


    '''
    Método processar(percepcao)

    Recebe uma percepcao e ativa o comportamento interno retornando uma accao 
    utilizando o método activar da classe Comportamento

    @param Percepcao
    @return Accao
    '''
    def processar(self, percepcao):
        #if self.__comportamento!=None:
        return self.__comportamento.activar(percepcao)