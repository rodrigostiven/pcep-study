# Exemplo Login com usuário e senha

usuario = input("Usuário: ")

if usuario == "admin":
    senha = input("Senha: ")
    if senha == ("1234"):
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")