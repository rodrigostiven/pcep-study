# Exemplo 1: len() - comprimento da lista
frutas = ["maçã", "banana", "laranja", "uva"]
print("Quantidade de frutas:", len(frutas))  # 4

numeros = [10, 20, 30]
print("Tamanho:", len(numeros))  # 3

# Exemplo 2: append() - adiciona no final
lista = [1, 2, 3]
lista.append(4)
lista.append(5)
print(lista)  # [1, 2, 3, 4, 5]

# Exemplo 3: insert() - insere em posição específica
cores = ["vermelho", "azul", "verde"]
cores.insert(0, "preto")      # Insere no início
cores.insert(2, "amarelo")    # Insere no índice 2
print(cores)  # ['preto', 'vermelho', 'amarelo', 'azul', 'verde']

# Exemplo 4: index() - encontra índice do elemento
animais = ["gato", "cachorro", "pássaro", "peixe"]
posicao = animais.index("pássaro")
print("Pássaro está no índice:", posicao)  # 2

# Se o elemento não existe, gera erro
# print(animais.index("cobra"))  # ValueError!

# Exemplo 5: Verificando antes de usar index()
if "cachorro" in animais:
    print("Índice do cachorro:", animais.index("cachorro"))