'''
#Divison by Zero Error
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r}')

#TypeError: unssoported operand type(s) for /: int andstr
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a/b
print(f'O resultado é {r}')
#list index out of range
lst = []
lst = [3,6,4]
print(lst[3])
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
#except Exception as erro:
#   print('Infelizmente tivemos um problema :(')
#    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisonError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')




    
