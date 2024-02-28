from pee.mec_proc.fronteira.fronteira_prioridade import FronteiraPrioridade
from pee.mec_proc.procura_grafo import ProcuraGrafo

'''
Classe ProcuraMelhorPrim
Herança de ProcuraGrafo
Classe utilizada no estudo de procura onde vai pelo melhor nó primeiro

Procura melhor-primeiro:
• Criar nó inicial
• Iniciar fronteira
• Iniciar explorados
• Enquanto fronteira não vazia
    • Remover primeiro nó da
    fronteira
    • Verificar se estado é
    objectivo
    • Expandir nó
    • Por cada nó sucessor
        • Se nó ainda não foi
        explorado ou se é melhor
            • Juntar nó aos explorados
            • Juntar nó à fronteira
• Caso fronteira vazia indicar que não existe solução
'''
class ProcuraMelhorPrim(ProcuraGrafo):

    '''
    Método construtor da classe
    Utiliza o super construtor e a classe FronteiraPrioridade como atributo desse construtor
    na classe FronteiraPrioridade utilizar o parametro avaliador

    @param avaliador
    '''
    def __init__(self,avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador=avaliador


    '''
    • Se nó ainda não foi explorado ou se é melhor
        • Juntar nó aos explorados
        • Juntar nó à fronteira

        Verificar se o no já existe ou não no dict de explorados com o método da super classe
        se já existir verificar o custo e retornar se é menor ou maior que o custo do nó dentro do dict de explorados
    

    @param no
    @return boolean
    '''
    def _manter(self, no):

        return super()._manter(no) or (no<self._explorados[no.estado])


