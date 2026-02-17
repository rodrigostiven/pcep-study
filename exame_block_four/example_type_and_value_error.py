# Exemplo 1: TypeError - operação inválida
try:
    resultado = "texto" + 5
except TypeError as e:
    print(f"TypeError: {e}")

try:
    lista = [1, 2, 3]
    lista[0] = "texto"  # OK
    lista["chave"] = 10  # TypeError
except TypeError as e:
    print(f"TypeError: {e}")

# Exemplo 2: ValueError - valor inadequado
def calcular_raiz(numero):
    try:
        return numero ** 0.5
    except ValueError:
        print("Erro: Número inválido!")

try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Erro: Digite um número válido!")

# Exemplo 3: Diferença entre TypeError e ValueError
try:
    int("abc")  # ValueError: string não é número
except ValueError:
    print("ValueError: Não é um número")

try:
    int([1, 2, 3])  # TypeError: tipo errado
except TypeError:
    print("TypeError: Tipo incompatível")

# Exemplo 4: Validação com ValueError
def definir_idade(idade):
    if not isinstance(idade, int):
        raise TypeError("Idade deve ser um inteiro")
    if idade < 0 or idade > 150:
        raise ValueError("Idade deve estar entre 0 e 150")
    return idade

try:
    definir_idade(-5)
except ValueError as e:
    print(f"Erro: {e}")