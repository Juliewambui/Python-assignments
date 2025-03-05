Class BankAccount:
    def __init__(self, acc_no, name, balance, open_date):
        self.acc_no =acc_no
        self.name = name
        self.balance = balance
        self.open_date = open_date

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}, New Balance: {self.balance}"
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawn: {amount}, New Balance: {self.balance}"
    def check_balance(self):
        return f"Balance: {self.balance}"
    def customer_details(self):
        return f"Name: {self.name}, Account: {self.acc_no}, Opened:  {self.open_date}, Balance: {self.balance}" 
    my_bankaccount = BankAccount("234567", "Julie Wambui", 500000, "2009-04-11")
    print(my_bankaccount.deposit(20000)) #depositing money
    print(my_bankaccount.withdraw(3000)) #withdrawing money
    print(my_bankaccount.check_balance()) #checking balance
    print(my_bankaccount.customer_details()) #printing customer details
