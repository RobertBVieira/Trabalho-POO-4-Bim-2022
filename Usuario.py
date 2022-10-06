# # # # # # # # # # # # # # # # # # # #
#  class - 2° Informática Matutino    #
# # # # # # # # # # # # # # # # # # # #
#      Aimêe de Oliveira Amorim       #
#      Ricardo Prestes Martins        #
#      Robert Barreto Vieira          #
#      Ryan Ribeiro Martins           #
# # # # # # # # # # # # # # # # # # # #
#      OS GAROTOS DE PROGRAMA         #
# # # # # # # # # # # # # # # # # # # #

usuarios = []
print('\033[4;31;40mREALIZE SEU CADASTRO 🖥️\x1b[39m\n')
class Usuario:
  #Construtor
  def __init__(self,nome,email,senha):
    self.nome = nome
    self.email = email
    self.senha = senha

  def cadastroUsuario(self, nome, email, senha):
    self.nome = input("Nome: ")
    self.email = input("Email: ")
    self.senha = input("Senha: ")
    
    file = open('usuario.txt', 'a+')
    file.write('\n usuario: \n')
    file.write(self.nome)



    print(nome,email,senha)
    
  def login(self):
    
    print('\033[4;31;40m\nFAÇA SEU LOGIN\x1b[39m')
    emailInformado = input("\nDigite seu Email de login: ")
    senhaInformado = input("\nDigite sua senha: ")
    
    if emailInformado == self.email and senhaInformado == self.senha:
      print("\nAcesso autorizado")
    elif emailInformado != self.email and senhaInformado != self.senha:
      print("\n⚠️ Usuário ou senha invalido⚠️")
      resp4 = input("\nDeseja alterar a senha? (sim/não): ")
      if resp4 == "sim":
        novaSenha = input("\nDigite uma nova senha: ")
        usu.setSenha(novaSenha)
    else:
      pass
  
  def getSenha(self):
      return self.senha

  def setSenha(self,novaSenha):
      self.senha = novaSenha

  def exibirUsuario(self):
      print(f"\nAs informações do usuário são:\nNome: {self.nome}\nE-mail: {self.email}\nSenha: {self.senha}")
  

    
usu = Usuario('','','')
usu.cadastroUsuario("","","")
usu.login()
usu.getSenha()
resp3 = input("\nDeseja exibir as informações do usuário? (sim/não): ")
if resp3 == "sim":
  usu.exibirUsuario()
else:
  pass