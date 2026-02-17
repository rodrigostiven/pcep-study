# Exemplo 1: Função simples sem parâmetros

def saudacao():
    print("Olá, mundo!")

saudacao() # Chamando a função

# Exemplo 2: Função com parâmetros

def saudar_pessoa(nome):
    print(f"Olá, {nome}!")

saudar_pessoa("João")

# Exemplo 3: Função com múltiplos parâmetros

def somar(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

somar(5, 3)

# Exemplo 4: Função sem execução (pass)

def funcao_futura():
    pass # Será implementada depois

funcao_futura()  # Não faz nada, mas não gera erro

# Exemplo 5: Chamando função dentro de outra

def dobro(x):
    return x * 2

def quadruplo(x):
    return dobro(dobro(x))

print(quadruplo(5))