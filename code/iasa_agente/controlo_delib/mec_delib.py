from sae import Elemento

class MecDelib:

    '''
    construtor da classe
    '''
    def __init__(self,modelo_mundo):
        self.__modelo_mundo = modelo_mundo


    '''
    Vai gerar conjunto de objetivos-->Estados que o agente quer atingir
    Esses estados são todos os estados que contêm um alvo
    '''
    def deliberar(self):
        objetivos = [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        if(objetivos):
            objetivos.sort(key=self.__modelo_mundo.distancia)
            return objetivos
        '''
        Gerar um conjunto de objetivos -->todos os estados em que o elemento é um alvo
        Ordenar lista de objetivos por distancia ao agente
        '''