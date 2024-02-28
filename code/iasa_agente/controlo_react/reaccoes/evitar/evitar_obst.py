from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

'''
Classe EvitarObst
Herança de Hierarquia
'''
class EvitarObst(Hierarquia):

    '''
    Método construtor da classe EvitarObst
    Instanciar uma resposta(Classe RespostaEvitar())
    Criar as 4 instancias das EvitarDir com a direção necessária e a instancia de resposta criada anteriormente no método
    Utilização do construtor da super classe 

    '''
    def __init__(self):
        self.__resposta=RespostaEvitar()
        self.norte = EvitarDir(Direccao.NORTE,self.__resposta)
        self.sul = EvitarDir(Direccao.SUL,self.__resposta)
        self.oeste = EvitarDir(Direccao.OESTE,self.__resposta)
        self.este = EvitarDir(Direccao.ESTE,self.__resposta)
        dir=[self.norte,self.sul,self.oeste,self.este]
        super().__init__(dir)
        