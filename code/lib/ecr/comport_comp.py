from abc import ABC,abstractmethod

from sae.agente.accao import Accao
from .comportamento import Comportamento

"""
Classe ComportComp
Contrato funcional com Comportamento
"""
class ComportComp(Comportamento):
    
    """
    método construtor da classe ComportComp

    @param comportamento ->List<Comportamentos>
    """
    def __init__(self,comportamentos):
        self.__comportamentos=comportamentos

    """
    método activar(percepcao)

    método activar da classe ComportComp

    1- Ciclo for para activar comportamentos
    2- se der resposta adicionar accao a uma lista de accoes
    3- ver se Accao existe
    4- guardar accoes numa lista
    5- utilizar selecionar_accao para retornar accao principal

    @param percepcao->Percepcao
    @return Accao
    """
    def activar(self,percepcao):

        arrayAccoes=[]

        for i in self.__comportamentos:
            accao = i.activar(percepcao)
            if(accao):
                arrayAccoes.append(accao)
        if len(arrayAccoes)>0:
            return self.selecionar_accao(arrayAccoes)

        
    
    """
    método selecionar_accao(accoes)

    método abstract da classe ComportComp que irá ser utilizado por outras classes 
    apenas inicializa o que recebe no método
    Hierarquia--> Os primeiros atributos da lista é os que tem maior prioridade Nº0->Maior prioridade assim em diante
    Prioridade--> Analisar a propriedade de cada uma das accoes e retorna a que tiver a maior prioridade

    @param accoes->List<Accao>
    """
    @abstractmethod
    def selecionar_accao(self,accoes):
        '''
        '''
