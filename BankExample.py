class ICICIBankAccount:
    def __init__(self,user_name,main_bal):
        self.name=user_name
        self.__MainBal=main_bal
        self.Accountnumber="56324"
        self.__pin=1234
        self.__Account_Active_Status=True
        self.__isAtmCardHolder=False
        self.__isCheckBookHolder=False
        self.__isAtmCardGotFreezed=False
        self.__isAccountFreezed=False
    def __verifypin(self,pin):
        return self.__pin==pin
    def __UpdateMainBalByWithDraw(self,amount):
        self.__MainBal-=amount
        print(f"you have drawn{amount} successfully",self.__MainBal,"is main bal")
    def __UpdateMainBalByDeposit(self,amount):
        self.__MainBal +=amount
        print(f"you have credited {amount} successfully to your account",self.__MainBal,"is main bal")
    def __Show_MainBal(self):
        print(f"{self.__MainBal}is main bal")
    def __raiseAtmCard(self):
        self.__isAtmCardHolder=True
        return f"atm card approved"
    def __raiseCheckBook(self):
        self.__isCheckBookHolder=True
        return f"check book approved"
    #def __AtmCardFreezing(self):
       # self.__isAtmCardGotFreezed=True
        #return f"atm card got freezed"
    def __accountFreezed(self):
        self.__isAccountFreezed=True
        return "account freezed successfully"
    def withdraw(self,amount,pin):
        if self.__Account_Active_Status:
            if self.__verifypin(pin):
                if amount>self.__MainBal:
                    print("you are trying draw more amount than your main bal")
                else:
                    self.__UpdateMainBalByWithDraw(amount)
            else:
                    print("incorrect pin...")
    def deposit(self,amount,pin):
        if self.__Account_Active_Status:
            if self.__verifypin(pin):
                self.__UpdateMainBalByDeposit(amount)
            else:
                print("incorrect Pin")
        else:
            print("your account is not active in status")
    def Check_Bal(self,pin):
        if self.__Account_Active_Status:
            if self.__verifypin(pin):
                self.__Show_MainBal()
            else:
                print("incorrect pin...")
    def request_for_ATMcard(self):
        statusofatmcardapproval=self.__raiseAtmCard()
        print(statusofatmcardapproval)
    def request_for_CheckBook(self):
        satusofcheckBookApproval=self.__raiseCheckBook()
        print(satusofcheckBookApproval)
    def request_for_ATMCardFreezing(self):
        print(self.__AtmCardFreezing())
    def request_for_AccountFreezing(self):
        if self.Accountnumber==ac_number:
            self.__isAccountFreezed=False
            print("account frozen successfully")
            #else :
                #print("account is already closed.cannot freeze")
        else:
            print("account number is not matched.please enter valid account number")
class SavingAccount(ICICIBankAccount):
    def __init__(self,name,bal):
        self.loanLimit=200000
        super().__init__(name,bal)
    def personalLoanRaise(self,amount):
        if amount>self.loanLimit:
            print("you are exceeding your loan limit amount")
        else:
            print("you are quoting in your loan limit amount...you will granted loan soon")
class BusinessAccount(ICICIBankAccount):
    def __init__(self,name,bal):
        self.loanLimit=2000000
        super().__init__(name,bal)
    def businessLoanRaise(self,amount):
        if amount>self.loanLimit:
            print("you are exceeding your loan limit amount")
        else:
            print("you are quoting in your loan limit amount..you will granted loan soon")
saccount=SavingAccount("Madhu",50000)
baccount=BusinessAccount("shainy",100000)
#amount=int(input("enter amount:"))
#pin=int(input("enter pin:"))
ac_number=input("enter number:")
#saccount.personalLoanRaise(amount)
#baccount.businessLoanRaise(amount)
#saccount.request_for_ATMcard()
#saccount.request_for_CheckBook()
#saccount.request_for_ATMCardFreezing()
#saccount.withdraw(amount,pin)
#saccount.deposit(amount,pin)
#saccount.Check_Bal(pin)
#baccount.request_for_ATMcard()
saccount.request_for_AccountFreezing()
#baccount.request_for_AccountFreezing()

    