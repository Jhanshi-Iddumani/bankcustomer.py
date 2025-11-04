class sbibank:
    def __init__(self,name,main_balance):
        self.n=name
        self.__MainBal=main_balance
        self.__pin=1234
        self.__Account_Active_Status=True
    def __verifypin(self,pin):
            return self.__pin==pin
class savingaccount(sbibank):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        print(self.n)
    def CheckBalance(self,pin):
        if self.__Account_Active_Status:
            if self.__verifypin(pin):
                self.__Show_MainBal()
            else:
                print("incorrect pin...")
class bussinessaccount(sbibank):
    def __init__(self,bname,initialb):
        self.bussiness=bname
        self.initial=initialb
        print(self.bussiness,self.initial)
        
account=savingaccount("ram",10000)
#acc=bussinessaccount("Super Market",20000)
account.CheckBalance()
pin=int(input("enter pin:"))