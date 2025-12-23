#lista de tarefas,tarefas numeradas, tarefas com check (concluido, pendente e iniciado) e remoção por número

tarefas = []
while True:
    print("*** Menu de Tarefas ***")
    print('1. Adicionar Tarefa')
    print('2. Remover Tarefa')
    print('3. Listar Tarefas')
    print('4. Marcar Tarefa')
    print('5. Sair')
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        tarefa = input('Digite a tarefa a ser adicionada: ')
        #tafeas.append adiciona um item na lista
        tarefas.append({'descricao': tarefa, 'status': 'Pendente'})
        print('Tarefa adicionada com sucesso!')
    
    elif escolha == '2':
        # pq -1? pq a lista comeca do 0
        numero = int(input('Digite o número da tarefa a ser removida: ')) - 1
        
        # verifica se o número é válido # len = tamanho da lista
        if 0 <= numero < len(tarefas):
            tarefas.pop(numero)
            print('Tarefa removida com sucesso!')
        else:
            print('Número de tarefa inválido.')
            
            # lista as tarefas que ja existem
    elif escolha == '3':
        print('Lista de Tarefas:')
        for i, tarefa in enumerate(tarefas):
            # i + 1 para numerar a partir de 1
            print(f'{i + 1}. {tarefa["descricao"]} - {tarefa["status"]}')

    elif escolha == '4':
        #marcacoes de tarefas
        numero = int(input('Digite o número da tarefa a ser marcada: ')) - 1
        if 0 <= numero < len(tarefas):
            print('Escolha o status:')
            print('1. Pendente')
            print('2. Iniciado')
            print('3. Concluído')
            status_escolha = input('Digite o número do status: ')
            # atualiza o status da tarefa
            if status_escolha == '1':
                # tarefas[numero] acessa a tarefa na posicao numero e ['status'] acessa o status dela
                tarefas[numero]['status'] = 'Pendente'
            elif status_escolha == '2':
                tarefas[numero]['status'] = 'Iniciado'
            elif status_escolha == '3':
                tarefas[numero]['status'] = 'Concluído'
            
            else:
                print('Status inválido.')
                continue
            print('Tarefa atualizada com sucesso!')
        else:
            print('Número de tarefa inválido.')
            
    #sair do programa
    elif escolha == '5':
        print('Saindo do programa. Até mais!')
        break
    else:
        #vai alem dos numeros existemtes
        print('Opção nao reconhecida. Tente novamente.')
        