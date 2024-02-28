from random import choice
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae.ambiente.direccao import Direccao


class Explorar(Comportamento):

    '''
    método activar(percepcao)

    Gera uma ação que representa uma movimentação aleatoria de uma das 4 direções possiveis
    1- criar list com as direções possiveis(enum Direccao)
    2- utilizar random.choice para escolher uma direção aleatoria
    3- criar um atributo RespostaMover com a direção aleatoria gerada
    4- retornar a Accao ativada pela RespostaMover utilizando a percepcao dada pelo método

    @param Percepcao
    @return Accao

    '''
    def activar(self,percepcao):
        dir=list(Direccao)
        choosenDir = choice(dir)
        resposta = RespostaMover(choosenDir)    
        return resposta.activar(percepcao)