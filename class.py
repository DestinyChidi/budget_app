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
        food_category()

    elif selectedOption == 2:
        clothing_category()

    elif selectedOption == 3:
        entertainment_category()

    else:
        print("Invalid option selected, please try again!")
        init()


def food_category():
    print("You selected food category")

    print("Here are the Options available in food category, select any to proceed")

    print("1. Deposit Funds")
    print("2. Withdraw Funds")
    print("3. Check Balance")
    print("4. Transfer Balance to another category")
    print("5. Go Back to Main Menu")

    foodOption = int(input("Please select an option: \n"))
    if foodOption == 1:

        amount = int(input("How much would you like to deposit? \n"))
        print('Your Balance is N' + str(amount + food.balance))
        print("\n")
        print("###### WHAT DO YOU WANT TO DO NEXT? #######")
        print("\n")
        print("1. Return to previous Menu")
        print("2. Return to Main Menu")
        print("\n")
        action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

        if action_input == 1:
            food_category()

        else:
            init()

    elif foodOption == 2:

        amount = int(input("How much would you like to withdraw: \n"))

        if amount <= food.balance:
            print("Take your cash, and your remaining balance is N" + str(food.balance - amount))
            print("\n")
            print("###### WHAT DO YOU WANT TO DO NEXT? #######")
            print("\n")
            print("1. Return to previous Menu")
            print("2. Return to Main Menu")
            print("\n")
            action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

            if action_input == 1:
                food_category()

            else:
                init()
        else:
            print("Sorry! Insufficient Balance")

        food_category()

    elif foodOption == 3:

        print("Your Balance is N" + str(food.balance))

        print("\n")
        print("###### WHAT DO YOU WANT TO DO NEXT? #######")
        print("\n")
        print("1. Return to previous Menu")
        print("2. Return to Main Menu")
        print("\n")
        action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

        if action_input == 1:
            food_category()

        else:
            init()

    elif foodOption == 4:

        print("Which Category do you want to transfer funds to?")

        print("1. Clothing")
        print("2. Entertainment")

        food_transfer_option = int(input("Please select an option: \n"))

        if food_transfer_option == 1:

            amount = int(input("How much do you want to transfer? \n"))
            if amount <= food.balance:
                print("Transfer successful, and your remaining balance is N" + str(food.balance - amount))
                print("\n")
                print("###### WHAT DO YOU WANT TO DO NEXT? #######")
                print("\n")
                print("1. Return to previous Menu")
                print("2. Return to Main Menu")
                print("\n")
                action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

                if action_input == 1:
                    food_category()

                else:
                    init()
            else:
                print("Sorry! Insufficient Balance")
                food_category()

        elif food_transfer_option == 2:

            amount = int(input("How much do you want to transfer? \n"))
            if amount <= food.balance:
                print("Transfer successful, and your remaining balance is N" + str(food.balance - amount))

                print("\n")
                print("###### WHAT DO YOU WANT TO DO NEXT? #######")
                print("\n")
                print("1. Return to previous Menu")
                print("2. Return to Main Menu")
                print("\n")
                action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

                if action_input == 1:
                    food_category()

                else:
                    init()
            else:
                print("Sorry! Insufficient Balance")
                food_category()

        else:
            print("Wrong option selected, please try again")
            food_category()

    elif foodOption == 5:

        print("Welcome to Main Menu")
        init()

    else:
        print("Wrong option selected, please try again")
        food_category()


def clothing_category():
    print("You selected Clothing category")

    print("Here are the Options available in Clothing category, select any to proceed")

    print("1. Deposit Funds")
    print("2. Withdraw Funds")
    print("3. Check Balance")
    print("4. Transfer Balance to another category")
    print("5. Go Back to Main Menu")

    clothing_option = int(input("Please select an option: \n"))
    if clothing_option == 1:

        amount = int(input("How much would you like to deposit? \n"))
        print("Deposit successful")
        print('Your Balance is N' + str(amount + clothing.balance))
        print("\n")
        print("###### WHAT DO YOU WANT TO DO NEXT? #######")
        print("\n")
        print("1. Return to previous Menu")
        print("2. Return to Main Menu")
        print("\n")
        action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

        if action_input == 1:
            clothing_category()

        else:
            init()

    elif clothing_option == 2:

        amount = int(input("How much would you like to withdraw: \n"))

        if amount <= clothing.balance:
            print("Take your cash, and your remaining balance is N" + str(clothing.balance - amount))

            print("\n")
            print("###### WHAT DO YOU WANT TO DO NEXT? #######")
            print("\n")
            print("1. Return to previous Menu")
            print("2. Return to Main Menu")
            print("\n")
            action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

            if action_input == 1:
                clothing_category()

            else:
                init()
        else:
            print("Sorry! Insufficient Balance")
            clothing_category()

    elif clothing_option == 3:

        print("Your Balance is N" + str(clothing.balance))
        print("\n")
        print("###### WHAT DO YOU WANT TO DO NEXT? #######")
        print("\n")
        print("1. Return to previous Menu")
        print("2. Return to Main Menu")
        print("\n")
        action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

        if action_input == 1:
            clothing_category()

        else:
            init()
    elif clothing_option == 4:

        print("Which Category do you want to transfer funds to?")

        print("1. Food")
        print("2. Entertainment")

        clothing_transfer_option = int(input("Please select an option: \n"))

        if clothing_transfer_option == 1:

            amount = int(input("How much do you want to transfer? \n"))
            if amount <= clothing.balance:
                print("Transfer successful, and your remaining balance is N" + str(clothing.balance - amount))

                print("\n")
                print("###### WHAT DO YOU WANT TO DO NEXT? #######")
                print("\n")
                print("1. Return to previous Menu")
                print("2. Return to Main Menu")
                print("\n")
                action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

                if action_input == 1:
                    clothing_category()

                else:
                    init()
            else:
                print("Sorry! Insufficient Balance")
                clothing_category()

        elif clothing_transfer_option == 2:

            amount = int(input("How much do you want to transfer? \n"))
            if amount <= clothing.balance:
                print("Transfer successful, and your remaining balance is N" + str(clothing.balance - amount))

                print("\n")
                print("###### WHAT DO YOU WANT TO DO NEXT? #######")
                print("\n")
                print("1. Return to previous Menu")
                print("2. Return to Main Menu")
                print("\n")
                action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

                if action_input == 1:
                    clothing_category()

                else:
                    init()

            else:
                print("Sorry! Insufficient Balance")
                clothing_category()

        else:
            print("Wrong option selected, please try again")
            clothing_category()

    elif clothing_option == 5:
        init()

    else:
        print("Wrong option selected, please try again")
        clothing_category()


