from ecr.comport_comp import ComportComp

'''
Classe Prioridade
Herança de ComportComp
'''

class Prioridade(ComportComp):
    
    '''
    Método selecionar_accao(accoes)

    Seleção por prioridade

    1- Analisar as propriedades de cada accao
    2- Retornar a accao com maior prioridade

    Funcão lambda -->A lambda function is a small anonymous function.
                     A lambda function can take any number of arguments, 
                     but can only have one expression

    @param List<Accao>
    @return Accao
    '''

    def selecionar_accao(self,accoes):
        print('Accoes->',accoes)
        accao_selecionada = max(accoes,key=lambda a:a.prioridade)
        return accao_selecionada