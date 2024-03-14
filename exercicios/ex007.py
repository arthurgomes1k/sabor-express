user = 'python'
senha = int(1234)

def login():
    user = input('insira seu usuario: ')
    senha = int(input('Insira sua senha: '))

    if user == 'python' and senha == 1234:
        print('Login realizado com sucesso!')
    else:
        print('Dados incorretos')

def main():
    login()

if __name__ == '__main__':
    main()