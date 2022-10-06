lista_compromisso = []

class compromisso:
  def __init__(self,nome_compromisso,data_compromisso,hora_compromisso,descricao_compromisso,lista_compromisso):
    self.nome_compromisso = nome_compromisso
    self.data_compromisso = data_compromisso
    self.hora_compromisso = hora_compromisso
    self.descricao_compromisso = descricao_compromisso
    self.lista_compromisso = lista_compromisso
    
  def criar_compromisso(self):
    self.nome_compromisso = input("\nNome do compromisso: ")
    self.data_compromisso = input("\nData do compromisso: ")
    self.hora_compromisso = input("\nHora do compromisso: ")
    self.descricao_compromisso = input("\nDescrição do compromisso: ")
    
    file = open('compromisso.txt', 'a+')
    file.write('\n compromisso: \n')
    file.write(self.nome_compromisso,)

  def getvisualizar_compromisso(self):
    return self.lista_compromisso
    
  def apagar_compromisso(self):
    self.lista_compromisso.remove(self.nome_compromisso)
    
  def modificar_compromisso(self):
    resp2 = input("\nDeseja alterar o compromisso? (sim/não): ")
    if resp2 == "sim":
      self.nome_compromisso = input("\nNome do compromisso: ")
      self.data_compromisso = input("\nData do compromisso: ")
      self.hora_compromisso = input("\nHora do compromisso: ")
      self.descricao_compromisso = input("\nDescrição do compromisso: ")
    else:
      pass
    file = open('compromisso.txt', 'a+')
    file.write('compromisso:  \n')
    file.write(self.nome_compromisso)
      
casinha = compromisso("","","","","")