def entertainment_category():
    print("You selected Entertainment category")

    print("Here are the Options available in Entertainment category, select any to proceed")

    print("1. Deposit Funds")
    print("2. Withdraw Funds")
    print("3. Check Balance")
    print("4. Transfer Balance to another category")
    print("5. Go Back to Main Menu")

    entertainment_option = int(input("Please select an option: \n"))

    if entertainment_option == 1:

        amount = int(input("How much would you like to deposit? \n"))
        print("Deposit Successful")
        print('Your Balance is N' + str(amount + entertainments.balance))

        print("\n")
        print("###### WHAT DO YOU WANT TO DO NEXT? #######")
        print("\n")
        print("1. Return to previous Menu")
        print("2. Return to Main Menu")
        print("\n")
        action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

        if action_input == 1:
            entertainment_category()

        else:
            init()

    elif entertainment_option == 2:

        amount = int(input("How much would you like to withdraw: \n"))

        if amount <= entertainments.balance:
            print("Take your cash, and your remaining balance is N" + str(entertainments.balance - amount))
            print("\n")
            print("###### WHAT DO YOU WANT TO DO NEXT? #######")
            print("\n")
            print("1. Return to previous Menu")
            print("2. Return to Main Menu")
            print("\n")
            action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

            if action_input == 1:
                entertainment_category()

            else:
                init()

        else:
            print("Sorry! Insufficient Balance")
            entertainment_category()

    elif entertainment_option == 3:

        print("Your Balance is N" + str(entertainments.balance))
        print("\n")
        print("###### WHAT DO YOU WANT TO DO NEXT? #######")
        print("\n")
        print("1. Return to previous Menu")
        print("2. Return to Main Menu")
        print("\n")
        action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

        if action_input == 1:
            entertainment_category()

        else:
            init()

    elif entertainment_option == 4:

        print("Which Category do you want to transfer funds to?")

        print("1. Food")
        print("2. Clothing")

        entertainment_transfer_option = int(input("Please select an option: \n"))

        if entertainment_transfer_option == 1:

            amount = int(input("How much do you want to transfer? \n"))
            if amount <= entertainments.balance:
                print("Transfer successful, and your remaining balance is N" + str(entertainments.balance - amount))
                print("\n")
                print("###### WHAT DO YOU WANT TO DO NEXT? #######")
                print("\n")
                print("1. Return to previous Menu")
                print("2. Return to Main Menu")
                print("\n")
                action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

                if action_input == 1:
                    entertainment_category()

                else:
                    init()
            else:
                print("Sorry! Insufficient Balance")
                entertainment_category()

        elif entertainment_transfer_option == 2:

            amount = int(input("How much do you want to transfer? \n"))
            if amount <= entertainments.balance:
                print("Transfer successful, and your remaining balance is N" + str(entertainments.balance - amount))

                print("\n")
                print("###### WHAT DO YOU WANT TO DO NEXT? #######")
                print("\n")
                print("1. Return to previous Menu")
                print("2. Return to Main Menu")
                print("\n")
                action_input = int(input("Please enter an option, 1 for Previous Menu, 2 for Main Menu: \n"))

                if action_input == 1:
                    entertainment_category()

                else:
                    init()
            else:
                print("Sorry! Insufficient Balance")
                entertainment_category()

        else:
            print("Wrong option selected, please try again")
            entertainment_category()

    elif entertainment_option == 5:
        init()

    else:
        print("Wrong option selected, please try again")
        entertainment_category()


init()
