# Exemplo 1: Busca com while-else

numero_secreto = 7
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número (1-10):"))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    tentativas -= 1
else:
    print("Suas tentativas acabaram! O número era", numero_secreto)


# Exemplo 2: Validação de entrada
contador = 0

while contador < 5:
    senha = input("Digite a senha: ")
    if senha == "admin123":
        print("Acesso concedido")
        break
    contador += 1
else:
    print("Conta bloqueada por excesso de tentativas")