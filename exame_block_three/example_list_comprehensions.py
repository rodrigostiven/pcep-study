# Exemplo 1: Criando lista de quadrados
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)  # [1, 4, 9, 16, 25]

# Exemplo 2: Filtrando números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]

# Exemplo 3: Convertendo para maiúsculas
palavras = ["python", "java", "c++"]
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)  # ['PYTHON', 'JAVA', 'C++']

# Exemplo 4: Multiplicando por 2
original = [1, 2, 3, 4, 5]
dobro = [x * 2 for x in original]
print(dobro)  # [2, 4, 6, 8, 10]

# Exemplo 5: Compreensão com condição
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares_quadrados = [x**2 for x in numeros if x % 2 != 0]
print(impares_quadrados)  # [1, 9, 25, 49, 81]

# Exemplo 6: If-else em compreensão
numeros = [1, 2, 3, 4, 5]
resultado = ["par" if x % 2 == 0 else "ímpar" for x in numeros]
print(resultado)  # ['ímpar', 'par', 'ímpar', 'par', 'ímpar']