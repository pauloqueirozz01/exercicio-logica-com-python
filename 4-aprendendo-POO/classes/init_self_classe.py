class Account:

  ## Para iniciar um metodo construtor nós podemos usar um metodo nativo do python chamendo a def __init__()
  def __init__(self, nameAccount, balanceAccount ):
    self.nameAccount = nameAccount
    self.balanceAccount = balanceAccount

  # Passando funções que podem ser utilizadas pelas instâncias da Classe.

  # Imprime o saldo atual da conta
  def check_balance(self):
    print(f"Saldo atual da conta: R$ {self.balanceAccount}")

  # Imprime o Nome do titular da conta
  def check_nameAccount(self):
    print(f"Titular da conta: {self.nameAccount}")

  # Lista todas as informações da Conta (nome e saldo do titular)
  def list_details(self):
    print(f"Mostrando informações da Conta:")
    self.check_balance(),
    self.check_nameAccount()

  # Operação de depósito bancário
  def deposit(self):
    value = int(input("Digite o valor que você quer depositar:"))
    self.balanceAccount += value
    print(f"Você fez um depósito no valor de: R$ {value}")
    self.check_balance()

  # Operação de Transferência Bancária

account_paulo = Account("Paulo", 60021)
account_paulo.list_details()
account_paulo.deposit()
