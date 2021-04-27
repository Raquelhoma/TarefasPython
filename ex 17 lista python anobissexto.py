'''Faça um Programa que peça um número correspondente a um determinado
ano e em seguida informe se este ano é ou não bissexto.
Precisa ser divisivel por 400 ou divisivel por 4 e nao divisivel por 100
'''

ano = int(input('Informe o ano a ser consultado: '))
if(ano%400==0) or ((ano%4==0) and (ano%100!=0)):
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
ano = int(input('Informe o ano a ser consultado: '))
