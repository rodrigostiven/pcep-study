# Exemplo 1: Tuplas são imutáveis
coordenadas = (10, 20)
# coordenadas[0] = 15  # TypeError: não pode modificar!

# Exemplo 2: Pode criar nova tupla
coord_antiga = (10, 20)
coord_nova = (15, 20)
print(coord_nova)

# Exemplo 3: Concatenação cria nova tupla
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)  # (1, 2, 3, 4, 5, 6)

# Exemplo 4: Repetição
tupla = (1, 2)
repetida = tupla * 3
print(repetida)  # (1, 2, 1, 2, 1, 2)

# Exemplo 5: Métodos disponíveis (apenas 2!)
numeros = (1, 2, 3, 2, 4, 2)
print(numeros.count(2))   # 3
print(numeros.index(3))   # 2