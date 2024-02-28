from mod.operador import Operador
from mod_prob.estado_valor import EstadoValor
from mod_prob.estado_contagem import EstadoContagem
# from teste_pee.mod_prob.estado_contagem import EstadoContagem


class OperadorIncremento(Operador):

    # def __init__(self,incremento):
    #     self.__incremento=incremento
    #     '''
    #     '''
    # @property
    # def incremento(self):
    #     return self.__incremento

    # def aplicar(self,estado):
    #     return EstadoValor(self.incremento+estado.id_valor())
    # '''
    # '''

    # def custo(self,estado, est_sucessor):
    #     return EstadoValor(self.incremento**2)

    def __init__(self,incremento):
         self.__incremento = incremento

    def incremento(self):
        return self.__incremento

    def aplicar(self,estado):
        novo_valor = estado.valor + self.__incremento
        return EstadoContagem(novo_valor)

    def custo(self,estado,estado_suc):
        return self.__incremento**2