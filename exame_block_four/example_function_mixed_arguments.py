# Exemplo 1: Posicionais + Keywords
def registrar_venda(produto, quantidade, preco, desconto=0):
    total = quantidade * preco * (1 - desconto)
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: R$ {total:.2f}")

registrar_venda("Notebook", 2, 3000)
registrar_venda("Mouse", 5, 50, desconto=0.1)
registrar_venda("Teclado", quantidade=3, preco=150, desconto=0.05)

# Exemplo 2: Ordem correta
def funcao(a, b, c=3, d=4):
    print(a, b, c, d)

funcao(1, 2)              # 1 2 3 4
funcao(1, 2, 5)           # 1 2 5 4
funcao(1, 2, d=10)        # 1 2 3 10
funcao(1, 2, 5, 6)        # 1 2 5 6

# Exemplo 3: ERRO - posicional após keyword
# funcao(1, b=2, 3)  # SyntaxError!