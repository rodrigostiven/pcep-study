# Exemplo 1: remove() - remove primeira ocorrência
numeros = [1, 2, 3, 2, 4, 2]
numeros.remove(2)
print(numeros)  # [1, 3, 2, 4, 2] (remove apenas o primeiro 2)

# Exemplo 2: pop() - remove e retorna elemento
frutas = ["maçã", "banana", "laranja"]
ultima = frutas.pop()      # Remove último
print(ultima)              # laranja
print(frutas)              # ['maçã', 'banana']

primeira = frutas.pop(0)   # Remove do índice 0
print(primeira)            # maçã
print(frutas)              # ['banana']

# Exemplo 3: clear() - limpa a lista
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)  # []

# Exemplo 4: count() - conta ocorrências
numeros = [1, 2, 2, 3, 2, 4, 2]
print("Quantidade de 2:", numeros.count(2))  # 4

# Exemplo 5: reverse() - inverte a lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)  # [5, 4, 3, 2, 1]

# Exemplo 6: sort() - ordena a lista
numeros = [5, 2, 8, 1, 9]
numeros.sort()
print(numeros)  # [1, 2, 5, 8, 9]

numeros.sort(reverse=True)
print(numeros)  # [9, 8, 5, 2, 1]