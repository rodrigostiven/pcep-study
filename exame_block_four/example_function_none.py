# Exemplo 1: Função sem return retorna None
def sem_retorno():
    print("Esta função não retorna nada")

resultado = sem_retorno()
print(resultado)  # None

# Exemplo 2: Return vazio retorna None
def funcao_vazia():
    return

print(funcao_vazia())  # None

# Exemplo 3: Verificando None
def buscar_usuario(id):
    usuarios = {1: "João", 2: "Maria"}
    return usuarios.get(id)

usuario = buscar_usuario(3)
if usuario is None:
    print("Usuário não encontrado")
else:
    print(f"Usuário: {usuario}")

# Exemplo 4: None como valor padrão
def processar_dados(dados=None):
    if dados is None:
        dados = []
    dados.append("novo item")
    return dados

print(processar_dados())        # ['novo item']
print(processar_dados([1, 2]))  # [1, 2, 'novo item']

# Exemplo 5: Comparando com None
x = None
print(x is None)      # True (correto)
print(x == None)      # True (funciona, mas não recomendado)
print(x is not None)  # False