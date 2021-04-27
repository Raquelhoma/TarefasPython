#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
#é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
#18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
#preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
#considere latas cheias.

area = float(input('Informe a área a ser pintada em m²: '))
litros = area/6

print('\n\n****Caso 1: Somente latas de 18 litros**** ')
litros_extra = litros * 1.01
resto18 = litros_extra % 18
divisao = int(litros_extra / 18)

#Prova dos 9
print('Divisao em numero inteiro é: ', divisao)
print('O resto da divisao de litros de tinta por 18 é ', resto18)

if(resto18 == 0):
    numerolatas18 = divisao
if(resto18 > 0):
    numerolatas18 = divisao + 1

gasto = numerolatas18 * 80

print('\nO número de latas de 18 litros são: ', numerolatas18)
print('O valor pago será R$ ', gasto)

print('\n\n****Caso 2 : somente latas de 3,6 litros****')
resto36 = litros_extra % 3.6
divisao2 = int(litros_extra /3.6)

#prova dos 9
print('Divisao 2 é em inteiro ', divisao2)
print('O resto da divisao de litros de tinta por 3.6 é ', resto36)

if(resto36 == 0):
    numerolatas36 = divisao2
if(resto36 > 0):
    numerolatas36 = divisao2 + 1

gasto2 = numerolatas36 * 25

print('\nO número de latas de 3,6 litros são: ', numerolatas36)
print('O valor pago será R$ ', gasto2)

print('\n\n****Caso 3: Usando latas misturadas****')
quantidade18 = litros_extra / 18
quantidade_int = int(litros_extra / 18)
resto_18 = litros_extra % 18
if(resto_18 == 0):
    numerolatas_18 = quantidade18
if(resto_18 > 0):
    numerolatas_18 = quantidade_int
    litros_restantes = quantidade18 - quantidade_int
    resto_36 = litros_restantes % 3.6
    divisao_36 = int(litros_restantes /3.6)
    if(resto_36 == 0):
        numerolatas_36 = divisao_36
    if(resto_36 > 0):
        numerolatas_36 = divisao_36 + 1
gasto3 = (80 * numerolatas_18) + (25 * numerolatas_36)            

print('\nSerão usadas ', numerolatas_18, ' de 18 l e usadas ', numerolatas_36, ' de 3,6 l.')
print('O custo será de R$ ', gasto3)

if(gasto != gasto2) and (gasto2 !=gasto3):
    if(gasto < gasto2) and (gasto < gasto3):
        menor = gasto
        
    if(gasto2 < gasto) and (gasto2 < gasto3):
      menor = gasto2
    else:
        menor = gasto3

print('\nO menor valor é R$ ', menor)




