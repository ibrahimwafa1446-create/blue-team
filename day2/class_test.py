"""class Person:
    def __init__(self, Name, Age, City):
        self.Name = Name
        self.Age = Age
        self.City = City
    def print_data(self):
        print(f"Hi, I'm {self.Name}, {self.Age} years old from {self.City}.")

P1 = Person("Ibrahim", 31, "Misrata")
P1.print_data()"""

class BankAccount:
    def __init__(self, Name, Balance):
        self.Name = Name
        self.Balance = Balance
    def Deposit(self, Value):
        self.Balance += Value
    def Withdraw(self, Value):
        if Value <= self.Balance:
            self.Balance -= Value
        else:
            print("There is not enough balance")
    def Print_Balance(self):
        print("Balance = " + str(self.Balance))

x = BankAccount("Ali", 100)
x.Deposit(50)
x.Withdraw(140)
x.Print_Balance()