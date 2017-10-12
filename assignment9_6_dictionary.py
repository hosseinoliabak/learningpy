"""
9.6 Write a program (a tiny inventory program).
The original inventory is described by the following dictionary:
dFruits = {'Apples':10, 'Bananas':20, 'Oranges':15, 'Raisins':5, 'Apricots':8}
Present the user with a menu like this one:
 1. Display inventory
 2. Buy dFruits
 3. Stock dFruits
 4. Exit
When the user takes option 1: You must display all the dFruits and their
current stock levels on the screen.
When the user takes option 2: You must prompt the user for the fruit he/she
would like to buy. Example: Enter the fruit you would like to buy: Bananas

If the fruit is not available let the user know and re-prompt him for another
fruit. Once the fruit type is validated, prompt the user for the amount
(how many).
If the users chooses a number higher that the value currently available in
inventory, let the user know and re-prompt him for another amount.
If the amount is available then take it out of inventory and make the sale.

When the user selects option 3 Prompt the user for the name of the fruit,
and the amount to be stocked. If it is a new fruit, create its inventory record.

When the user enter the option 4 The programs exists.
"""
dFruits = {'Apples':10, 'Bananas':20, 'Oranges':15, 'Raisins':5, 'Apricots':8}
while (True):
    print ("______________________________________________")
    print("1. Display inventory")
    print("2. Buy dFruits")
    print("3. Stock dFruits")
    print("4. Exit")
    try:
        iChoice = int(input("Please enter a choice 1, 2, 3, or 4: "))
        if iChoice == 1:
            for k,v in dFruits.items():
                print (k,v)
        elif iChoice == 2:
            fruit = input("Which fruit would you want to buy? ")
            while fruit not in dFruits:
                print ("We didn't have", fruit, "in stock")
                fruit = input("Which fruit would you want to buy? ")
            iQuantity = int(input("How Many? "))
            while iQuantity > dFruits[fruit] or iQuantity <= 0:
                print("We don't have",iQuantity ,fruit ,"in stock. We only have", dFruits[fruit], ". Please anter a valid value: ")
                iQuantity= int(input("How Many? "))
            print (iQuantity, "of", fruit, "has/have been invoiced. The new inventory is: ")
            dFruits[fruit] -= iQuantity
            print (dFruits)
        elif iChoice == 3:
            fruit = input("Which fruit would you want to stock? ")
            while True:
                iQuantity = int(input("How many would you want to stock? "))
                if iQuantity <= 0:
                    print ("Enter an integer greater equal than 1")
                if iQuantity > 0:
                    if fruit in dFruits:
                        dFruits[fruit] += iQuantity
                    else:
                        dFruits[fruit] = iQuantity
                    break
        elif iChoice == 4:
            break
        else:
            print("Entry is NOT valid!")
    except ValueError:
        print("Oops! That was NOT a valid number. Try again...")
