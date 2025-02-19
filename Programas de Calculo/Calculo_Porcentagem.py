while True:
    a = input('\nInforme o que deseja encontrar ("t" para nº total; "num" para o número; "p" para a porcentagem do nº)> ')
    if a == 't':
        p = int(input('\nInforme a porcentagem do número> '))
        num = int(input('Informe o número da porcentagem> '))
        
        t = num * 100 / p
        
        print('\n','='*50)
        print(f'número total é < {t:0.0f} >')
        print('='*50)
    if a == 'num':
        p = int(input('\nInforme a porcentagem do número> '))
        t = int(input('Informe o número total da porcentagem> '))
        
        num = t * p / 100
        
        print('\n','='*50)
        print(f'número da porcentagem < {num:0.0f} >')
        print('='*50)
    if a == 'p':
        t = int(input('\nInforme o número total da porcentagem> '))
        num = int(input('Informe o número que deseja> '))

        p = num * 100 / t
    
        print('\n','='*50)
        print(f'a porcentagem do número desejado é < {p}% >')
        print('='*50)
     
    dnv = input('\n Deseja fazer mais um cálculo?(s/n)> ')
    
    if dnv == 's':
        continue
    elif dnv == 'n':
        break
