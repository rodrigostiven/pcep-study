# Exemplo 1: Variável local "esconde" global
x = "global"

def funcao():
    x = "local"  # Esconde a variável global
    print(x)

funcao()  # local
print(x)  # global

# Exemplo 2: Shadowing em diferentes níveis
x = 1

def externa():
    x = 2
    
    def interna():
        x = 3
        print(f"Interna: {x}")
    
    interna()
    print(f"Externa: {x}")

externa()
print(f"Global: {x}")

# Exemplo 3: Cuidado com nomes de funções built-in
# list = [1, 2, 3]  # Esconde a função list()!
# nova_lista = list(range(5))  # TypeError!

# Exemplo 4: Parâmetro esconde variável global
nome = "Global"

def saudar(nome):  # Parâmetro esconde variável global
    print(f"Olá, {nome}!")

saudar("Local")  # Olá, Local!
print(nome)      # Global