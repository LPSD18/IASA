from pee.larg.procura_largura import ProcuraLargura
from pee.melhor_prim.procura_AA import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from sequencia.mod_prob.heur_seq import HeurSeq
from sequencia.mod_prob.problema_seq import ProblemaSeq

'''
Classe PlaneadorSeq
Nesta class é realizado o código para a aplicação e retorna-se a solução
'''
class PlaneadorSeq:

    def planear(self,trocas,array_inicial,array_final):
        problema = ProblemaSeq(array_inicial,array_final,trocas)
        mec_proc = ProcuraCustoUnif()
        mec_proc = ProcuraAA()
        heuristica = HeurSeq(array_final)
        solucao = mec_proc.procurar(problema,heuristica)
        # solucao=mec_proc.procurar(problema)
        if(solucao):
            for no in solucao:
                if(no.operador):
                    print(no.estado.array,',',no.operador)
                else:
                    print(no.estado.array)
            print("Dimensão",solucao[-1].profundidade+1)
            print("Custo",solucao[-1].custo)
            print('Complexidade temporal',mec_proc.complexidade_temporal())
            print('Complexidade especial',mec_proc.complexidade_especial())
            
        else:
            print("Não existe")
        return solucao