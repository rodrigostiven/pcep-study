# Exemplo 1: range com 1 parâmetro (stop)

for i in range(5):
    print(i) # Saída: 0, 1, 2, 3, 4

# Exemplo 2: range com 2 parâmetros (start, stop)

for i in range(1, 6):
    print(i) # Saída 1, 2, 3, 4, 5

# Exemplo 3: range com 3 parâmetros (start, stop, step)

for i in range(0, 11, 2):
    print(i) # 0, 2, 4, 6, 8, 10

# Exemplo 4: range decrescente

for i in range(10, 0, -1):
    print(i) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Exemplo 5: Tabuada com for

numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")