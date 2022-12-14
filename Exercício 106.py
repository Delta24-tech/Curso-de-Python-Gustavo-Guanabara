from time import sleep
c = ('\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
     );

def ajuda(com):
    help(com)

def título(msg,cor):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHelp',cor=1)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO',cor=1)
