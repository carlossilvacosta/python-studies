# EDITAL 104-2022 2nd Stage - Selection Process - Software Testing/Python/Java - Questions

print("""Question 1 [1 pt]: Suppose that you need to describe the software test process and its importance to a 6 
      years old kid. Which characteristics would you present and why?""")

# RESPOSTA:
# Para explicar o processo de teste de software e sua importância para uma criança de 6 anos, eu simplificaria bastante, 
# usando uma linguagem simples e exemplos que ela possa entender.

# - Encontrar erros: Diria que testar software é como procurar tesouros escondidos em um mapa de piratas. Assim como os piratas procuram por 
# tesouros, os testadores procuram por erros ou bugs no software.
# - Deixar o jogo mais divertido: Explicaria que, quando encontramos e corrigimos esses erros, tornamos os jogos e aplicativos mais divertidos 
# e fáceis de usar. Assim todos podem aproveitá-los ao máximo.
# - Garantir que Funcione Bem: Compararia o teste de software a verificar se todos os brinquedos funcionam corretamente antes de brincar com eles. 
# Se um brinquedo estiver quebrado, não será tão divertido brincar com ele. Da mesma forma, se um aplicativo ou jogo tiver erros, pode não 
# funcionar corretamente e não será tão divertido usar.

print("-------------------------------------------------------------------------------------------------------------------------------------")

print("""Question 2 [2 pts]: Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) 
      difference and then return the difference.
            
            Example:
            
            input: {1, 3, 15, 11, 2},{23, 127, 235, 19, 8}
            output: 3. That is, the pair (11,8).""")

# RESPOSTA:

lista1 = [int(x) for x in input("Digite a primeira lista com os elementos separados por espaço:\n").split()]
lista2 = [int(x) for x in input("Digite a segunda lista com os elementos separados por espaço:\n").split()]
par1 = 0
par2 = 0
menor = 9999999999999

for x in lista1:
    for y in lista2:
        if menor > x - y >= 0:
            par1 = x
            par2 = y
            menor = x - y
print("{}. That is, the pair: ({},{}).".format(menor, par1, par2))

print("-------------------------------------------------------------------------------------------------------------------------------------")

print("""Question 3 [2 pts]: Suppose you own a shoe store. The supplier of this store made a mistake when packaging the shoes and delivered 
      several shoes with incorrect pairs (e.g. two left shoes, shoes with different sizes). You had the idea to create a script to be able to 
      count how many valid pairs of shoes you have received.
    
        Script input:
        The script should read from the standard input an integer number (T) with the total number of individual shoes, followed by T lines 
        containing an integer number representing the size of the shoe, followed by a white space and a character representing which foot the 
        shoe was made for (R = right or L = Left). Note: You can consider that T is always even.
        
        Script output:
        The number of valid pairs of shoes (one shoe for each foot, with the same size) after organizing them.
        Example (Note: This is just a example of input, we may use other values to test that):
            
            Input             Output
            6                 2
            43 R
            32 L
            43 L
            32 L
            40 L
            40 R
      """)

# RESPOSTA:

T = int(input("Digite o valor total de unidades de sapatos.\n"))
dic = {'R': [],
        'L': []}
pares = 0

for x in range(T):
    sapato = input("""Informe o tamanho do sapato e qual o seu lado (\"R\" para direito ou \"L\" para esquerdo), 
                   separando os valores com espaço.\n""").split()
    num = int(sapato[0])
    lado = sapato[1]
    
    if lado == 'R':
        ladoOposto = "L"
    else:
        ladoOposto = 'R'
    if num in dic[ladoOposto]:
        dic[ladoOposto].remove(num)
        pares += 1
    else:
        dic[lado].append(num)

print("Foram formados {} pares de sapatos.".format(pares))

print("-------------------------------------------------------------------------------------------------------------------------------------")

print("""Question 4: [1 pt] The Collatz Conjecture is a mathematical problem that describes a progression of numbers
      that should always return to 1. Here are the rules:

      ● Every even number you have to divide by 2
      ● Every odd number, you apply the equation 3*x+1, x being the integer
      
      Here is an example of the conjecture working with the input 40 as the starting integer, following the
      rules, it would follow these steps:

      40 20 10 5 16 8 4 2 1

      You have to implement a program that applies these rules to any integer.
      
      Input:
      ● An integer N which will be your starting number. Where N>0.
      ● The input ends when N=0
      
      Output:
      ● The series of numbers leading to 1, formatted as such:

      Sequence = (40, 20, 10, 5, 16, 8, 4, 2, 1) (from the example).""")

