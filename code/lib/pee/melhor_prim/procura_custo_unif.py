from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

'''
Classe ProcuraCustoUnif
Herança de ProcuraMelhorPrim()
Caso particular da procura melhor-primeiro em que f(n) corresponde ao custo do percurso associado a cada nó

'''
class ProcuraCustoUnif(ProcuraMelhorPrim):
    
    '''
    Método construtor da classe
    Vai utilizar o super construtor dando como atributo a classe AvaliadorCustoUnif()
    '''
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())