from utils import cadastrar_pessoa, pessoas

mai, men = cadastrar_pessoa()


print('-=' * 30)
print()
print(f'{"Cadastro de Pessoas:":^60}')
print()
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}KG. O peso foi de: ', end='')

for p in pessoas:
    if p[1] == mai:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {men}KG. O peso foi de: ', end='')
for p in pessoas:
    if p[1] == men:
        print(p[0], end=' ')

while True:
    print('\n')
    try:
        print('-=' * 30)
        opcao = int(input('\nQuer ver o IMC de qual pessoa? [0 para sair]: '))
        if opcao == 0:
            break
        print(f'{pessoas[opcao - 1][0]} tem IMC de {pessoas[opcao - 1][3]:.2f}')
    except Exception as e:
        print('Digite um numero valido')
        print('-=' * 30)
        

