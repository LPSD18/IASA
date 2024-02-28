from pee.melhor_prim.aval.avaliador_AA import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada

'''
Classe ProcuraAA
Herança da super classe ProcuraInformada
'''
class ProcuraAA(ProcuraInformada):

    '''
    Método construtor da classe
    Utilizar o construtor da super classe com uma instancia da classe AvaliadorAA()
    '''
    def __init__(self):
        super().__init__(AvaliadorAA())
        '''
        '''