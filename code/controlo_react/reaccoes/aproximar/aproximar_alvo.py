from controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao

'''
Classe AproximarAlvo
Herança de Prioridade
'''
class AproximarAlvo(Prioridade):

    '''
    Construtor da classe
    Criar internamente as 4 instancias de AproximarDir com as direccoes necessárias
    e utiliza-se o super construtor da classe
    '''
    def __init__(self):
        self.norte = AproximarDir(Direccao.NORTE)
        self.sul = AproximarDir(Direccao.SUL)
        self.este = AproximarDir(Direccao.ESTE)
        self.oeste = AproximarDir(Direccao.OESTE)
        dir = [self.norte,self.sul,self.este,self.oeste]
        super().__init__(dir)    