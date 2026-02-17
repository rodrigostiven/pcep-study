# Exemplo 1: Estrutura básica
"""
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── AssertionError
    └── ... (muitas outras)
"""

# Exemplo 2: ZeroDivisionError (ArithmeticError)
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero!")

# Exemplo 3: IndexError (LookupError)
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Erro: Índice fora do alcance!")

# Exemplo 4: KeyError (LookupError)
try:
    dicionario = {"a": 1, "b": 2}
    print(dicionario["c"])
except KeyError:
    print("Erro: Chave não encontrada!")

# Exemplo 5: TypeError
try:
    resultado = "texto" + 5
except TypeError:
    print("Erro: Tipos incompatíveis!")

# Exemplo 6: ValueError
try:
    numero = int("abc")
except ValueError:
    print("Erro: Valor inválido para conversão!")