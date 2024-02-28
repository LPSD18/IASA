from pee.melhor_prim.heuristica import Heuristica


class HeuristicaValor(Heuristica):
    
    def __init__(self,valor_final):
        self.valor_final = valor_final

    def h(self, estado):
        return abs(estado.id_valor() - self.valor_final.id_valor())