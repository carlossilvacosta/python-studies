nome = "Carlos"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome":  "Carlos", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))

print("---------------------------------------------------")

print("Nome: {} Idade: {}".format(nome, idade))

print("---------------------------------------------------")

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1} {1}".format(idade, nome))

print("---------------------------------------------------")

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} Nome: {name} {name} {name}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print("---------------------------------------------------")

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")