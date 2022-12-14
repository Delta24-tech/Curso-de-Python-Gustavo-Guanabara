'''filme = {'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'}
print(filme.values())
for k,v in filme.items():
    print(f'O {k} é {v}')
brasil = []
estado1 = {'uf': 'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf': 'Sao Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')
        
         
