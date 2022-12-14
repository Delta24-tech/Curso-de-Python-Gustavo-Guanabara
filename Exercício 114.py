import urlib
import urlib.request
try:
    site = urlib.request.urlopen('https://www.pudim.com.br')
except urlib.erro.URLError:
    print('O site Pudim não está acessando.')
else:
    print('Tudo ok com o funcionamento do site')
