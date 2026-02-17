# Exemplo 1: IndexError
def acessar_lista(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print(f"Erro: Índice {indice} não existe!")
        return None

numeros = [1, 2, 3, 4, 5]
print(acessar_lista(numeros, 2))   # 3
print(acessar_lista(numeros, 10))  # Erro

# Exemplo 2: KeyError
def buscar_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        print(f"Erro: Chave '{chave}' não encontrada!")
        return None

dados = {"nome": "João", "idade": 25}
print(buscar_valor(dados, "nome"))     # João
print(buscar_valor(dados, "cidade"))   # Erro

# Exemplo 3: Capturando LookupError genérico
def acessar_dado(estrutura, chave):
    try:
        return estrutura[chave]
    except LookupError:
        print("Erro de busca!")
        return None

print(acessar_dado([1, 2, 3], 5))        # IndexError
print(acessar_dado({"a": 1}, "b"))       # KeyError