from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

'''
Classe ProcuraProfundidade
Filha da classe MecanismoProcura

'''
class ProcuraProfundidade(MecanismoProcura):
    
    '''
    Método construtor da classe
    Utilizar o construtor da super classe a utilizar a class FronteiraLIFO() como o atributo do construtor
    '''
    def __init__(self):
        super().__init__(FronteiraLIFO())
        
    '''
    Método memorizar
    É utilizado para memorizar o nó na lista de nós da fronteira na procura atual utilizada
    Inserir(metodo da classe fronteira) o no dado no método na lista fronteira da super classe 


    @param no
    '''
    def _memorizar(self, no):
        self._fronteira.inserir(no)

    def complexidade_especial(self):
        return self.maximo
        