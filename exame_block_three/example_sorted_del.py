# Exemplo 1: sorted() - retorna nova lista ordenada
original = [5, 2, 8, 1, 9]
ordenada = sorted(original)
print("Original:", original)    # [5, 2, 8, 1, 9]
print("Ordenada:", ordenada)    # [1, 2, 5, 8, 9]

# Exemplo 2: sorted() decrescente
numeros = [3, 1, 4, 1, 5, 9, 2]
desc = sorted(numeros, reverse=True)
print(desc)  # [9, 5, 4, 3, 2, 1, 1]

# Exemplo 3: del - deleta elemento por índice
frutas = ["maçã", "banana", "laranja", "uva"]
del frutas[1]
print(frutas)  # ['maçã', 'laranja', 'uva']

# Exemplo 4: del com fatiamento
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numeros[2:5]
print(numeros)  # [0, 1, 5, 6, 7, 8, 9]

# Exemplo 5: del - deleta a lista inteira
lista = [1, 2, 3]
del lista
# print(lista)  # NameError: lista não existe mais