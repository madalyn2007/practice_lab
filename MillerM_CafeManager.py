#Madalyn Miller


def show_banner():
    print("____________________________________")
    print("|                                  |")
    print("|  Café Du Merde - Tax Rate: 0.095 |")
    print("|__________________________________|")

def main_menu():
    while True:
        show_banner()

        print("[1] Add Item")
        print("[2] View Cart")
        print("[3] Remove item by number")
        print("[4] Checkout")
        print("[5] QUIT")

        choice = input("Please Choose an Option: ")

        if choice == "1":
            addItems(itemList, priceList, quantityList)

        if choice == "2":
             view_cart()
        
        if choice == "3":
            remove_item()
        
        if choice == "4":
             checkout()

        if choice == "5":
            print("Have a good day!")
            break



itemList = []
priceList = []
quantityList = []

def items():  
    return ["Coffee" , "Muffin" , "Fruit Cup"]

def price(): 
    return ["3.00" , "2.00" , "5.00"]


def addItems(itemList, priceList, quantityList):
    
    while True:
        print("---------------------------")
        count = 1
    
        for x in range(len(items())):
            print(f"{count} {items()[x]} ${price()[x]}")
            count += 1



        addChoice = input("What would you like to add to your cart? or press ENTER to exit: ")
        if (addChoice == ""):
            return
        else:
            index = int(addChoice) - 1
            howMany = int(input("How many?: "))


        quantity = int(howMany)

        itemList.append(items()[index])
        priceList.append(price()[index])
        quantityList.append(howMany)

        print (f"You added {howMany} {items()[index]} to your cart.")
    



def view_cart():

    print("---------------------------")

    print("Your Cart: ")

    subtotal = 0

    if len(itemList)== 0:
         print("Your cart is empty. Add some items!")


    for x in range(len(itemList)):
                    total = float(priceList[x]) * quantityList[x]
                    subtotal += total
                    print(f"{x+1}. {itemList[x]}  x {quantityList[x]} = ${total:.2f}")

    print("---------------------------")
 
    print(f"Subtotal: ${subtotal:.2f}")

    cart_input = input("Press ENTER to exit: ")


    if cart_input == "":
         return



def remove_item():
    print("---------------------------")

    for x in range(len(itemList)):
        subtotal = float(priceList[x]) * quantityList[x]
        print(f"{x+1}. {itemList[x]} x {quantityList[x]} = ${subtotal:.2f}")
    

    remove_choice = input("Enter the item number to remove OR press ENTER to exit: ")

    if remove_choice == "":
         return
    
    index = int(remove_choice) - 1

    remove_choice = itemList.pop(index)
    priceList.pop(index)
    quantityList.pop(index)

    print("---------------------------")
    print(f"{remove_choice} has been removed from the cart.")
    print("---------------------------")

    remove_choice = input("Enter the item number to remove OR press ENTER to exit: ")


discount_used = False


def checkout():
    print("---------------------------")

    global discount_used

    subtotal = 0
    discount = 0

    for x in range(len(itemList)):
        subtotal = float(priceList[x]) * quantityList[x]
        print(f"{x+1}. {itemList[x]} x {quantityList[x]} = ${subtotal:.2f}")
    
    tax_rate = 0.095
    tax = tax_rate * subtotal

    code = input("Enter a discount code OR press ENTER to continue: ")

    if code == "STUDENT10":
         if not discount_used:
              discount = subtotal * 0.10
              discount_used = True
              print("Discount Applied! (10% OFF)")
         else:
            print("Code already used!")
    
    final_total = subtotal + tax - discount


    print("---------------------------")
    print("Your total is:")
    print(f"-Subtotal: ${subtotal:.2f}")
    print(f"-Tax: ${tax:.2f}")
    if discount > 0:
         print(f"-Discount: -${discount:.2f}")
    print(f"-Total: ${final_total:.2f}")
    print("---------------------------")

    print(input("Press enter to print your receipt: "))
    
    itemList.clear()
    priceList.clear()
    quantityList.clear()

    print("---------------------------")
    print("Thank you for your purchase!")
    print("Your cart has been cleared.")
    print("Transaction complete.")
    print("---------------------------")
    print('\n')
    
    returnMain = input("Press ENTER to return to the main menu: ")
    if returnMain == "":
         return




def main():
    main_menu()




main()

