dados = []
pessoas = []
mai = men = 0
maxi = []
mini = []

try:
    while True:
        dados.append(str(input('Nome: ')))
        dados.append(int(input('Peso: ')))
        if len(pessoas) == 0:
            mai = men = dados[1]
        else:
            if dados[1] > mai:
                mai = dados[1]
            if dados[1] < men:
                men = dados[1]
        pessoas.append(dados[:])
        dados.clear()
        while True:
            opcao = str(input('Quer continuar? [S/N]: ')).lower()
            if opcao in 'sn':
                break
            print('Digite apenas S ou N')
        if opcao == 'n':
            break
    print(f'Foram cadastradas {len(pessoas)} pessoas')
    print(f'O maior peso foi de {mai}KG. O peso foi de: ', end='')
    for p in pessoas:
        if p[1] == mai:
            print(p[0], end=' ')
    print(f'\nO menor peso foi de {men}KG. O peso foi de: ', end='')
    for p in pessoas:
        if p[1] == men:
            print(p[0], end=' ')
except KeyboardInterrupt:
    print('O usuario interrompeu o programa')
except Exception:
    print('Ouve um erro')
