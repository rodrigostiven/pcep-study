# Exemplo 1: Escopo local vs global
x = 10  # Variável global

def funcao():
    x = 5  # Variável local (diferente da global)
    print(f"Dentro da função: {x}")

funcao()
print(f"Fora da função: {x}")

# Exemplo 2: Acessando variável global
nome = "Global"

def mostrar_nome():
    print(nome)  # Pode ler variável global

mostrar_nome()

# Exemplo 3: Não pode modificar global sem 'global'
contador = 0

def incrementar():
    # contador += 1  # UnboundLocalError!
    pass

# Exemplo 4: Variáveis locais não existem fora da função
def criar_variavel():
    local = 100
    print(local)

criar_variavel()
# print(local)  # NameError: 'local' não existe aqui

# Exemplo 5: Parâmetros são variáveis locais
def funcao(parametro):
    parametro = parametro * 2
    print(f"Dentro: {parametro}")

valor = 10
funcao(valor)
print(f"Fora: {valor}")  # 10 (não mudou)