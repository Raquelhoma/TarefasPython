print("""
      Instructions: Press 1: Enter an item,
      Press 2: For delete an item,
      Press 3: To show your Basket
      Press 0: To Exit the program
      """)


shopping_basket = {}

option = int(input('Enter an option: '))

while option != 0:
    if option ==1:
        item = input('Enter an item to add: ')
        if item in shopping_basket:
            print('Item already in the shopping_basket')
            qnty = int(input('Enter the quantity to add: '))
            shopping_basket[item] = shopping_basket[item] + qnty
        else:                
            
            qnty = int(input('Enter the quantity: '))
            shopping_basket[item] = qnty
    elif option == 2:
        item = input('Enter an item to delete: ')
        del (shopping_basket[item])
    elif option == 3:
        for item in shopping_basket:
            print(item, ":" , shopping_basket[item])
    elif option != 0:
        print('You didn´t enter a valid number, ')

    option = int(input('\n\nEnter a valid number. '))

else:
    print('Shopping_basket program is close')
