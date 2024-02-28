from pee.melhor_prim.heuristica import Heuristica

'''
Classe HeurSeq
Herança da classe Heuristica
'''
class HeurSeq(Heuristica):

    '''
    Construtor da classe
    '''
    def __init__(self,valor_final):
        self.valor_final=valor_final


    '''
    Vê a estimativa das posições incorretas na lista de sequencia
    '''

    def h(self,estado):
        num=0
        for i in range(len(estado.array)):
            for j in range(len(estado.array)):
                if(i!=j)and(estado.array[i]>estado.array[j])and(i<j):
                    num+=1
        # print(num)
        return num