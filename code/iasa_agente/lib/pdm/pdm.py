from pdm.mec_util import MecUTil


class PDM:

    '''
    Construtor da classe
    '''
    def __init__(self,modelo,gama,delta_max):
        self.__modelo = modelo
        self.gama=gama
        self.delta_max=delta_max
        self.__mec_util = MecUTil(self.__modelo,self.gama,self.delta_max)

    '''
    Calucar a politica de um estado 
    É a ação que maximiza a utilidade de um estado
    @param U
    @return Politica
    '''
    def politica(self,U):
        S,A = self.__modelo.S,self.__modelo.A
        pol = {}
        for s in S():
            if A(s):
                pol[s] = max(A(s),key=lambda a: self.__mec_util.util_accao(s,a,U))
        return pol
        

    '''
    Calcular utilidade e politica 
    no final faz-se return de tuplo com esses atributos
    '''
    def resolver(self):
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U,pol