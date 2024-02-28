from pee.mec_proc.fronteira.fronteira import Fronteira

'''
Classe FronteiraFIFO
Filha da classe Fronteira 

'''
class FronteiraLIFO(Fronteira):

    '''
    Inserir o nó no index 0 da list 
    insert adiciona o objeto no index pretendido pelo utilizador
    Os ultimos a entrar são os primeiros a sair portanto adiciona-se no index 0 (Last In First Out)
    '''
    def inserir(self,no):
        self._nos.insert(0,no)
        '''
        '''