from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


'''
Classe ProcuraInformada
Herança de ProcuraMelhorPrim
Estratégias de exploração do espaço de estados (controlo da
procura) tiram partido de conhecimento do domínio do
problema para ordenar a fronteira de exploração
• Procura guiada
• Exploração selectiva do espaço de estados

'''
class ProcuraInformada(ProcuraMelhorPrim):

    '''
    Método Procurar
    1-> instanciar um atributo de heuristica
    2-> difinir uma heuristica para o avaliador utilizado
    3-> return do procurar da super classe com o problema

    @param Problema problema
    @param Heuristica heuristica
    return Solucao
    '''
    def procurar(self, problema,heuristica):
        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
        '''
        '''