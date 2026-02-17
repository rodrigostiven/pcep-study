# Exemplo 1: Modificando variável global
contador = 0

def incrementar():
    global contador
    contador += 1

print(contador)  # 0
incrementar()
print(contador)  # 1
incrementar()
print(contador)  # 2

# Exemplo 2: Criando variável global dentro de função
def criar_global():
    global nova_variavel
    nova_variavel = "Criada na função"

criar_global()
print(nova_variavel)  # Criada na função

# Exemplo 3: Múltiplas variáveis globais
x = 1
y = 2

def modificar():
    global x, y
    x = 10
    y = 20

modificar()
print(x, y)  # 10 20

# Exemplo 4: Quando usar global (exemplo prático)
saldo = 1000

def depositar(valor):
    global saldo
    saldo += valor
    print(f"Depósito: R$ {valor}. Saldo: R$ {saldo}")

def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo -= valor
        print(f"Saque: R$ {valor}. Saldo: R$ {saldo}")
    else:
        print("Saldo insuficiente")

depositar(500)
sacar(300)
sacar(2000)

# Exemplo 5: Evitando global (melhor prática)
def depositar_melhor(saldo, valor):
    return saldo + valor

def sacar_melhor(saldo, valor):
    if valor <= saldo:
        return saldo - valor
    return saldo

saldo = 1000
saldo = depositar_melhor(saldo, 500)
saldo = sacar_melhor(saldo, 300)
print(f"Saldo final: R$ {saldo}")