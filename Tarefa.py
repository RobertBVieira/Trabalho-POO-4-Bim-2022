listaTarefas = []

from Compromisso import *

class Tarefa(compromisso):
  def __init__(self,estadoMeta):
    self.estadoMeta = None
    
  def tarefas_comp(self):
    super().criar_compromisso()
    super().modificar_compromisso()
  
cumprir = Tarefa("")
cumprir.tarefas_comp()
    