'''
Módulo test planeamento trajeto
'''

from plan_traj.planeador.ligacao import Ligacao
from plan_traj.planeador.planeador_trajecto import PlaneadorTrajecto


LIGACOES = [Ligacao("Loc-0","Loc-1",5),
            Ligacao("Loc-0","Loc-2",25),
            Ligacao("Loc-1","Loc-3",12),
            Ligacao("Loc-1","Loc-6",5),
            Ligacao("Loc-2","Loc-4",30),
            Ligacao("Loc-3","Loc-2",10),
            Ligacao("Loc-3","Loc-5",5),
            Ligacao("Loc-4","Loc-3",2),
            Ligacao("Loc-5","Loc-6",8),
            Ligacao("Loc-5","Loc-4",10),
            Ligacao("Loc-6","Loc-3",15)]

loc_inicial = "Loc-0"
loc_final = "Loc-4"

planeador = PlaneadorTrajecto()
solucao = planeador.planear(LIGACOES,loc_inicial,loc_final)

if solucao:
    while no := solucao.remover():
        print(no.estado,":",no.operador)
else:
    print("Não existe solucao")


'''
Suposto aparecer
loc0:None
loc1:Loc0->Loc1
loc3:loc1->loc3
loc5:loc3->loc5
loc4:loc5->loc4
'''

'''
Resultados Obtidos
ProcuraCustoUnif()
Loc-0 : None
Loc-1 : Loc-0 -> Loc-1
Loc-3 : Loc-1 -> Loc-3
Loc-5 : Loc-3 -> Loc-5
Loc-4 : Loc-5 -> Loc-4

ProcuraProfLim()
Loc-0 : None
Loc-2 : Loc-0 -> Loc-2
Loc-4 : Loc-2 -> Loc-4

ProcuraProfIter()
Loc-0 : None
Loc-2 : Loc-0 -> Loc-2
Loc-4 : Loc-2 -> Loc-4

ProcuraLargura()
Loc-0 : None
Loc-2 : Loc-0 -> Loc-2
Loc-4 : Loc-2 -> Loc-4
'''