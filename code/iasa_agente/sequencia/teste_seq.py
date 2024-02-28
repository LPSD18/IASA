from sequencia.mod_prob.operador_seq import OperadorSeq
from sequencia.mod_prob.planeador_seq import PlaneadorSeq


ARRAY_INICIAL = [3,6,4,2,5,1]
ARRAY_FINAL =   [1,2,3,4,5,6]
TROCAS = [OperadorSeq(0,1),
          OperadorSeq(0,2),
          OperadorSeq(0,3),
          OperadorSeq(0,4),
          OperadorSeq(0,5),
          OperadorSeq(1,2),
          OperadorSeq(1,3),
          OperadorSeq(1,4),
          OperadorSeq(1,5),
          OperadorSeq(2,3),
          OperadorSeq(2,4),
          OperadorSeq(2,5),
          OperadorSeq(3,4),
          OperadorSeq(3,5),
          OperadorSeq(4,5)]

planeador = PlaneadorSeq()
solucao = planeador.planear(TROCAS,ARRAY_INICIAL,ARRAY_FINAL)
