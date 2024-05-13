nome = "cArLoS"

print(nome.upper())
print(nome.lower())
print(nome.title())

print("----------------------------------------")

texto = "   Olá Mundo!    "

print(texto  + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

print("----------------------------------------")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))