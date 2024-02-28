
'''
Classe MecUtil
Verificar a utilidade das ações do modelo
'''
class MecUTil:

    '''
    Construtor da classe
    '''
    def __init__(self,modelo,gama,delta_max):
        self.__modelo=modelo
        self.__gama=gama
        self.__delta_max=delta_max
    
    '''
    Função para verificar a utilidade de um conjunto de estados num problema
    S – conjunto de estados do mundo
    A(s) – conjunto de acções possíveis no estado s  S
    '''
    def utilidade(self):
        
        S,A = self.__modelo.S,self.__modelo.A
        U = {s:(0.0)for s in S()}
        while True:
            Uant = U.copy()
            delta=0
            for s in S():
                U[s] = max([self.util_accao(s,a,Uant)for a in A(s)],default= 0)
                delta = max(delta,abs(U[s]-Uant[s]))
            if(delta<self.__delta_max):
                break
        return U

        
    '''
    Método para verificar a utilidade de uma ação
    Se o próximo estado
    Guarda instancias das possibilidades de transições e de recompensa(T,R)
    utiliza a ação e o estado dados como atributos para verificar a próxima ação a realizar-se
    caso exista soma-se com uma equação lecionada
    return dessa soma
    '''
    def util_accao(self,s,a,U):
        T,R,Suc = self.__modelo.T,self.__modelo.R, self.__modelo.Suc
        return sum(T(s,a,sn)*(R(s,a,sn)+self.__gama*U[sn])for sn in Suc(s,a))
    


        