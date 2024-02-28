from pee.mec_proc.mecanismo_procura import MecanismoProcura


'''
Classe ProcuraGrafo que utiliza a classe abstrata MecanismoProcura
Classe tambem abstrata
Esta classe é utilizada pela classe ProcuraLargura

Grafo do espaço de estados apresenta ciclos 
'''
class ProcuraGrafo(MecanismoProcura):

    '''
    Iniciar a memoria da fronteira utilizando o método da super classe

    @param fronteira
    '''
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados={}
        
    '''
    explorados é uma estrutura indexada de nos onde se pode associar aos estados dos nós o no
    IF self._manter(no)--> 1-adicionar o nó ao seu respetivo estado no dict de explorados "{no.estado : no}"
                           2-inserir o nó na lista da fronteira(VERIFICAR)------------

    @param no
    '''
    def _memorizar(self,no):
        if self._manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)
        
        '''
        '''

    '''
    indica se um no deve ser mantido para exploração ou não em memória
    se o estado do nó não existir fazer return do estado do no

    @param no
    @return boolean
    '''
    def _manter(self,no):
        return no.estado not in self._explorados

        '''
        '''

    def complexidade_especial(self):
        return len(self._explorados)

