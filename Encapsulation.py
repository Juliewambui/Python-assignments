class BankAccount:
    def __init__(self, balance, name, number):
        self.__balance = balance #private attribute
        self.name = name #public attribute
        self._number = number #protected

    def deposit (self, amount):
        self.__balance += amount
        return f"Deposited {amount}"
    
    def get_balance(self):
        return f"New balance: {self.__balance}"
     
account = BankAccount(1500, "John", 1234)
 #print(account.__balance) #attribute error
print(account.name)
print(account._number)

print(account.deposit(2000))
print(account.get_balance())