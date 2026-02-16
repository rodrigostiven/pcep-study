# Exemplo 1: Criando listas

lista_vazia = []
numeros = [1, 2 ,3 , 4, 5]
frutas = ["maçã", "banana", "laranja"]
mista = [1, "texto", 3.14, True]

print(numeros)
print(frutas)
print(mista)

# Exemplo 2: Indexação (começa em 0)

cores = ["vermelho", "azul", "verde", "amarelo"]
print(cores[0])   # vermelho (primeiro)
print(cores[1])   # azul
print(cores[-1])  # amarelo (último)
print(cores[-2])  # verde (penúltimo)

# Exemplo 3: Modificando elementos

numeros = [10, 20, 30, 40]
numeros[0] = 15
numeros[-1] = 45
print(numeros) # [15, 20, 30, 45]

# Exemplo 4: Acessando com input

lista = [100, 200, 300, 400, 500]
indice = int(input("Digite um índce (0-4): "))
if 0 <= indice < len(lista):
    print("Valor:", lista[indice])
else:
    print("índice inválido!")