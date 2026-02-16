# Exemplo 1: Lista dentro de tupla
tupla_com_lista = (1, 2, [3, 4, 5])
print(tupla_com_lista)

# A tupla é imutável, mas a lista dentro pode mudar!
tupla_com_lista[2].append(6)
print(tupla_com_lista)  # (1, 2, [3, 4, 5, 6])

# Exemplo 2: Tupla dentro de lista
lista_com_tupla = [1, 2, (3, 4, 5)]
print(lista_com_tupla)

# A lista pode mudar, mas a tupla dentro não
lista_com_tupla.append(6)
print(lista_com_tupla)  # [1, 2, (3, 4, 5), 6]

# lista_com_tupla[2][0] = 10  # ERRO: tupla é imutável

# Exemplo 3: Estrutura mista complexa
dados = [
    ("João", 25, [90, 85, 88]),
    ("Maria", 23, [95, 92, 89]),
    ("Pedro", 24, [78, 82, 85])
]

for nome, idade, notas in dados:
    media = sum(notas) / len(notas)
    print(f"{nome}, {idade} anos, média: {media:.1f}")