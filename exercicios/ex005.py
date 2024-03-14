
def insira_um_numero():
    numero_escolhido = int(input('Insira um número: '))

    if (numero_escolhido % 2) == 0:
        print(f'O númeor {numero_escolhido} é PAR')
    else:
        print(f'O númeor {numero_escolhido} é ÍMPAR')


def main():
    insira_um_numero()

if __name__ == '__main__':
    main()