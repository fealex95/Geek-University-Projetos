from models.cliente import Cliente
from models.conta import Conta



Pessoa: Cliente = Cliente('Felipe Alexandre', 'felipealexandre98@gmail.com', '123.123.123-01', '17/01/1995')
conta: Conta = Conta(Pessoa)

print(Pessoa)
print(conta)
