from pee.mec_proc.fronteira.avaliador import Avaliador

'''
Classe AvaliadorCustoUnif
Herança de Avaliador()
Avalia o nó pelo seu custo
'''
class AvaliadorCustoUnif(Avaliador):

    '''
    Método prioridade
    return do custo do nó dado por atributo

    @param no
    '''
    def prioridade(self, no):
        return no.custo
