# Exemplo 1: Verificando existência
frutas = ["maçã", "banana", "laranja"]

if "banana" in frutas:
    print("Temos banana!")

if "uva" not in frutas:
    print("Não temos uva")

# Exemplo 2: Validação de entrada
opcoes_validas = ["sim", "não", "talvez"]
resposta = input("Sua resposta (sim/não/talvez): ")

if resposta in opcoes_validas:
    print("Resposta válida!")
else:
    print("Resposta inválida!")

# Exemplo 3: Filtrando lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print("Números pares:", pares)

# Exemplo 4: Busca em lista
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
buscar = input("Digite um nome: ")

if buscar in nomes:
    posicao = nomes.index(buscar)
    print(f"{buscar} encontrado no índice {posicao}")
else:
    print(f"{buscar} não encontrado")