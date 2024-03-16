pessoas = [
    {'nome':'Jose', 'idade':30, 'cidade':'Patos'},
    {'nome':'Joao', 'idade':40, 'cidade':'Baraunas'},
    {'nome':'Maria', 'idade':20, 'cidade':'Passagem'}
    ]

nome = input('Digite o nome da pessoa que deseja alterar a idade: ')
pessoa_encontrada = False

for pessoa in pessoas:
    if nome == pessoa['nome']:
        pessoa_encontrada = True
        idade = input('Digite a nova idade: ')
        pessoa['idade'] = idade
        nova_profissao = input('Digite o nome da profissão dessa pessoa: ')
        profissao = {'profissao':nova_profissao}
        pessoa.update(profissao)
        del pessoa['cidade']

if not pessoa_encontrada:
    print('A pessoa não foi encontrada')

print(pessoas)