# RESPOSTA:

numero = int(input("Digite um número inteiro N(N>0): "))

while numero <= 0:
    numero = int(input("O número digitado deve ser um inteiro positivo: "))

sequencia = [numero]

while numero > 1:
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = numero * 3 + 1
    sequencia.append(numero)

print(f"Sequencia = {sequencia}")

print("-------------------------------------------------------------------------------------------------------------------------------------")

print("""Question 5 [4 pts]:

You must use your knowledge on object oriented design to implement a Vending Machine which:

      ● Accepts coins of 1,5,10,25 Cents
      ● Allow user to select products Coke(25), Pepsi(35), Soda(45)
      ● Allow the user to take a refund by canceling the request.
      ● Return selected product and remaining change if any
      ● Allow reset operation for vending machine suppliers.

Note:
      ● You don't need to implement a menu option
      ● Implement all the methods and class needed
      ● Feel free to comment explaining the function of each method""")

# RESPOSTA:

class MaquinaDeVendas:
    def __init__(self):
        self.saldo = 0
        self.produtos = {"Coca-Cola": 25, "Pepsi": 35, "Soda": 45}

    def inserir_moeda(self, moeda):
        if moeda in [1, 5, 10, 25]:
            self.saldo += moeda
        else:
            print("Moeda inválida! Moedas aceitas: 1, 5, 10, 25 centavos")

    def selecionar_produto(self, produto):
        if produto in self.produtos:
            preco = self.produtos[produto]
            if self.saldo >= preco:
                self.saldo -= preco
                return produto, self.saldo
            else:
                return "Saldo insuficiente. Por favor, insira mais moedas.", self.saldo
        else:
            return "Seleção de produto inválida.", self.saldo

    def cancelar_pedido(self):
        reembolso = self.saldo
        self.saldo = 0
        return f"Pedido cancelado. Reembolso: {reembolso} centavos"

    def resetar(self):
        self.saldo = 0
        return "Maquina de vendas resetada com sucesso. Saldo zerado."

# Exemplo de uso:
mv = MaquinaDeVendas()
mv.inserir_moeda(25)
print(mv.selecionar_produto("Coca-Cola"))
print(mv.cancelar_pedido())

## OUTRA MANEIRA DE RESPOSTA DA QUESTÃO:

def vending_machine():
    global creditoTotal
    
    print("Bem-vindo a máquina de vendas!")
    print("Aceitamos moedas de 0.01, 0.05, 0.10 ou 0.25 centavos.")
    
    list = [0.01, 0.05, 0.10, 0.25]
    creditoTotal = 0

    while True:
        moedaValor = float(input("Adicione o valor que deseja inserir: \n"))
        if moedaValor not in list:
            print("O valor inserido não é aceito, insira uma das seguintes moedas: 0.01, 0.05, 0.10 ou 0.25 centavos.")
            print("Você receberá um reembolso.")
        else:
            creditoTotal += moedaValor
        flag = str(input("Você deseja inserir outra moeda? [S/N] "))
        if flag in 'Nn':
            break
    produtos(creditoTotal)

def produtos(creditoTotal):
    global creditoFinal
    creditoFinal = 0
    print("Você possui {:.2f} disponível.".format(creditoTotal))
    print("")
    print("1. Coke -> 25 centavos")
    print("2. Pepsi -> 35 centavos")
    print("3. Soda -> 45 centavos")
    print("")
    item = int(input("Insira o número do item desejado: \n"))
    while 1 > item > 3:
        print("Este não é um valor válido.")
        item = int(input("Insira o número do item desejado: "))
    if item == 1:
        creditoFinal = creditoTotal - 0.25
        print("Você acaba de adquirir uma Coke, custando R$ 0.25.")
        print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
    elif item == 2:
        creditoFinal = creditoTotal - 0.35
        print("Você acaba de adquirir uma Pepsi, custando R$ 0.35.")
        print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
    elif item == 3:
        creditoFinal = creditoTotal - 0.45
        print("Você acaba de adquirir uma Soda, custando R$ 0.45.")
        print("Você possui R${:.2f} no seu saldo final.".format(creditoTotal))
    confirmacao()

def confirmacao():
    validacao = str(input("Você confirma o pedido? [S/N] "))
    if validacao in 'Nn':
        print(f"Você será reembolsado ${creditoTotal}.")
        produtos(creditoTotal)
    else:
        print("Você receberá {:.2f} como troco.".format(creditoFinal))
        print("Pode retirar o produto.")

vending_machine()