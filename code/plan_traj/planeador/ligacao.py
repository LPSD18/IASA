from dataclasses import dataclass

'''
Classe Ligação
tipo dataclass
'''
@dataclass
class Ligacao():
    origem:str
    destino:str
    custo:int
        