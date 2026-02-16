# Exemplo 1: Classificação de notas

nota = float(input("Digite a nota (0-10): "))

if nota >= 9:
    print("Conceito: A - Excelente!")
elif nota >= 7:
    print("Conceito: B - Bom!")
elif nota >= 5:
    print("Conceito: C - Regular")
else:
    print("Conceito: D - Insuficiente")