lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0

for num in lista_de_numeros:
    if (num % 2) == 1:
        soma += num
print(soma)