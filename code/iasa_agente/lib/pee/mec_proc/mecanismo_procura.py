from abc import ABC, abstractmethod, abstractproperty

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

'''
Classe MecanismoProcura
Classe Abstrata para ser utilizada por outras classes

numero total de nos processados
numero maximo de nos acumulados
'''
class MecanismoProcura(ABC):

    '''
    método construtor da classe onde se inicia uma instancia da classe fronteira

    @param fronteira
    '''
    def __init__(self, fronteira):  
        self._fronteira=fronteira
        '''
        atributos utilizados para número total de nos processados e número máximo de nos processados
        '''
        self.__nos_processados = 0
        self.__maximo = 0
    
    '''
    getter do atritubuto "total"
    '''
    @property
    def total(self):
        return self.__total
    
    '''
    setter do atritubuto "total"
    '''
    @total.setter
    def total(self,num):
        self.__total=num

    '''
    getter do atritubuto "maximo"
    '''
    @property
    def maximo(self):
        return self.__maximo
    
    '''
    setter do atritubuto "maximo"
    '''
    @maximo.setter
    def maximo(self,num):
        self.__maximo=num
    
    '''
    ativa a instancia de fronteira

    @return lista vazia de nos
    '''
    def _iniciar_memoria(self):

        return self._fronteira.iniciar()
        '''
        '''
    '''
    método abstrato

    método que memoriza os nós sucessores do nó inicial do método

    @param no
    '''
    @abstractmethod
    def _memorizar(self,no):

        '''
        '''
    '''
    1- iniciar a memoria do mecanismo
    2- criar um nó inicial com o estado inicial do problema dado
    3- inserir o nó na fronteira
    4- enquanto a fronteira não for vazia remover o nó da fronteira
    5- se o estado do no for o objetivo return da solucao com o no
    6- se não for então utilizar o método de expandir desta classe num For e memorizar os nós sucessores da fronteira

    @param problema
    @return Solucao
    '''
    def procurar(self,problema):
        
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        '''
        # atributo de ajuda para o numero total de nós processados
        '''
        help1=0
        
        self._fronteira.inserir(no)

        '''
        # atualiza de inicio com o tamanho de nós na fronteira
        '''
        # self.maximo(len(self._fronteira._nos))
        while  self._fronteira.vazia is False:
            
            no_rem = self._fronteira.remover()

            
            # parte de codigo que verifica se o tamanho atual de fronteira é maior que o antigo e se for verdade atualiza o valor do atributo "maximo" 
            if(self.maximo<(self._fronteira.len_nos())):
                self.maximo=self._fronteira.len_nos()
                # '''
                # VER AQUI CORRIGIR ISTO
                # '''
            if(problema.objectivo(no_rem.estado)):
                self.__nos_processados = help1
                return Solucao(no_rem)
            else:
                help1+=1
                for no_suc in self._expandir(problema,no_rem):
                    self._memorizar(no_suc)
        
    '''
    1- ver para cada operador o estado sucessor do estado do nó dado no método
    2- se o estado sucessor for um estado utilizar a função yield para criar um No com o estado sucessor, o operador atual e o no dado no método
    Yield are used in Python generators.
    A generator function is defined like a normal function, 
    but whenever it needs to generate a value, 
    it does so with the yield keyword rather than return

    @param problema
    @param no
    @yield<No>
    '''
    def _expandir(self,problema,no):
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if(estado_suc):
                yield No(estado_suc,operador,no)
        '''
        '''
    
    def complexidade_temporal(self):
        # print(self.__nos_processados)
        return self.__nos_processados
    
    @abstractproperty
    def complexidade_especial(self):
        '''Número máximo de nós em memória
        '''