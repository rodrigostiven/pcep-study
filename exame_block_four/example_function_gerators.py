# Exemplo 1: Função geradora simples
def contador(max):
    n = 0
    while n < max:
        yield n
        n += 1

for num in contador(5):
    print(num)  # 0 1 2 3 4

# Exemplo 2: Gerador de números pares
def pares(max):
    n = 0
    while n <= max:
        yield n
        n += 2

for num in pares(10):
    print(num, end=" ")  # 0 2 4 6 8 10

# Exemplo 3: Diferença entre return e yield
def com_return():
    return 1
    return 2  # Nunca executado

def com_yield():
    yield 1
    yield 2

print(com_return())  # 1
for valor in com_yield():
    print(valor)  # 1, depois 2

# Exemplo 4: Gerador infinito
def numeros_infinitos():
    n = 0
    while True:
        yield n
        n += 1

# Cuidado! Este loop é infinito
# for num in numeros_infinitos():
#     print(num)

# Uso controlado:
gen = numeros_infinitos()
for _ in range(5):
    print(next(gen))  # 0 1 2 3 4