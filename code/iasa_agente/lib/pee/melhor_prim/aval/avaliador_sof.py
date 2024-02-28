


'''
Classe AvaliadorSof
Herança da super classe AvaliadorHeur
utilizado para definir a prioridade do nó
'''
from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorSof(AvaliadorHeur):
    
    '''
    Método prioridade
    return do custo do nó + a heuristica do estado do nó
    '''
    def prioridade(self,no):

        return self._heuristica.h(no.estado)
        