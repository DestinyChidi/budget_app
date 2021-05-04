class Budget:
    def __init__(self, balance):
        self.balance = balance


food = Budget(5000)
clothes = Budget(30000)
entertainments = Budget(2000)


# first list the available categories
# then list the functions available in the selected category
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
            print("Take your cash, and your remaining balance is N" + str(food.balance - amount))

        elif foodOption == 3:
            amount = int(input("What issue will you like to report? \n"))
            print("Your Balance is N" + str(food.balance))

        elif foodOption == 4:
            amount = int(input("What issue will you like to report? \n"))
            print("Your Balance is N" + str(food.balance))

    elif selectedOption == 2:
        amount = int(input("How much would you like to deposit? \n"))
        print('Your Balance is N' + str(amount + food))

        pass

    elif selectedOption == 3:
        amount = int(input("What issue will you like to report? \n"))
        print('Thank you for contacting us')


init()
