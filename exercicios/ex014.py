lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
#lista_de_numeros = [1,2,3,4,5,6,'a',8,9,10]
soma = 0

try:
    for num in lista_de_numeros:
        soma += num
    print(f"A soma dos elementos é: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
