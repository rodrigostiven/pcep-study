# Exemplo 1: Comparação de sintaxe
lista = [1, 2, 3]
tupla = (1, 2, 3)

# Exemplo 2: Mutabilidade
lista[0] = 10      # OK
# tupla[0] = 10    # ERRO!

# Exemplo 3: Métodos disponíveis
print(dir(lista))  # Muitos métodos
print(dir(tupla))  # Poucos métodos

# Exemplo 4: Performance (tuplas são mais rápidas)
import sys
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
print("Tamanho lista:", sys.getsizeof(lista))
print("Tamanho tupla:", sys.getsizeof(tupla))

# Exemplo 5: Uso como chave de dicionário
# dicionario = {[1, 2]: "valor"}  # ERRO: lista não é hashable
dicionario = {(1, 2): "valor"}    # OK: tupla é hashable
print(dicionario)

# Exemplo 6: Desempacotamento
coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}")