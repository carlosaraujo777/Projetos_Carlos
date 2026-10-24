import os

# 1. Carregar tarefas antigas (se existirem)
tarefas = []

if os.path.exists(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        # Lê as linhas, remove os espaços em branco e guarda na lista
        tarefas = [linha.strip() for linha in arquivo.readlines()]

while True:
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        
        # 2. Salvar a nova tarefa no arquivo
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(nova_tarefa + "\n")
            
        print("Tarefa adicionada e salva com sucesso!")
        
    elif opcao == "2":
        print("\n--- SUAS TAREFAS ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada ainda.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
        
        print("") 

    elif opcao == "3":
        print("Saindo do sistema... Até logo!")
        break
        
    else:
        print("Opção inválida! Tente novamente.")