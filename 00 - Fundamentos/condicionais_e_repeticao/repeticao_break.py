# break-while
while True:
    numero = int(input("Informe o número: "))

    if numero == 10:
        break
print(numero)

# break-for
for numero in range(100):
    if numero == 10:
        break
    print(numero, end=" ")

# continue / continue pula o número
for numero in range(100):
    if numero == 10:
        continue
    print(numero, end=" ")