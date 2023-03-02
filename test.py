shopping_cart= []

print("Hi, let's shop!")
while True:
    
    response = input("To add item from your shopping cart, press 1. To remove an item from your shopping cart, press 2. To checkout and leave press 3. \n")
    if response == "1":
        item = input("What would you like to add to your cart: ")
        shopping_cart.append(item)
        print(shopping_cart)
        print("Would you like to go back to the main menu?")
        main = input("'Yes' or 'No'?\n")
        if main == 'yes':
            continue
        if main == 'no':
            print("Would you like to checkout?\n")
            checkout=input("'Yes' or 'No'?\n")
            if checkout == 'no':
                continue
            if checkout == 'yes':
                print("Here are the contents of your shopping cart. Goodbye!")
                print(shopping_cart)
                break

    if response == "2":
        print(shopping_cart)
        shopping_cart.remove((input("Above is your shopping cart, what item would you like to remove? ")))
        print(shopping_cart)
        print("Would you like to go back to the main menu?")
        main = input("'Yes' or 'No'?\n")
        if main == 'yes':
            continue
        if main == 'no':
            print("Would you like to checkout?\n")
            checkout=input("'Yes' or 'No'?\n")
            if checkout == 'no':
                continue
            if checkout == 'yes':
                print("Here are the contents of your shopping cart. Goodbye!")
                print(shopping_cart)
                break
 
        
    elif response == "3":
        print("Here are the contents of your shopping cart. Goodbye!")
        print(shopping_cart)
        break
  

  


