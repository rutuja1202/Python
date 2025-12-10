


class Company:

    # company_name="capgemini"

    def __init__(self,company_name,company_address):

        self.company_name=company_name
        self.company_address=company_address # instance variable
        print(f"company Name : {self.company_name} {self.company_address}")


    def employee(self,name,address,skill,role):
        self.name=name
        self.address=address
        self.skill=skill
        self.role=role

        print(f"Name : {self.name} {self.address} {self.skill} and {self.role}  and company address is {self.company_address}"  )



emp1=Company("TCS","Pune")
emp1.employee("Pratik","Pune","HTML","Developer")

emp2=Company("Infosys","Mumbai")
emp2.employee("ABC","Mumbai","CSS","Mentor")
    


# ********************************************************

class BankAccount:

    def __init__(self,name):
        self.name=name
        self.balance=0

    def Deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print(f"Money Deposit : {self.amount} and Balance is :{self.balance}" )


    def withDraw(self,amount):
        self.amount=amount
        self.balance-=self.amount
        print(f"Money Withdraw : {self.amount} and Balance is :{self.balance}" )



b1=BankAccount("Harsh")
b1.Deposit(1000)
b1.Deposit(2000)

b1.withDraw(500)


    
