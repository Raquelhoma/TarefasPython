coluna = []

for i in range(3):
    linha = []    
    for j in range(3):
        linha.append(int(input('Digite a nota [' + str(i) + ',' + str(j) + ']:')))
    coluna.append(linha)
cont = 0
for i in range(3):
    for j in range(3):
        if coluna[i][j] % 2 == 0:
            cont +=1

for i in range(3):
    print(coluna[i])

print('A matriz contém ', cont, 'números pares')
            



                     
        
