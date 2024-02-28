from pee.mec_proc.no import No
from pee.prof.procura_profundidade import ProcuraProfundidade


'''
Classe ProcuraProfLim
Herança de ProcuraProfundidade

Procura em profundidade limitada:
• Iniciar fronteira
• Iniciar resultado
• Enquanto fronteira não vazia
    • Remover primeiro nó da fronteira
    • Verificar se estado é objectivo
    • Se profundidade máxima
        • Não existe solução
    • Senão, se não existe ciclo
        • Expandir nó
        • Por cada nó sucessor
            • Juntar nó à fronteira
• Retornar resultado
'''
class ProcuraProfLim(ProcuraProfundidade):


    '''
    Método construtor

    @param prof_max (int)--> Profundidade maxima da profundidade

    '''
    def __init__(self,prof_max=100):
        #Profundidade máxima da procura
        self.__prof_max=prof_max
        super().__init__()
        
    '''
    getter do prof_max
    @return self.__prof_max
    '''
    @property
    def prof_max(self):
        return self.__prof_max
    
    '''
    setter do prof_max

    @param num
    '''
    @prof_max.setter
    def prof_max(self,num):
        self.__prof_max=num


    '''
    Método expandir
    Expande nó se a sua profundidade for inferior à
    profundidade máxima da procura


    @param problema
    @param no
    
    '''
    def _expandir(self,problema,no):
        # print('ola')
        if no.profundidade<self.prof_max:
            # print('ola')
            yield from super()._expandir(problema,no)
        # if no.profundidade <self.pr
        '''
        '''

    '''
    Método memorizar 
    Memoriza nó se não corresponder a um ciclo

    @param no

    '''
    def _memorizar(self, no):
        if(not self._ciclo(no)):
            super()._memorizar(no)
        '''
        '''
    
    '''
    Método Ciclo
    Verifica se nó corresponde a um ciclo no ramo
    respectivo, para evitar a expansão de nós referentes a
    estados já explorados (não evita ciclos em relação a
    outros ramos)

    @param no
    @return boolean
    '''
    def _ciclo(self,no):
        no_ramo = no.antecessor
        while no_ramo:
            if no.estado == no_ramo.estado:
                return True
            no_ramo = no_ramo.antecessor
        return False
        '''
        '''