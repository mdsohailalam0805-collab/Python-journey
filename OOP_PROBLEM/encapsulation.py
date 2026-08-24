class bankAccount:
    def __init__(self, acccount_number,  balance):
        self.account_number=acccount_number
        self.balance=balance #public variable
        self.__balance=balance #private variable

    def deposite(self,amount):
        self.__balance+=amount
        print(f"deposite {amount} new balance {self.__balance}")

    def get_balance(self):
        return self.__balance
    
    
account =bankAccount("54321", 5000)
account.deposite(1000)
print(account.get_balance)
