# Exemplo 1: Adicionando chaves
pessoa = {"nome": "João", "idade": 25}
pessoa["cidade"] = "Rio de Janeiro"
pessoa["profissao"] = "Engenheiro"
print(pessoa)

# Exemplo 2: Modificando valores
pessoa["idade"] = 26
print(pessoa)

# Exemplo 3: Removendo com del
del pessoa["profissao"]
print(pessoa)

# Exemplo 4: Removendo com pop()
idade = pessoa.pop("idade")
print("Idade removida:", idade)
print(pessoa)

# Exemplo 5: pop() com valor padrão
telefone = pessoa.pop("telefone", "Não encontrado")
print(telefone)  # Não encontrado

# Exemplo 6: popitem() - remove último item
dados = {"a": 1, "b": 2, "c": 3}
item = dados.popitem()
print("Item removido:", item)
print(dados)

# Exemplo 7: clear() - limpa dicionário
dados.clear()
print(dados)  # {}