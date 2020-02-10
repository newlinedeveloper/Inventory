#email module

class bank:
    
    a,i,no,name,bal,dep = 0,101,0,'',0.0,0.0
    
    def creation(self):
        print("*******************************")
        print("ACCOUNT CREATION")
        print("*******************************")
        print("your account no is: ",bank.i)
        self.ac_no =bank.i
        self.name=input("Enter your name: ")
        print("Your minimum deposit amount is Rs.500")
        self.dep = 500
        bank.i += 1 
        
        
    def deposit(self):
        print("*******************************")
        print("\n DEPOSIT")
        print("*******************************")
        no = int(input("\nEnter your Account number:"))
        for b in range(0,(bank.i)+1):
            if self.ac_no == no:
                m = b
        if self.ac_no == no:
            print("Account Number is :",self.ac_no)
            print("Name :",self.name)
            print("Balance is: ",self.dep)
            dep = int(input("How much Deposited Now: "))
            self.dep += dep 
            print("The current amount is : ",self.dep)
        else:
            print("Account number is not valid")
            
        
    def withdraw(self):
        
        print("*******************************")
        print("\n WITHDRAW")
        print("*******************************")
        no = int(input("\nEnter your Account number:"))
        for b in range(0,(bank.i)+1):
            if self.ac_no == no:
                m = b
        if self.ac_no == no:
            print("Account Number is :",self.ac_no)
            print("Name :",self.name)
            print("Balance is: ",self.dep)
            dep = int(input("How much Withdraw now: "))
            if self.dep - dep > 500:
                self.dep -= dep 
                print("The current amount is : ",self.dep)
            else:
                print("You have minimum amount")
        else:
            print("Account number is not valid")
            
        
    def balance(self):
        
        print("*******************************")
        print("\n Balance Enquiry")
        print("*******************************")
        no = int(input("\nEnter your Account number:"))
        for b in range(0,(bank.i)+1):
            if self.ac_no == no:
                m = b
        if self.ac_no == no:
            print("Account Number is :",self.ac_no)
            print("Name :",self.name)
            print("Balance is: ",self.dep)
        else:
            print("Account number is not valid")
            


user = []
user.append(bank())
while True:
    print("********************************")
    print("BANKING SYSTEM")
    print("********************************")
    print("1-Account creation")
    print("2-Deposit")
    print("3-Withdraw")
    print("4-Balance Enquiry")
    print("5-Exit")

    choice =int(input("Enter your choice: "))

    if choice < 5:
        if choice == 1:
            user[-1].creation()
        elif choice == 2:
            user[-1].deposit()
        elif choice == 3:
            user[-1].withdraw()
        elif choice == 4:
            user[-1].balance()
    elif choice == 5:
        exit()
    else:
        print("please select 1-5 option only")




