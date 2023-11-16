import random

v = ['a','e','i','o','u', 'y']
c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

while True:
    n = int(input('\nQuantos caracteres deseja que tenha no nome>'))
    if n <= 1:
        print('<Erro> informe um valor maior que 1')
    else:
        if n == 2:
            c1 = random.randint(1,2)
            if c1 == 1:
                c1 = random.choice(v)
                c2 = random.choice(c)
            elif c1 == 2:
                c1 = random.choice(c)
                c2 = random.choice(v)
            print('\n', c1, c2)
        elif n > 2:
            name = random.choice(v) + random.choice(c)
            for _ in range(n - 2):
                if name[-1] in v:
                    name += random.choice(c)
                else:
                    name += random.choice(v)
            print('\n', name)