from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae import Simulador


controlo = ControloDelib(PlaneadorPEE(3))
Simulador(4,controlo).executar()


'''
Valores para o ambiente 4
'''

'''
TipoProcura.CUSTO_UNIFORME
Complexidade temporal 393
Complexidade espacial 418
TipoProcura.CUSTO_UNIFORME
Complexidade temporal 424
Complexidade espacial 434
TipoProcura.CUSTO_UNIFORME
Complexidade temporal 599
Complexidade espacial 611
Dá estes valores porque na pesquisa de custo uniforme 
é verificado primeiro os nós com um custo menor 
'''

'''
TipoProcura.SOFREGA
Complexidade temporal 412
Complexidade espacial 353
TipoProcura.SOFREGA
Complexidade temporal 167
Complexidade espacial 195
TipoProcura.SOFREGA
Complexidade temporal 604
Complexidade espacial 562
Dá estes valores porque na pesquisa Sofrega
pois é pesquisado primeiro os nós mais promissores
assim o algoritmo limita-se a manter a fronteira
da árvore de procura ordenada pelos valores de
h(n), sendo sempre escolhido o nó de valor
mais baixo, ou seja, aquele que está
hipoteticamente mais próximo da solução
'''

'''
TipoProcura.AA
Complexidade temporal 230
Complexidade espacial 247
TipoProcura.AA
Complexidade temporal 233
Complexidade espacial 246
TipoProcura.AA
Complexidade temporal 419
Complexidade espacial 438
Dá estes valores porque na pesquisa A*
é verificado o custo minimo e a estimativa de custo 
sendo menor que o custo efectivo minimo
'''


