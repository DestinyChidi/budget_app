class Budget:
    def __init__(self, balance):
        self.balance = balance


food = Budget(5000)
clothing = Budget(30000)
entertainments = Budget(2000)


# first list all the Categories
# then list the options available in the selected category
# perform the function
# compute the balance

def init():

    print("Welcome to our budget app")
    print("***** What do you want to do today?")

    print("Below are the Categories available in our budget app, select any to proceed")

    print("1. Food")
    print("2. Clothing")
    print("3. Entertainment")

    selectedOption = int(input("Please select an option:"))

    if selectedOption == 1:

        print("You selected food category")

        print("Here are the Options available in food category, select any to proceed")

        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. Check Balance")
        print("4. Transfer Balance to another category")

        foodOption = int(input("Please select an option: \n"))
        if foodOption == 1:

            amount = int(input("How much would you like to deposit? \n"))
            print('Your Balance is N' + str(amount + food.balance))

        elif foodOption == 2:

            amount = int(input("How much would you like to withdraw: \n"))

            if amount <= food.balance:
                print("Take your cash, and your remaining balance is N" + str(food.balance - amount))
            else:
                print("Sorry! Insufficient Balance")

        elif foodOption == 3:

            print("Your Balance is N" + str(food.balance))

        elif foodOption == 4:

            print("Which Category do you want to transfer funds to?")

            print("1. Clothing")
            print("2. Entertainment")

            food_transfer_option = int(input("Please select an option: \n"))

            if food_transfer_option == 1:

                amount = int(input("How much do you want to transfer? \n"))
                if amount <= food.balance:
                    print("Transfer successful, and your remaining balance is N" + str(food.balance - amount))
                else:
                    print("Sorry! Insufficient Balance")

            elif food_transfer_option == 2:

                amount = int(input("How much do you want to transfer? \n"))
                if amount <= food.balance:
                    print("Transfer successful, and your remaining balance is N" + str(food.balance - amount))
                else:
                    print("Sorry! Insufficient Balance")

            else:
                print("Wrong option selected, please try again")

        else:
            print("Wrong option selected, please try again")

    elif selectedOption == 2:

        print("You selected Clothing category")

        print("Here are the Options available in Clothing category, select any to proceed")

        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. Check Balance")
        print("4. Transfer Balance to another category")

        clothing_option = int(input("Please select an option: \n"))
        if clothing_option == 1:

            amount = int(input("How much would you like to deposit? \n"))
            print('Your Balance is N' + str(amount + clothing.balance))

        elif clothing_option == 2:

            amount = int(input("How much would you like to withdraw: \n"))

            if amount <= clothing.balance:
                print("Take your cash, and your remaining balance is N" + str(clothing.balance - amount))
            else:
                print("Sorry! Insufficient Balance")

        elif clothing_option == 3:

            print("Your Balance is N" + str(clothing.balance))

        elif clothing_option == 4:

            print("Which Category do you want to transfer funds to?")

            print("1. Food")
            print("2. Entertainment")

            clothing_transfer_option = int(input("Please select an option: \n"))

            if clothing_transfer_option == 1:

                amount = int(input("How much do you want to transfer? \n"))
                if amount <= clothing.balance:
                    print("Transfer successful, and your remaining balance is N" + str(clothing.balance - amount))
                else:
                    print("Sorry! Insufficient Balance")

            elif clothing_transfer_option == 2:

                amount = int(input("How much do you want to transfer? \n"))
                if amount <= clothing.balance:
                    print("Transfer successful, and your remaining balance is N" + str(clothing.balance - amount))
                else:
                    print("Sorry! Insufficient Balance")

            else:
                print("Wrong option selected, please try again")

        else:
            print("Wrong option selected, please try again")

    elif selectedOption == 3:

        print("You selected Entertainment category")

        print("Here are the Options available in Entertainment category, select any to proceed")

        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. Check Balance")
        print("4. Transfer Balance to another category")

        entertainment_option = int(input("Please select an option: \n"))

        if entertainment_option == 1:

            amount = int(input("How much would you like to deposit? \n"))
            print('Your Balance is N' + str(amount + entertainments.balance))

        elif entertainment_option == 2:

            amount = int(input("How much would you like to withdraw: \n"))

            if amount <= entertainments.balance:
                print("Take your cash, and your remaining balance is N" + str(entertainments.balance - amount))
            else:
                print("Sorry! Insufficient Balance")

        elif entertainment_option == 3:

            print("Your Balance is N" + str(entertainments.balance))

        elif entertainment_option == 4:

            print("Which Category do you want to transfer funds to?")

            print("1. Food")
            print("2. Clothing")

            clothing_transfer_option = int(input("Please select an option: \n"))

            if clothing_transfer_option == 1:

                amount = int(input("How much do you want to transfer? \n"))
                if amount <= entertainments.balance:
                    print("Transfer successful, and your remaining balance is N" + str(entertainments.balance - amount))
                else:
                    print("Sorry! Insufficient Balance")

            elif clothing_transfer_option == 2:

                amount = int(input("How much do you want to transfer? \n"))
                if amount <= entertainments.balance:
                    print("Transfer successful, and your remaining balance is N" + str(entertainments.balance - amount))
                else:
                    print("Sorry! Insufficient Balance")

            else:
                print("Wrong option selected, please try again")

        else:
            print("Wrong option selected, please try again")

    else:
        print("Wrong option selected, please try again")

init()
