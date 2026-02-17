# Exemplo 1: Usando nomes dos parâmetros
def apresentar(nome, idade, cidade):
    print(f"{nome}, {idade} anos, mora em {cidade}")

apresentar(nome="Maria", idade=30, cidade="Rio de Janeiro")

# Exemplo 2: Ordem não importa com keywords
apresentar(idade=25, cidade="Brasília", nome="Pedro")

# Exemplo 3: Misturando posicionais e keywords
apresentar("Ana", idade=28, cidade="Salvador")

# Exemplo 4: Keywords devem vir depois dos posicionais
apresentar("Carlos", cidade="Curitiba", idade=35)  # OK
# apresentar(nome="Lucas", 22, "Recife")  # ERRO: posicional após keyword

# Exemplo 5: Clareza no código
def criar_usuario(username, email, ativo, admin):
    print(f"User: {username}, Email: {email}, Ativo: {ativo}, Admin: {admin}")

# Mais legível:
criar_usuario(
    username="joao123",
    email="joao@email.com",
    ativo=True,
    admin=False
)