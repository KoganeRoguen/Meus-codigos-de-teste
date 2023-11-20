while True:
    t = int(input('\nInforme o número total da porcentagem> '))
    num = int(input('Informe o número que deseja> '))

    r = num * 100 / t
    
    print('\n','='*50)
    print(f'a porcentagem do número desejado é < {r}% >')
    print('='*50)
    
    p = input('\n Deseja fazer mais um cálculo?(s/n)> ')
    
    if p == 's':
        continue
    elif p == 'n':
        break