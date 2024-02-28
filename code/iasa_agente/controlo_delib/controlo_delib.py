from controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae import Controlo
from sae.vistas.vista_amb import VistaAmb

class ControloDelib(Controlo):

    '''
    Construtor da classe
    '''
    def __init__(self,planeador):
        self.__planeador=planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objectivos=None
        self.__plano = None

        


    '''
    1-->Assimilar uma percepcao -função assimilar
    if(reconsiderar is True)
        2-->deliberar do mec_delib
        3-->planear -função planear
    4-->executar -função executar return accao
    '''
    def processar(self, percepcao):
        self.__assimilar(percepcao)
        if(self.__reconsiderar()):
            self.__deliberar()
            self.__planear()
        self.__mostrar()
        return self.__executar()

        

    '''
    atualizar o moedelo_mundo com a informação que vem na percepcao--> chamar atualizar do modelo_mundo
    '''
    def __assimilar(self,percepcao):
        self.__modelo_mundo.actualizar(percepcao)
        

    '''
    reconsiderar se modelo_mundo.__alterado=True
    ou não existir um plano --> self.__plano == None ou lista vazia    
    '''
    def __reconsiderar(self):
        if(self.__modelo_mundo.alterado==True) or (not self.__plano):
            return True
        
    
    def __deliberar(self):

        self.__objectivos = self.__mec_delib.deliberar()
        '''
        Utilizar a função deliberar da classe mec_delib para criar objetivos
        '''

    def __planear(self):
        if(self.__objectivos):
            self.__plano = self.__planeador.planear(self.__modelo_mundo,self.__objectivos)
        else:
            self.__plano=None

        
      
        '''
        Gerar um plano para concretizar os objetivos
        '''

    def __executar(self):
        if(self.__plano):
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if(operador):
                return operador.accao
        
        '''
        Utilizar o plano para retornar a accao
        '''

    def __mostrar(self):
        self.vista.limpar()
        if(self.__plano):
            self.__plano.mostrar(self.vista)
        self.__modelo_mundo.mostrar(self.vista)
        '''
        método para mostrar o plano e o modelo mundo na interface gráfica
        '''