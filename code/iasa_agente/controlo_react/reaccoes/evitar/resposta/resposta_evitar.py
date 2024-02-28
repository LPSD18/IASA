from random import choice
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.resposta import Resposta
from sae.ambiente.direccao import Direccao

'''
Oposto da RespostaMover
'''
class RespostaEvitar(RespostaMover):

    '''
    método Construtor da classe RespostaEvitar

    @param Direccao dir_inicial 
    inicializar list de Direccao
    '''
    def __init__(self, dir_inicial=Direccao.ESTE):
        #self.__direccoes= [Direccao.NORTE,Direccao.SUL,Direccao.ESTE,Direccao.OESTE]
        super().__init__(dir_inicial)
        self.__direccoes=list(Direccao)


    '''
    Verificar se está em contacto com o obstaculo(utilizar função "alterar_dir")
    Sim--> Verificar direção livre(utilizar alterar_direccao)
        Sim--> Alterar direção para direção livre aleatoria 
        Não--> 
    Não--> Activar resposta da direção atual

    @param Percepcao percepcao
    @param Float intensidade
    @return Accao
    '''
    def activar(self,percepcao, intensidade):
    
        contacto_obst = percepcao.contacto_obst(self._accao.direccao)
        if(contacto_obst):
            contacto_obst = not self.__alterar_direccao(percepcao)
        if not contacto_obst:
            return super().activar(percepcao,intensidade)
        
    
    '''
    Método que altera a direccao 
    encontra uma direccao livre (utilizar o metodo direccao_livre)
    se existir uma altera a direccao e retorna essa direccao livre
    @param Percepcao percepcao
    @return direccao livre utilizada para alterar direccao
    '''
    def __alterar_direccao(self,percepcao):
        novaDir = self.direccao_livre(percepcao)
        if(novaDir is not None):
            #self.actualDir=novaDir
            self._accao.direccao = novaDir
            return novaDir

        '''
        '''
    
    '''
    Vai à procura de uma direccao livre 
    criar um array de direccoes livres e fazer uma choice(random) de uma dessas direccoes livres
    @param Percepcao percepcao
    @return Direccao
    '''
    def direccao_livre(self,percepcao):
        dir_livres=[direccao for direccao in self.__direccoes if not percepcao.contacto_obst(direccao)]
        if(dir_livres):
            return choice(dir_livres)