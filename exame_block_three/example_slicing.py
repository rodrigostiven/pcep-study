# Exemplo 1: Fatiamento básico
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])    # [2, 3, 4] (do índice 2 até 4)
print(numeros[:4])     # [0, 1, 2, 3] (do início até 3)
print(numeros[5:])     # [5, 6, 7, 8, 9] (do 5 até o fim)
print(numeros[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (cópia completa)

# Exemplo 2: Fatiamento com step
print(numeros[::2])    # [0, 2, 4, 6, 8] (de 2 em 2)
print(numeros[1::2])   # [1, 3, 5, 7, 9] (ímpares)
print(numeros[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (invertido)

# Exemplo 3: Fatiamento negativo
letras = ['a', 'b', 'c', 'd', 'e', 'f']
print(letras[-3:])     # ['d', 'e', 'f'] (últimos 3)
print(letras[:-2])     # ['a', 'b', 'c', 'd'] (exceto últimos 2)
print(letras[-4:-1])   # ['c', 'd', 'e']

# Exemplo 4: Modificando fatias
numeros = [1, 2, 3, 4, 5]
numeros[1:4] = [20, 30, 40]
print(numeros)  # [1, 20, 30, 40, 5]