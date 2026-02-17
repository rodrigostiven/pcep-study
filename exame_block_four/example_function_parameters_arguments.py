# Exemplo 1: Conceito básico
def saudar(nome):  # 'nome' é um PARÂMETRO
    print(f"Olá, {nome}!")

saudar("João")  # "João" é um ARGUMENTO

# Exemplo 2: Múltiplos parâmetros
def calcular_area(largura, altura):  # Parâmetros
    return largura * altura

area = calcular_area(5, 10)  # 5 e 10 são argumentos
print(area)

# Exemplo 3: Parâmetros são variáveis locais
def dobrar(x):
    x = x * 2
    return x

numero = 5
resultado = dobrar(numero)
print(numero)    # 5 (não mudou)
print(resultado) # 10