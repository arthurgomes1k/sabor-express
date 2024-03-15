lista_de_numeros = [5, 10, 8, 10]
soma = 0

try:
    for num in lista_de_numeros:
        soma += num
        media = soma / len(lista_de_numeros)
    print(f'A média dos valores é {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média')
except Exception as e:
    print(f"Ocorreu um erro: {e}")