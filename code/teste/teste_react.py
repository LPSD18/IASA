from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from ecr.hierarquia import Hierarquia
from ecr.prioridade import Prioridade
from sae import Controlo
from sae import Simulador
from ecr.comport_comp import ComportComp



'''
Modulo teste_react precisa de utilizar um ComportComp -->Requesito de avaliação
'''


#________________________________________________________________________________________________________________
#Controlo de teste

class ControloReactTeste(ControloReact):
    '''
    Método construtor da classe ControloReactTeste

    @param comportamento
    '''
    def __init__(self,comportamento):
        
        super().__init__(comportamento)

    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)
        

#________________________________________________________________________________________________________________
# Activação

controlo = ControloReact(Recolher())
Simulador(5,controlo).executar()