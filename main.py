from Usuario import*
perg1 = input ('\nEscolha um tipo de compromisso: \n1-evento\n2-metas\n3-tarefas\nR: ')

if perg1 == 'evento' or perg1 == "1":
  from Evento import*
if perg1 == 'metas' or perg1 == "2":
  from Metas import*
if perg1 == 'tarefa' or perg1 == "3":
  from Tarefa import*


usu = Usuario("","","")

usuarios.append(usu)

print(usuarios)

