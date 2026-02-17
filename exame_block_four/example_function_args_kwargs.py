# Exemplo 1: *args - argumentos posicionais variáveis
def somar_todos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(somar_todos(1, 2, 3))           # 6
print(somar_todos(1, 2, 3, 4, 5))     # 15
print(somar_todos(10))                # 10

# Exemplo 2: **kwargs - argumentos keyword variáveis
def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_info(nome="João", idade=25, cidade="SP")

# Exemplo 3: Combinando tudo
def funcao_completa(obrigatorio, *args, padrao=10, **kwargs):
    print(f"Obrigatório: {obrigatorio}")
    print(f"Args: {args}")
    print(f"Padrão: {padrao}")
    print(f"Kwargs: {kwargs}")

funcao_completa(1, 2, 3, 4, padrao=20, extra="valor")