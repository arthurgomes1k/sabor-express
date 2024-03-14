def determinador_de_quadrante():
    x = int(input('insira a cordenada X: '))
    y = int(input('insira a cordenada Y: '))

    if x > 0 and y > 0:
        print('Primeiro Quadrante.')
    elif x < 0 and y > 0:
        print('Segundo Quadrante.')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante.')
    elif x > 0 and y < 0:
        print('Quarto Quadrante.')
    else:
        print('Origem.')

def main():
    determinador_de_quadrante()

if __name__ == '__main__':
    main()