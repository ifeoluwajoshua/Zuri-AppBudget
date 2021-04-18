database ={ }


class Budget:

    
    def __init__(self , category , amount):
        self.category = category
        self.amount = amount



    def deposit(user ,amount , bal):
        bal += amount
        return bal


    def withdraw(user ,amount , bal):
        bal -= amount
        return bal
        

    def balance(db):
        for category, bal in db.items():
            print(category, bal)



    def transfer(db , option1 ,amount , option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) + amount
        db[option2] = int(value2) + amount



def init():
    print("********WELCOME*********")
    menu()



def menu():
    try:

        user = int(input("\n=== *****WHAT WOULD YOU LIKE TO DO?******* =====\nPress \n(1) TO CREATE A NEW BUDGET \n(2) TO DEPOSIT \n(3) TO WITHDRAW \n(4) TO CHECK BALANCE \n(5) TO TRANSFER FUNDS BETWEEN BUDGETS \n(6) TO QUIT \n"))
        
    except:
        print("INVALID INPUT")
        menu()

    if (user == 1):
        new_budget()

    elif (user == 2):
        credit()

    elif (user == 3):
        debit()

    elif (user == 4):
        balance()

    elif (user == 5):
        transfer()

    elif (user == 6):
        out()

    else:
        print("INVALID INPUT")
        menu()



def new_budget():
    print("*****CREATING A NEW BUDGET******")

    budget_title = input("ENTER BUDGET NAME(FOOD , CLOTHING OR ENTERTAINMENT): \n")
    try:
        amount = int(input("ENTER YOUR BUDGET AMOUNT: \n#"))

    except:
        print("INVALID INPUT")
        new_budget()

    budget = Budget(budget_title, amount)
    database[budget_title] = amount
    print("")
    print(f"BUDGET {budget_title} WAS SETUP WITH #{amount}")
    menu()



def debit():
    print("********WITHDRAW FROM A CREATED BUDGET**********")
    print("******* AVAILABLE BUDGETS************")


    for key , value in database.items():
        print(f" - {key}")


    pick = int(input("PRESS (1) TO CONTINUE WITH YOUR DEBIT TRANSACTION\n PRESS (2) TO STOP TRANSACTION \n"))
    if pick == 1:
        user = input("SELECT ONE OF THE BUDGETS AFOREMENTIONED\n")
        if user in database:
            amt = int(input("ENTER AMOUNT YOU WISH TO WITHDRAW: \n#"))
            if amt < database[user]:
                balance = int(database[user])
                new_balance = Budget.withdraw(user , amt , balance)
                database[user] = new_balance
                print(f"#{amt} HAS BEEN DEBITED FROM BUDGET-{user} \nBUDGET AMOUNT REMAINING #{new_balance}")
                menu()

            else:
                pick = int(input(f"BUDGET {user} IS INSUFFICIENT OF THE #{amt} REQUIRED \nTHE ACTUAL BALANCE {databse[user]} \nPRESS (1) TO CREDIT ACCOUNT\n PRESS (2) TO DEBIT \n"))
                if pick == 1:
                    amt = int(input("ENTER AMOUNT YOU WISH TO WITHDRAW: \n#"))
                    balance = int(database[user])
                    new_balance = Budget.deposit(user , amt , balance)
                    database[user] = new_balance
                    print(" ")
                    print(f"BUDGETS-{user} HAS BEEN CREDITED WITH #{amt}")
                    debit()

                elif pick == 2:
                    debit()
                    
                else:
                    print("INVALID OPTION")
                    debit()

        else :
            pick = int(input(f"BUDGET {user} DOES NOT EXIST \nPRESS (1) TO CREATE A NEW BUDGET \nPRESS (2) TO RETRY \nPRESS (3) TO EXIT TRANSACTION "))
            if pick == 1:
                new_budget()

            elif pick == 2:
                debit()

            elif pick == 3:
                print(" ")
                menu()

            else:
                print("INVALID OPTION")
                debit()

    elif pick == 2:
        print("YOU HAVE TERMINATED THE DEBIT TRANSACTION")
        menu()

    else :
        print("INVALID OPTION")
        debit()



