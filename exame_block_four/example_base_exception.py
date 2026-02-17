# Exemplo 1: BaseException (não capture normalmente!)
try:
    # Código
    pass
except BaseException:  # Captura TUDO (incluindo Ctrl+C)
    print("Isso captura até KeyboardInterrupt!")

# Exemplo 2: Exception (recomendado)
try:
    # Código
    pass
except Exception:  # Captura erros comuns, mas não SystemExit/KeyboardInterrupt
    print("Erro capturado!")

# Exemplo 3: SystemExit
import sys

try:
    sys.exit(0)
except SystemExit:
    print("Tentativa de sair do programa")

# Exemplo 4: KeyboardInterrupt (Ctrl+C)
try:
    while True:
        pass  # Loop infinito
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário")