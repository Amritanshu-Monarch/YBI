pin = int(input("\nHello User! (^_^)\nPlease enter your Pin to proceed\n\nTo exit, Press 1\n\nPin : "))
if pin != 1:
    class ATM:
        balance = int(15000)
        def withdrawal(self,amount):
            balance = self.balance
            if amount>balance:
                print("\nSorry!\nEntered amount exceeds your Bank Balance\n\nThank You for choosing our ATM (^_^)\n")
            else :
                balance = balance - amount
                print(f"\n{amount} debited from account.\nRemaining Bank Balance is {balance}\n\nThank You for choosing our ATM (^_^)\n")
        def bal(self):
            print(f"\nCurrent Bank Balance : {self.balance}\n\nThank You for choosing our ATM (^_^)\n")
        def deposit(self,depAmount):
            balance = self.balance
            balance = balance + depAmount
            print(f"\n{depAmount} deposited to account.\nBank Balance is {balance}\n\nThank You for choosing our ATM (^_^)\n")
        def pinChange(self):
            def change():
                int(input("\nEnter OTP :\n"))
                a = int(input("\nEnter New Pin :\n"))
                b = int(input("\nConfirm New Pin :\n"))
                if a == b:
                    print("\nPin changed successfully!\n\nThank You for choosing our ATM (^_^)\n")
                else:
                    print("\nPins don't match\nPlease retry!\n")
                    change()
            change()
    customer = ATM()
    print("\nWelcome!\n\nWhat would you like to do?")
    def Choices():
        print("1) Balance Enquiry")
        print("2) Cash Withdrawal")
        print("3) Deposit Money")
        print("4) Change PIN")
        print("5) EXIT")
    Choices()
    choice = int(input("\nEnter the option number: "))
    def Execution(choice):
        if choice == 1:
            customer.bal()
        elif choice == 2:
            customer.withdrawal(int(input("\nEnter amount :\n")))
        elif choice == 3:
            customer.deposit(int(input("\nEnter amount :\n")))
        elif choice == 4:
            customer.pinChange()
        elif choice == 5:
            print("\nThank You for choosing our ATM (^_^)\n")
            exit()
        else:
            print("Invalid option!\nPlease choose a valid option.\n",Choices())
            choice = int(input("Enter the option number: "))
            Execution(choice)
    Execution(choice)
else :
    print("\nThank You for choosing our ATM (^_^)\n")
