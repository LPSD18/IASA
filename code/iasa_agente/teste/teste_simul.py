from sae import Controlo
from sae import Simulador


#________________________________________________________________________________________________________________
#Controlo de teste

class ControloTeste(Controlo):
    def processar(self,percepcao):
        print("processar")

#________________________________________________________________________________________________________________
# Activação

controlo = ControloTeste()
Simulador(4,controlo).executar()