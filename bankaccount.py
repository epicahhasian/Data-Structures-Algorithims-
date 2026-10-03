class BankAccount():
    def __init__ (self,account_holder, balance):
        self.account = account_holder
        self.balance = balance 

    def getdetails(self):
        return self.account, self.balance 


    def deposit(self):
        self.depositamount =  int (input("Please enter the amount you would like to deposit:"))
        self.balance += self.depositamount 
        print("Amount Depoisited")

    def withdraw(self):
        self.withdrawamount = int(input ("Please enter the amount you would like to withdraw"))
        if self.withdrawamount > self.balance:
            print ("Not enough balance to withdraw:")

        else:
            self.balance -= self.withdrawamount 
            print("Amount Withdrawn")

        


        


bank = BankAccount("Abaan" ,456000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
print (bank.getdetails())
print(bank.deposit())
print(bank.getdetails())
print (bank.withdraw())
print(bank.getdetails())