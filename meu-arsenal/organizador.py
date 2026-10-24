import os
import shutil

# O caminho da pasta que você quer organizar (troque pelo caminho real)
pasta_alvo = "C:/Users/Carlos/Downloads" 

# Mapeamento de extensões para as pastas
pastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mov"],
    "Outros": [] # Vai cair tudo que não for nas outras
}

# Garante que as pastas existam
for nome_pasta in pastas:
    caminho_pasta = os.path.join(pasta_alvo, nome_pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

# Percorre todos os arquivos da pasta alvo
for arquivo in os.listdir(pasta_alvo):
    caminho_arquivo = os.path.join(pasta_alvo, arquivo)
    
    # Ignora se for uma pasta
    if os.path.isdir(caminho_arquivo):
        continue
        
    # Pega a extensão do arquivo (em minúsculo)
    _, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()
    
    # Descobre em qual pasta ele se encaixa
    destino = "Outros"
    for nome_pasta, extensoes in pastas.items():
        if extensao in extensoes:
            destino = nome_pasta
            break
            
    # Move o arquivo
    caminho_destino = os.path.join(pasta_alvo, destino, arquivo)
    shutil.move(caminho_arquivo, caminho_destino)
    print(f"Movido: {arquivo} -> {destino}")

print("Organização concluída!")