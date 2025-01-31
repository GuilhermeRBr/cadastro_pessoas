dados = []
pessoas = []
mai = men = 0
maxi = []
mini = []

def cadastrar_pessoa():
    try:
        while True:

            while True:
                nome = input('Nome: ')
                if nome.isalpha():
                    break
                print('Digite apenas letras')
            while True:
                peso = input('Peso: ')
                if peso.isnumeric():
                    peso = int(peso)
                    break
                print('Digite apenas numeros')

            dados.append(nome)
            dados.append(peso)

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
                if opcao in ['s', 'n']:
                    break
                elif not opcao:
                    print('Digite uma opção')
                else:
                    print('Digite apenas S ou N')
                    
                if opcao == 'n':
                    break
    except Exception as e:
        print('\nOuve um erro: ', e)

cadastrar_pessoa()

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}KG. O peso foi de: ', end='')
for p in pessoas:
    if p[1] == mai:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {men}KG. O peso foi de: ', end='')
for p in pessoas:
    if p[1] == men:
        print(p[0], end=' ')

