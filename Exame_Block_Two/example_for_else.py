# Exemplo 1: Busca em lista

numeros = [2, 4, 8, 10]
procurar = 7

for num in numeros:
    if num == procurar:
        print("Número encontrado!")
        break
else:
    print("Número não encontrado na lista")