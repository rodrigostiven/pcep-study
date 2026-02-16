# Exemplo 1: Criando tuplas
tupla_vazia = ()
numeros = (1, 2, 3, 4, 5)
frutas = ("maçã", "banana", "laranja")
mista = (1, "texto", 3.14, True)

print(numeros)
print(frutas)

# Exemplo 2: Tupla com um elemento (precisa da vírgula!)
tupla_um = (5,)
print(type(tupla_um))  # <class 'tuple'>

nao_tupla = (5)
print(type(nao_tupla))  # <class 'int'>

# Exemplo 3: Tupla sem parênteses
coordenadas = 10, 20, 30
print(type(coordenadas))  # <class 'tuple'>
print(coordenadas)        # (10, 20, 30)

# Exemplo 4: Indexação (igual listas)
cores = ("vermelho", "azul", "verde", "amarelo")
print(cores[0])   # vermelho
print(cores[-1])  # amarelo
print(cores[1:3]) # ('azul', 'verde')

# Exemplo 5: len() funciona em tuplas
print(len(cores))  # 4