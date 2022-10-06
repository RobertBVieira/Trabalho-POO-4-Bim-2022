listaMetas = []

from Compromisso import *

class Metas(compromisso):
  def __init__(self,visualizarMetas):
    self.visualizarMetas = None
    
  def metas_comp(self):
    super().criar_compromisso()
    super().modificar_compromisso()
    
  def ListaMetas(self):
    print(ListaMetas)

atingir = Metas("")
atingir.metas_comp()


