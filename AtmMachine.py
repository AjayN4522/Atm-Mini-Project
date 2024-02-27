def atmMachine():
    print("Select Your Language")
    print("1.Tamil")
    print("2.English")
    print("3.Hindi")
    choice=int(input("Enter Your choice"))
    if choice==" ":
        print("please select any Language")
        atmMachine()
    elif choice==1:
        print("You select a Tamil Language and You countine")
    elif choice==2:
        print("You select a English Language and You countine")
    else:
        print("you select a Hindi Language and You continue")
    print("----------------------------------------------------------------------")
    
    print("Enter Your Atm Pin...")
    pins=[1234,1345,4567,5675,3464,1235,9999]
    def pinGenerate():
        atmPin=int(input("Type Your Pin: "))
        for i in pins:
            if i==atmPin:
                print(" Correct Pin and you Continue")
                return True
            else:
                print("invalid Pin Please Enter Again")
                pinGenerate()
    pinGenerate()
    print("------------------------------------------------------------------------")
    
    def selectFucntion():
        def withDraw(amount):
            print("enter Your With draw amount...!")
            wiDraw=int(input("enter amount :"))
            if wiDraw==" ":
                print("please enter Your Amount..!")
                withDraw()
            elif wiDraw>amount:
                print("insufficient balance")
                print("do You want to continue enter no:1 :")
                print("do you want to close enter no:3 :")
                con=int(input("enter no : "))
                if con==1:
                    withDraw()
                else:
                    "Thanks you for Your coversion"
                    atmMachine()
            elif wiDraw<amount:
                amount=amount-wiDraw
                print("your amount have success fully withdraw")
                print("you want more amount click no : 1")
                print("balance check click no: 2")
                exit=int(input("continue or exit :"))
                if exit==1:
                    withDraw()
                elif exit==2:
                    balanceCheck(amount)
                else:
                    selectFucntion()
                print("--------------------------------------------------------")
        def balanceCheck(amount):
            print("your current balance is :",amount)
            selectFucntion()
        
        def depositMoney(amount):
            print("enter Your deposit amount")
            deposit=int(input("enter amount :"))
            amount=amount+deposit
            print("do check your balance click 1 or exit click 2 :")
            choice=int(input("enter choice"))
            if choice==1:
                balanceCheck(amount)
            else:
                selectFucntion()
            
        print("Start Your Fuctions")
        print("1.Withdraw")
        print("2.Balance Check")
        print("3.deposit Amount")
        amount=50000
        selFucn=int(input("select Your function"))
        if selFucn==1:
            print("with drawing a money")
            withDraw(amount)
        elif selFucn==2:
            balanceCheck(amount)
        else:
            depositMoney(amount)
    selectFucntion()
if __name__ == '__main__':
    atmMachine()