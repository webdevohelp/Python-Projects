class Customer:
    def __init__(self, name, amount = 0):
        self.name = name
        self.amount = amount
    def deposit(self,deposit):
        #to deposit given amount to the account of customer
        self.amount = self.amount+deposit
    def wthdwl(self, wthdwl):
        #to withdraw given amount from the account of customer
        if self.amount>=wthdwl:
            self.amount = self.amount-wthdwl
            #to check if customer has enough balance in account for withdrawl
            print(f"${wthdwl} withdrawn from the account! Current balance is {self.amount}")
        else:
            print("Not enough funds in the account!")
    def __str__(self) -> str:
        #to print the status of customer's account
        return f"customer name: {self.name}\nbalance:{self.amount}"
cust1 = Customer("Danny", 1000)
cust1.deposit(100)
print(cust1)
cust1.wthdwl(1100)
print(cust1)
cust1.wthdwl(10)
print(cust1)
