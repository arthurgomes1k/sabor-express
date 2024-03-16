pessoas = [
    {'nome':'Jose', 'idade':30, 'cidade':'Patos'},
    {'nome':'Joao', 'idade':40, 'cidade':'Baraunas'},
    {'nome':'Maria', 'idade':20, 'cidade':'Passagem'}
    ]

nome = input('Digite o nome da pessoa: ')
pessoa_encontrada = False

for pessoa in pessoas:
    if nome == pessoa['nome']:
        pessoa_encontrada = True
        print(f'A chave {nome} existe no dicionário.')

if not pessoa_encontrada:
    print(f'A chave {nome} não existe no dicionário.')