def credit():
    print("*******DEPOSIT INTO A BUDGET**********")
    print("********AVAILABLE BUDGETS*************")
    for key , value in database.items():
        print(f"-  {key}")

    pick = int(input("PRESS (1) TO CONTINUE WITH YOUR DEPOSIT \nPRESS (2) TO TERMINATE TRANSACTION \n"))
    if pick == 1:
        user = input("SELECT A BUDGET: \n")
        if user in database:
            amt = int(input("ENTER AMOUNT YOU WISH TO DEPOSIT: \n#"))
            balance = int(database[user])
            new_balance = Budget.deposit(user , amt , balance)
            database[user] = new_balance
            print(f"BUDGETS-{user} HAS BEEN CREDITED WITH #{amt} \nTOTAL BUDGET AMOUNT IS NOW #{new_balance}")
            menu()

        else:
            print(" ")
            pick = int(input(f"BUDGET {user} DOES NOT EXIST \nPRESS (1) TO CREATE A NEW BUDGET \nPRESS (2) TO RETRY \nPRESS (3) TO EXIT TRANSACTION "))
            if pick == 1:
                new_budget()

            elif pick == 2:
                credit()

            elif pick == 3:
                menu()

            else:
                print("INVALID OPTION")
                credit()
    elif pick == 2 :
        print("YOU HAVE TERMINATED THE DEPOSIT TRANSACTION")
        menu()

    else:
        print("INVALID OPTION")
        deposit()

        

def balance():
    print("********GETTING YOUR BUDGET BALANCE*********")
    check_bal = Budget.balance(database)
    if check_bal == None:
        print('')
        menu()
    else:
        print(f"#{check_bal}")
        menu()


def transfer():
    print("******AVAILABLE AND VALID BUDGETS*********")
    for key , value in database.items():
        print(key)
        print('')

    print("*******TRANSFER OPERATIONS*******")
    from_budget = input("ENTER THE BUDGET YOU ARE TRANSFERRING FROM: \n")
    if from_budget in database:
        from_amount = int(input("ENTER AMOUNT YOU WANT TO TRANSFER: \n#"))
        if from_amount < database[from_budget]:
            to_budget = input("ENTER THE BUDGET YOU ARE TRANSFERRING TO: \n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print(f"YOU HAVE TRANSFERRED #{from_amount} FROM {from_budget} TO {to_budget}")
                
                menu()

            else:
                print(f"{from_budget} BUDGET DOES NOT EXIST , PLEASE CHOOSE A VALID BUDGET")
                transfer()                

        else:
            print(f"YOU DO NOT HAVE ENOUGH FUNDS IN {from_budget} BUDGET")
            transfer()

    else:
        print(f"BUDGET {from_budget} DOES NOT EXIST , PLEASE CHOOSE A VALID BUDGET OR CREATE A NEW BUDGET")

        try:
            choice = int(input("PRESS (1) TO CHOOSE A VALID BUDGET \nPRESS (2) TO CREATE A NEW BUDGET \n"))

        except:
            print("INVALID INPUT")
        if choice == 1:
            transfer()
        elif choice == 2:
            new_budget()

        else:
            print("INVALID OPTION")
            menu()


def out():
    try:
        pick = int(input("ARE YOU SURE YOU WANT TO QUIT? \nPRESS (1) TO QUIT \nPRESS (2) TO CONTINUE \n"))

    except:
        print("INVALID INPUT")
        out()

    if pick == 1:
        print("WE HOPE YOU HAD A GREAT BUDGETTING EXPERIENCE BYE FOR NOW")
        quit()

    elif pick == 2:
        menu()

    else:
        print("INVALID INPUT")
        out()



init()
