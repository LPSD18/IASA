from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Simulador

# controlo = ControloDelib(PlaneadorPDM())
controlo = ControloDelib(PlaneadorPDM(0.95,1))
Simulador(4,controlo).executar()

'''
Ambiente 4(porque não funciona)
Não funciona pelo tamanho do ambiente 4 ser maior que o do ambiente 3
necessário aumentar o gama do planeadorPDM pelo facto do espaço temporal ser um valor pequeno anteriormente

'''