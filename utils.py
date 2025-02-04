dados = []
pessoas = []


def cadastrar_pessoa():
    mai = men = 0


    try:
        while True:

            while True:
                nome = input('Nome: ')
                if nome.isalpha():
                    break
                print('Digite apenas letras')

            while True:
                peso = input('Peso [Kg]: ')
                if peso.isnumeric():
                    peso = int(peso)
                    break
                print('Digite apenas numeros')

            while True:
                altura = input('Altura [Cm]: ')
                if altura.isnumeric():
                    altura = int(altura)
                    break
                print('Digite apenas numeros')

            dados.append(nome.capitalize())
            dados.append(peso)
            dados.append(altura)
            dados.append(calcula_imc(peso, altura))

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
                return mai, men
    except Exception as e:
        print('\nOuve um erro: ', e)


def calcula_imc(peso, altura):
    imc = peso / ((altura / 100)** 2)
    return imc