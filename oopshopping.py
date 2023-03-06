class Shopping_cart():
    def __init__(self, items):
        self.items = items

    def addItems(self):
        item = input("What would you like to add to your cart: ")
        self.items.append(item)

    def showItems(self):
        print("Here is what is in your cart: ")
        for i in self.items:
            print(i)

    def removeItems(self):
        print("Above is what is in your cart.")
        remove = input("What item would you like to remove?")
        self.items.remove(remove)

    
    def run(self):
        while True:
            resp = input("To add item from your shopping cart, press 1. To remove an item from your shopping cart, press 2. To checkout and leave press 3. \n")
        
            if resp == "1":
                self.addItems()
            
            elif resp == "2":
                self.showItems()
                self.removeItems()
            
            elif resp == "3":
                self.showItems()
                print("Thank you for shopping with us!")


         
  

  


