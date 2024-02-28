from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.procura_grafo import ProcuraGrafo


class ProcuraLargura(ProcuraGrafo):
    
    '''
    método construtor da classe
    Utiliza o construtor da super classe a class FronteiraFIFO() como atributo do construtor
    
    '''
    def __init__(self):
        super().__init__(FronteiraFIFO())
        