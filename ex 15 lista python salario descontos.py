#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados
#11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
input('*****************CONTRA CHEQUE**********************')
valor = float(input('Qual o valor da hora trabalhada R$ '))
horas = float(input('Informe a quantidade de horas trabalhadas no mês: '))

salario = valor * horas
descontoir = salario * 0.11
descontoinss = salario * 0.08
descontosind = salario * 0.05
descontos = descontoir + descontoinss + descontosind
salarioliquido = salario - descontos

print('+ Salário Bruto: R$ ', salario)
print('- IR (11%) : R$ ', descontoir)
print('- INSS (8%) : R$ ', descontoinss)
print('- Sindicato (5%) : R$ ', descontosind)
print('= Salário Líquido : R$ ', salarioliquido)



