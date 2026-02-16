# Exemplo 1: keys() - retorna todas as chaves
aluno = {"nome": "Maria", "nota": 9.5, "curso": "Python"}
chaves = aluno.keys()
print(chaves)        # dict_keys(['nome', 'nota', 'curso'])
print(list(chaves))  # ['nome', 'nota', 'curso']

# Exemplo 2: values() - retorna todos os valores
valores = aluno.values()
print(valores)        # dict_values(['Maria', 9.5, 'Python'])
print(list(valores))  # ['Maria', 9.5, 'Python']

# Exemplo 3: items() - retorna pares (chave, valor)
itens = aluno.items()
print(itens)        # dict_items([('nome', 'Maria'), ...])
print(list(itens))  # [('nome', 'Maria'), ('nota', 9.5), ...]

# Exemplo 4: Convertendo para lista
notas = {"João": 8, "Maria": 9, "Pedro": 7}
lista_alunos = list(notas.keys())
lista_notas = list(notas.values())
print(lista_alunos)  # ['João', 'Maria', 'Pedro']
print(lista_notas)   # [8, 9, 7]

# Exemplo 5: Calculando média
soma = sum(notas.values())
media = soma / len(notas)
print(f"Média da turma: {media:.1f}")

# Exemplo 6: Encontrando maior valor
maior_nota = max(notas.values())
print("Maior nota:", maior_nota)

for aluno, nota in notas.items():
    if nota == maior_nota:
        print(f"Melhor aluno: {aluno}")