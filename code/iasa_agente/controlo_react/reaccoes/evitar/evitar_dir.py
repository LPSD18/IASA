from controlo_react.reaccoes.evitar.estimulo.estimulo_obst import EstimuloObst
from controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar
from ecr.reaccao import Reaccao

'''
Classe EvitarDir
Herança de Reaccao
'''
class EvitarDir(Reaccao):

    '''
    Método construtor da classe EvitarDir
    Instancia um estimulo(Classe EstimuloObst) e uma resposta
    Utiliza o construtor da super classe com a resposta e o estimulo instanciados

    @param direccao
    @param resposta
    '''
    def __init__(self,direccao,resposta):
        self.__resposta=resposta
        self.__estimulo=EstimuloObst(direccao)
        super().__init__(self.__estimulo,self.__resposta)