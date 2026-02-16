# Exemplo 1: Iterando por string

palavra = "Python"
for letra in palavra:
    print(letra)

# Exemplo 2: Iterando por lista

frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print("Eu gosto de: ", fruta)

# Exemplo 3: Contando vogais
texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1
print("Número de vogais:", contador)