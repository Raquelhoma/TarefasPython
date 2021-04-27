limit = int(input('Informe um número limite: '))
primes = []
dicionario = {}
dicionario[1] = ['é primo']
for num in range(0, limit +1):
    counter = 0
    for i in range(1, num +1):
        if(num%i == 0):
            counter = counter + 1
    if(counter == 2):
        primes.append(num)
        dicionario[num] = ['é primo']
    
print(primes)
input('\nPress ENTER')
print(dicionario)
