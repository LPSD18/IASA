from ecr.comport_comp import ComportComp

'''
Classe Hierarquia
Herança de ComportComp
'''

class Hierarquia(ComportComp):
    
    '''
    Método seleccionar_accao(accoes)

    Método que seleciona a accao dependendo da sua hierarquia
    Os primeiros atributos da lista é os que tem maior uma hierarquia maior
    irá sempre fazer return da primeira accao da lista
    Subsunção

    @param List<Accao>
    @return Accao
    '''
    def selecionar_accao(self,accoes):
        if(len(accoes)>0):
             return accoes[0]