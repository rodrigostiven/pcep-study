# Exemplo 1: Ordem importa
def subtrair(a, b):
    return a - b

print(subtrair(10, 3))  # 7
print(subtrair(3, 10))  # -7 (ordem diferente, resultado diferente)

# Exemplo 2: Função com 3 parâmetros
def apresentar(nome, idade, cidade):
    print(f"{nome}, {idade} anos, mora em {cidade}")

apresentar("João", 25, "São Paulo")

# Exemplo 3: Erro por falta de argumento
def somar(a, b):
    return a + b

# print(somar(5))  # TypeError: falta 1 argumento

# Exemplo 4: Erro por excesso de argumentos
# print(somar(5, 3, 2))  # TypeError: muitos argumentos