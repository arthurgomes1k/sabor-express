
def classificar_idade():
    idade = int(input('Insira sua idade: '))

    if 0 <= idade <= 12:
        print('Você é uma Criança')
    elif 13 <= idade < 18:
        print('Você é um Adolescente')
    elif idade >= 18:
        print('Você é um Adulto')
    else:
        print('Valor inválido!')

def main():
    classificar_idade()

if __name__ == '__main__':
    main()