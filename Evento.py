listaEvento = []

from Compromisso import *

class Evento(compromisso):
  def __init__(self, localEvento):
    self.localEvento = None
    
  def event_comp(self):
    super().criar_compromisso()
    super().modificar_compromisso()
    
  def ListaEventos(self):
    print(ListaEvento)

marcar = Evento ("")
marcar.event_comp()