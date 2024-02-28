from pee.mec_proc.fronteira.avaliador import Avaliador

'''
Classe AvaliadorHeur
Herança da super classe Avaliador
Utilizado para definir a heuristica 
'''
class AvaliadorHeur(Avaliador):

    '''
    Método definir_heuristica
    Inicializar uma instancia de heuristica

    @param heuristica
    '''
    
    def definir_heuristica(self,heuristica):
        self._heuristica = heuristica
        '''
        '''