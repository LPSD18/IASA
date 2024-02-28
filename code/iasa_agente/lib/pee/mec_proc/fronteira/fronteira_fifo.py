from pee.mec_proc.fronteira.fronteira import Fronteira

'''
Classe FronteiraFIFO
Classe Filha da classe Fronteira
'''
class FronteiraFIFO(Fronteira):


    '''
    Fazer append do nó na lista de nós da fronteira 
    append adiciona o objeto no fim da lista
    Os ultimos a entrar são os ultimos a sair portanto faz-se append para o nó ficar no fim da lista (First In First Out)
    vai-se buscar a lista de nos à super classe

    @param no
    '''
    def inserir(self, no):
        self._nos.append(no)
        
