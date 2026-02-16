# Exemplo 1: ERRO - Atribuição cria referência
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)  # [1, 2, 3, 4] - lista1 também mudou!
print(lista2)  # [1, 2, 3, 4]

# Exemplo 2: Cópia com fatiamento
original = [1, 2, 3]
copia = original[:]
copia.append(4)
print(original)  # [1, 2, 3] - não mudou
print(copia)     # [1, 2, 3, 4]

# Exemplo 3: Cópia com list()
lista_a = [10, 20, 30]
lista_b = list(lista_a)
lista_b[0] = 99
print(lista_a)  # [10, 20, 30]
print(lista_b)  # [99, 20, 30]

# Exemplo 4: Cópia com copy()
import copy
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(original)  # [1, 2, 3]
print(copia)     # [1, 2, 3, 4]

# Exemplo 5: Problema com listas aninhadas (shallow copy)
original = [[1, 2], [3, 4]]
copia = original[:]
copia[0][0] = 99
print(original)  # [[99, 2], [3, 4]] - mudou!
print(copia)     # [[99, 2], [3, 4]]

# Exemplo 6: Deep copy para listas aninhadas
import copy
original = [[1, 2], [3, 4]]
copia = copy.deepcopy(original)
copia[0][0] = 99
print(original)  # [[1, 2], [3, 4]] - não mudou
print(copia)     # [[99, 2], [3, 4]]