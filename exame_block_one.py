# 1. Função print() básica

print("Olá, Mundo!")
print(42)
print(3.14)

# 2.Parâmetro sep= (separador)
# Separador padrão é espaço

print("A", "B", "C")

# Mudando o separador
print("A", "B", "C", sep="-") # Saída: A-B-C
print("2026", "02", "15", sep="/") # Saída: 2026/02/15
print("Python", "Java", "C++", sep=" | ") # Saída: Python | Java | C++
print(1, 2, 3, 4, 5, sep="") # Saída: 12345

# 3. Parâmettro end= (final)
# End padrão é quebra de linha (\n)

print("Linha 1")
print("Linha 2")

# Mudando o final
print("Mesma", end=" ")
print("linha") # Saída: Mesma Linha

print("Carregando", end="...")
print("Pronto!") # Saída: Carregando...Pronto!

# Sem quebra de linha
print("A", end="")
print("B", end="")
print("C") # Saída: ABC

# 4. Combinando sep= e end=

print("Python", "é", "legal", sep="-", end="!\n")
# Saída: Python-é-legal!

print("Item1", "Item2", "Item3", sep=" | ", end=" <- Lista\n")
# Saída: Item1 | Item2 | Item3 <- Lista

# 5. Função input() básica
# Entrada de texto

nome = input("Digite seu nome: ")
print("Olá,", nome)

# Input sempre retorna string
idade = input("Digite sua idade: ")
print("Você digitou:", idade, "- Tipo:", type(idade))

# 6. Função int() - Conversão para inteiro
# Convertendo string para inteiro

idade = input("Digite sua idade: ")
idade_int = int(idade)
print("Daqui a 5 anos você terá: ", idade_int + 5)

# Conversão direta

numero = int(input("Digite um número: "))
dobro = numero * 2
print("O dobro é:", dobro)

# Convertendo float para int (remove decimais)

print(int(3.9)) # Saída: 3
print(int(7.1)) # Saída: 7
print(int(-2.8)) # Saída: -2

# 7. Função float() - Conversão para decimal
# Convertendo string para float

altura = input("Digite sua altura em metros: ")
altura_float = float(altura)
print("Sua altura é:", altura_float, "metros")

# Conversão direta

preco = float(input("Digite o preco: R$ "))
desconto = preco * 0.1
print("Desconto de 10%: R$", desconto)

# Convertendo int para float
print(float(5)) # Saída: 5.0
print(float(10)) # Saída: 10.0