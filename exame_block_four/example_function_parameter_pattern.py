# Exemplo 1: Parâmetro com valor padrão
def saudar(nome="Visitante"):
    print(f"Olá, {nome}!")

saudar()          # Olá, Visitante!
saudar("João")    # Olá, João!

# Exemplo 2: Múltiplos parâmetros com padrão
def criar_perfil(nome, idade=18, cidade="Não informada"):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

criar_perfil("Ana")
criar_perfil("Bruno", 25)
criar_perfil("Carlos", 30, "São Paulo")

# Exemplo 3: Parâmetros sem padrão devem vir primeiro
def funcao(obrigatorio, opcional=10):  # OK
    pass

# def funcao_errada(opcional=10, obrigatorio):  # ERRO!
#     pass

# Exemplo 4: Valor padrão mutável (CUIDADO!)
def adicionar_item(item, lista=[]):  # PROBLEMA!
    lista.append(item)
    return lista

print(adicionar_item(1))  # [1]
print(adicionar_item(2))  # [1, 2] - Inesperado!

# Exemplo 5: Solução correta
def adicionar_item_correto(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(adicionar_item_correto(1))  # [1]
print(adicionar_item_correto(2))  # [2] - Correto!