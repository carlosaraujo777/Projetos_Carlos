import random
import string

# Definindo os caracteres que podem ser usados
letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

# Juntando tudo
todos_os_caracteres = letras + numeros + simbolos

# Pergunta o tamanho da senha
tamanho = int(input("Digite o tamanho da senha que você quer: "))

# Gera a senha aleatória
senha = ''.join(random.choice(todos_os_caracteres) for _ in range(tamanho))

print(f"Sua nova senha é: {senha}")