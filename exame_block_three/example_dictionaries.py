# Exemplo 1: Criando dicionários
dicionario_vazio = {}
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print(pessoa)

# Exemplo 2: Acessando valores por chave
print(pessoa["nome"])    # João
print(pessoa["idade"])   # 25

# Exemplo 3: Criando com dict()
aluno = dict(nome="Maria", nota=9.5, aprovado=True)
print(aluno)

# Exemplo 4: Chaves de diferentes tipos
misto = {
    "texto": "valor",
    42: "número",
    (1, 2): "tupla",
    True: "booleano"
}
print(misto[42])
print(misto[(1, 2)])

# Exemplo 5: Valores de diferentes tipos
dados = {
    "nome": "Ana",
    "idade": 30,
    "notas": [8, 9, 7],
    "endereco": {"rua": "A", "numero": 123}
}
print(dados["notas"])
print(dados["endereco"]["rua"])