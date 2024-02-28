from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from pee.melhor_prim.procura_informada import ProcuraInformada


'''
Classe ProcuraSofrega
Herança da super classe ProcuraInformada
'''
class ProcuraSofrega(ProcuraInformada):
    
    '''
    Método construtor da classe
    Utilizar o construtor da super classe com uma instancia da classe AvaliadorSof()
    '''
    def __init__(self):
        super().__init__(AvaliadorSof())
        '''
        '''