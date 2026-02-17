# Exemplo 1: Fatorial recursivo
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # 120 (5 * 4 * 3 * 2 * 1)

# Exemplo 2: Fibonacci recursivo
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")  # 0 1 1 2 3 5 8 13

# Exemplo 3: Contagem regressiva
def contagem_regressiva(n):
    if n <= 0:
        print("Fim!")
    else:
        print(n)
        contagem_regressiva(n - 1)

contagem_regressiva(5)

# Exemplo 4: Soma de lista recursiva
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

print(soma_lista([1, 2, 3, 4, 5]))  # 15

# Exemplo 5: Potência recursiva
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

print(potencia(2, 5))  # 32