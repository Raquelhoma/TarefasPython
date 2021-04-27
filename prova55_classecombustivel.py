class BombaCombustivel:
    def __init__(self, tipocombustivel, valorlitro, quantidadecombustivel):
        self.tipocombustivel = tipocombustivel
        self.valorlitro = valorlitro
        self.quantidadecombustivel = quantidadecombustivel

    def abastecerporvalor(self, litros2):        
        self.quantidadecombustivel -= litros2
        return self.quantidadecombustivel

    def abastecerporlitro(self, litros2):
        self.quantidadecombustivel -= litros2
        return self.quantidadecombustivel

    def alterarvalor(self, novopreco1):
        self.valorlitro = novopreco1
        return self.valorlitro

    def alterarcombustivel (self, novotipo):
        self.tipocombustivel = novotipo
        return self.tipocombustivel

    def alterarquantidadecombustivel(self, litros2):
        self.quantidadecombustivel += litros2
        return self.quantidadecombustivel

bomba1 = BombaCombustivel('Gasolina', 4, 1000)
opcao = int(input('''O que deseja: 
                (1)- Abastecer por valor
                (2)- Abastecer por litro 
                (3)- Alterar valor 
                (4)- Alterar combustível 
                (5)- Alterar quantidade de combustivel
                (6)- Para SAIR: ''')) 
while opcao >0 and opcao<6:
    if opcao==1:
        valorreal = float(input('Informe o valor abastecido R$ '))
        litros1 = valorreal / bomba1.valorlitro
        bomba1.quantidadecombustivel = bomba1.abastecerporvalor(litros1)
        print(f'A quantidade total de combustivel: {bomba1.quantidadecombustivel} litros')
        opcao = int(input('O que deseja:(1)- Abastecer por valor(2)- Abastecer por litro (3)- Alterar valor (4)- Alterar combustível (5)- Alterar quantidade de combustivel (6)- Para Sair: : '))
    elif opcao==2:
        litros3 = float(input('informe a quantidade de litros abastecidos: '))
        bomba1.quantidadecombustivel = bomba1.abastecerporlitro(litros3)
        print(f'A quantidade total de combustível: {bomba1.quantidadecombustivel} litros')
        opcao = int(input('O que deseja:(1)- Abastecer por valor(2)- Abastecer por litro (3)- Alterar valor (4)- Alterar combustível (5)- Alterar quantidade de combustivel (6)- Para Sair: : '))
    elif opcao==3:
        novopreco = float(input('Informe o novo valor do preço R$ '))
        bomba1.valorlitro = bomba1.alterarvalor(novopreco)
        print('O novo valor do litro de ', bomba1.tipocombustivel, ' é ' , bomba1.valorlitro, 'reais')
        opcao = int(input('O que deseja:(1)- Abastecer por valor(2)- Abastecer por litro (3)- Alterar valor (4)- Alterar combustível (5)- Alterar quantidade de combustivel (6)- Para Sair: : '))
    elif opcao==4:
        tipocombustivel1 = input('Informe o tipo de combustível: Gasolina, Etanol, Diesel: ')
        bomba1.tipocombustivel = bomba1.alterarcombustivel(tipocombustivel1)
        print('O tipo de combustível da bomba foi alterado para: ', bomba1.tipocombustivel)
        opcao = int(input('O que deseja:(1)- Abastecer por valor(2)- Abastecer por litro (3)- Alterar valor (4)- Alterar combustível (5)- Alterar quantidade de combustivel (6)- Para Sair: : '))
    elif opcao==5:
        adicionar = float(input('Quantos litros deseja adicionar? '))
        bomba1.quantidadecombustivel = bomba1.alterarquantidadecombustivel(adicionar)
        print(f'A quantidade total de combustível: {bomba1.quantidadecombustivel} litros')
        opcao = int(input('O que deseja:(1)- Abastecer por valor(2)- Abastecer por litro (3)- Alterar valor (4)- Alterar combustível (5)- Alterar quantidade de combustivel (6)- Para Sair: : '))
    else:
        break
