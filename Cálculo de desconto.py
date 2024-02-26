while True:
    find = input('\nInforme o que deseja encontrar ("P" para Preço, "D" para desconto, "PD" para Porcentagem de Desconto)> ')
    if find == 'P':
        pd = float(input('\nInforme o Desconto do produto> '))
        d = float(input('Informe o Desconto(preço) do produto> '))

        p = (d * 100) / (100 - pd)
    
        print(f'\nPreço original do produto é: = R${p:0.2f} =')
    
    elif find == 'D':
        p = float(input('\nInforme o Preço do produto> '))
        pd = float(input('Informe o Desconto do produto> '))
    
        d = p * (100 - pd)/100
    
        print(f'\nO preço do produto descontado é: = R${d:0.2f} =')

    elif find == 'PD':
        p = float(input('\nInforme o Preço do produto> '))
        d = float(input('Informe o Desconto(preço) do produto> '))

        pd = 100 - (d * 100 / p)
    
        print(f'\nO desconto do produto é: = {pd:0.0f}% =')

    repeat = input('\nDeseja realizar mais um cálculo?(S/N)> ')
    if repeat == 'S':
        continue    
    elif repeat == 'N':
        print('\n=== Programa Encerrado ===\n')
        break