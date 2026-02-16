# Exemplo 1: Iterando por chaves (padrão)
pessoa = {"nome": "João", "idade": 25, "cidade": "SP"}

for chave in pessoa:
    print(chave)

# Exemplo 2: Iterando por chaves e valores
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")

# Exemplo 3: Usando items()
for chave, valor in pessoa.items():
    print(f"{chave} = {valor}")

# Exemplo 4: Iterando apenas por valores
for valor in pessoa.values():
    print(valor)

# Exemplo 5: Iterando apenas por chaves explicitamente
for chave in pessoa.keys():
    print(chave)

# Exemplo 6: Exemplo prático - contagem de votos
votos = {"Ana": 45, "Bruno": 38, "Carlos": 52}
total = 0
for candidato, quantidade in votos.items():
    print(f"{candidato}: {quantidade} votos")
    total += quantidade
print(f"Total de votos: {total}")