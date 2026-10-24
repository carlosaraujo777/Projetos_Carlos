import string

# 1. Abre o arquivo e lê o conteúdo
with open('dev.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

# 2. Conta as linhas
linhas = texto.split('\n')
numero_de_linhas = len(linhas)

# 3. Limpa o texto (tira pontuação e deixa tudo minúsculo)
texto_limpo = texto.translate(str.maketrans('', '', string.punctuation)).lower()

# 4. Separa as palavras e conta
palavras = texto_limpo.split()
numero_de_palavras = len(palavras)

# 5. Conta a frequência de cada palavra
frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# 6. Pega as 3 palavras mais usadas
palavras_ordenadas = sorted(frequencia.items(), key=lambda item: item[1], reverse=True)
top_3 = palavras_ordenadas[:3]

# 7. Mostra o resultado
print("--- ANÁLISE DO TEXTO ---")
print(f"Total de linhas: {numero_de_linhas}")
print(f"Total de palavras: {numero_de_palavras}")
print("\nAs 3 palavras mais usadas:")
for palavra, quantidade in top_3:
    print(f"- '{palavra}': {quantidade} vezes")