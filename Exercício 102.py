def fatorial(número,show=True):
    if show:
        cont=número-1
        x = número
        while(cont > 0):
            x*=cont
            cont-=1
        print(f'O fatorial de {número} é {x}')
    
fatorial(3)


def fatorial(n,show=False):
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5,show=True))
