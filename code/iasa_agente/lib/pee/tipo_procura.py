from enum import Enum

'''
Classe Enumerado para definir que tipo de procura utilizar
Recebe um valor (1,2 ou 3) e por ai é definido o tipo de procura
'''
class TipoProcura(Enum):
    CUSTO_UNIFORME = 1
    SOFREGA = 2
    AA = 3