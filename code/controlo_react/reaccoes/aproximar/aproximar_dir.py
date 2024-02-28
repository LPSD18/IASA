# from ecr.comportamento import Comportamento
from controlo_react.reaccoes.aproximar.estimulo.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao

'''
Classe AproximarDir
Herança de Reaccao
Vai ser uma reação que dispara com o estimulo alvo e estimular uma RespostaMover

'''
class AproximarDir(Reaccao):

    '''
    Método construtor da clase AproximarDir
    recebe uma direccao
    Instancia um estimulo e uma resposta e chama o construtor da superClasse
    '''
    def __init__(self,direccao):
        self.direccao=direccao
        self.__estimulo=EstimuloAlvo(self.direccao)
        self.__resposta=RespostaMover(self.direccao)
        super().__init__(self.__estimulo,self.__resposta)