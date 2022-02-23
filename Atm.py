class ATM:
    balance = 100000.0
    def __init__(self, cardNum, pinNum):
        self.cardNum = cardNum
        self.pinNum = pinNum
    def cashWithdrawl(self, cash):
        if(cash > self.balance):
            print("you do not have that much money")
        else:
            self.balance-=cash
            print("The cash was withdrawn")
    def cashDeposit(self, cash):
        self.balance+=cash
        print("The cash was deposited")
    def balanceInquiry(self):
        print("Your current balance is:", self.balance)

cardNum = int(input("Enter your card number: "))
pinNum = int(input("Enter your pin: "))
atm = ATM(cardNum, pinNum)

while True:
    choice = int(input("Type 0 to exit out of the ATM, 1 for balance inquiry, 2 for depositing cash, and 3 for withdrawing cash: "))
    if(choice == 0):
        print("Thank you for using the ATM!")
        break
    elif(choice == 1):
        atm.balanceInquiry()
    elif(choice == 2):
        cash = int(input("Enter the amount of cash you want to deposit: "))
        atm.cashDeposit(cash)
    elif(choice == 3):
        cash = int(input("Enter the amount of cash you want to withdraw: "))
        atm.cashWithdrawl(cash)
    else:
        print("Invalid option")


