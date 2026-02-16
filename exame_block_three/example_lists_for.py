# Exemplo 1: Iteração simples
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print("Eu gosto de", fruta)

# Exemplo 2: Iteração com índice usando range()
cores = ["vermelho", "azul", "verde"]
for i in range(len(cores)):
    print(f"Índice {i}: {cores[i]}")

# Exemplo 3: enumerate() - índice e valor
animais = ["gato", "cachorro", "pássaro"]
for indice, animal in enumerate(animais):
    print(f"{indice}: {animal}")

# Exemplo 4: Somando elementos
numeros = [10, 20, 30, 40, 50]
soma = 0
for num in numeros:
    soma += num
print("Soma:", soma)  # 150

# Exemplo 5: Encontrando o maior
valores = [23, 45, 12, 67, 34]
maior = valores[0]
for valor in valores:
    if valor > maior:
        maior = valor
print("Maior valor:", maior)  # 67