'''
Problema da contagem 
Dado um valor inicial, um valor final e um conjunto de incrementos possiveis, que incrementos realizar para atingir ou superar o valor final

Valor inicial = 0
Valor final = 5
Incrementos:1,2,-1
Custo da ação: incremento**2

--> 2,2,1 (5<=) custo de incremento=12
-->1,1,1,1,1(5<=) custo de incremento=5 
'''

from pee.larg.procura_largura import ProcuraLargura
from pee.melhor_prim.procura_AA import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
# from mod_prob.problema_contagem import ProblemaContagem
from mod_prob.estado_valor import EstadoValor
# from mod_prob.operador_incremento import OperadorIncremento
from mod_prob.heuristica_valor import HeuristicaValor
from mod_prob.operador_incremento import OperadorIncremento
from mod_prob.problema_contagem import ProblemaContagem
# from mod_prob.problema_contagem import ProblemaContagem
# from teste_pee.mod_prob.operador_incremento import OperadorIncremento
# from mod_prob.problema_contagem import ProblemaContagem

'''
Resultados obtidos

ProcuraProfLim
Solucao:  [0, 2, 1, 3, 5, 4, 6, 8, 7, 9, 11, 10, 12, 14, 13, 15]
Dimensão:  16
Custo:  45

ProcuraProfIter
Solucao:  [0, 2, 4, 6, 8, 10, 12, 14, 16]
Dimensão:  9
Custo:  32

ProcuraLargura
Solucao:  [0, 1, 3, 5, 7, 9, 11, 13, 15]
Dimensão:  9
Custo:  29

ProcuraCustoUnif
Solucao:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Dimensão:  16
Custo:  15

ProcuraSofrega
Solucao:  [0, 2, 4, 6, 8, 10, 12, 14, 15]
Dimensão:  9
Custo:  29

ProcuraAA
Solucao:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Dimensão:  16
Custo:  15

'''
#Valor Inicial do teste do problema de contagem
# inicial=0
# #Valor Final do teste do problema de contagem
# final=1
# # final=1
# #Valores de incremento do problema de contagem
# incrementos=[1,2,-1]
# #Inicialização de uma instancia de ProblemaContagem dando o valor inicial, o valor final e os incrementos
# problema = ProblemaContagem(EstadoValor(inicial),EstadoValor(final),[OperadorIncremento(incremento)for incremento in incrementos])
# #Inicialização de um mecanismo de procura
# mec_proc = ProcuraProfLim()
# # mec_proc = ProcuraProfIter()
# # mec_proc = ProcuraLargura()
# # mec_proc = ProcuraCustoUnif()
# # mec_proc = ProcuraSofrega()
# # mec_proc = ProcuraAA()
# heuristica = HeuristicaValor(EstadoValor(final))
# #Inicialização de uma solução a utilizar o método procurar do mecanismo de procura
# solucao = mec_proc.procurar(problema)
# # solucao = mec_proc.procurar(problema,heuristica)
# #Prints para verificar a solução, dimensão e custo do problema
# print("Solucao: ",[no.estado.valor for no in solucao])
# print("Dimensão: ",solucao[-1].profundidade+1)
# print("Custo: ", solucao[-1].custo )


'''
Resultados obtidos 

ProcuraProfLim()
VALOR_INICIAL = 0
VALOR_FINAL = 1
Solucao:  [0, -1, 1]
Dimensão:  3
Custo:  5

VALOR_INICIAL = 0
VALOR_FINAL = 15
Solucao:  [0, -1, 1, 3, 2, 4, 6, 5, 7, 9, 8, 10, 12, 11, 13, 15]
Dimensão:  16
Custo:  45

ProcuraProfIter
VALOR_INICIAL = 0
VALOR_FINAL = 1
Solucao:  [0, 2]
Dimensão:  2
Custo:  4

VALOR_INICIAL = 0
VALOR_FINAL = 15
Solucao:  [0, 2, 4, 6, 8, 10, 12, 14, 16]
Dimensão:  9
Custo:  32

ProcuraLargura
VALOR_INICIAL = 0
VALOR_FINAL = 1
Solucao:  [0, 1]
Dimensão:  2
Custo:  1

VALOR_INICIAL = 0
VALOR_FINAL = 15
Solucao:  [0, 1, 3, 5, 7, 9, 11, 13, 15]
Dimensão:  9
Custo:  29

ProcuraCustoUnif
VALOR_INICIAL = 0
VALOR_FINAL = 15
Solucao:  [0, 1]
Dimensão:  2
Custo:  1

VALOR_INICIAL = 0
VALOR_FINAL = 15
Solucao:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Dimensão:  16
Custo:  15

'''

VALOR_INICIAL = 0
VALOR_FINAL = 15
INCREMENTOS = [1,2,-1]

problema = ProblemaContagem(VALOR_INICIAL,VALOR_FINAL,INCREMENTOS)

mec_proc = ProcuraProfLim()
# mec_proc = ProcuraProfIter()
# mec_proc = ProcuraLargura()
# mec_proc = ProcuraCustoUnif()
solucao = mec_proc.procurar(problema)

print("Solucao: ",[no.estado.valor for no in solucao])
print("Dimensão: ",solucao[-1].profundidade+1)
print("Custo: ", solucao[-1].custo )