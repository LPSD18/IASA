from mod.problema.problema import Problema
from sequencia.mod_prob.estado_seq import EstadoSeq
from sequencia.mod_prob.operador_seq import OperadorSeq

'''
Classe ProblemaSeq
Herança de Problema

'''
class ProblemaSeq(Problema):
    '''
    Construtor da classe
    '''
    def __init__(self,array_inicial,array_final,operadores):
        # print('ola')
        super().__init__(EstadoSeq(array_inicial),[OperadorSeq(ope.indice1,ope.indice2)for ope in operadores])
        # print('ola1')
        self.estado_final = EstadoSeq(array_final)

    def objectivo(self, estado):
        '''
        Verificar se o estado final é igual ao estado atual
        Se sim return true
        '''
        if self.estado_final==estado:
            # print('efrg')
            return True
        