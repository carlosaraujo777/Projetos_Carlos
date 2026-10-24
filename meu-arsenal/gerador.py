import os

# O nome da pasta que vamos criar
nome_pasta = "projetos_do_carlos"

# Cria a pasta (se ela não existir)
if not os.path.exists(nome_pasta):
    os.makedirs(nome_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso!")
else:
    print(f"A pasta '{nome_pasta}' já existe.")

# Loop para criar 10 arquivos
for i in range(1, 11):
    nome_arquivo = f"nota_{i}.txt"
    caminho_completo = os.path.join(nome_pasta, nome_arquivo)
    
    # Cria e escreve no arquivo
    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Esse é o arquivo número {i}.\n")
        arquivo.write("Criado automaticamente pelo Python!\n")
    
    print(f"Arquivo {nome_arquivo} criado.")

print("Tudo pronto! Olha a pasta no seu explorador de arquivos.")