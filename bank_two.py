class bank:

    name,IFSC,MICR,address,location,Zip_code = 'Canara bank','HGTREU09234','JJHGTEU8902148','Telephone road','Aruppukottai','626101'

    def __init__(self):
        print("*******************************")
        print("BANK DETAILS")
        print("*******************************")
        print("Bank name is : ", bank.name)
        print("IFSC code is: ",bank.IFSC)
        print("MICR code is: ",bank.MICR)
        print("Address : ", bank.address)
        print("LOCATION :",bank.location)
        print("Zip code: ",bank.Zip_code)


class creation(bank):
    ac_no,name,dep = 56001,'',500
    def __init__(self):
        print("*******************************")
        print("ACCOUNT CREATION")
        print("*******************************")
        print("your account no is: ",creation.ac_no)
        self.ac_no =creation.ac_no
        self.name=input("Enter your name: ")
        print("Your minimum deposit amount is Rs.500")
        self.dep = 500
        creation.ac_no += 1

    def display(self):
        print("\n*******************************")
        print("WELCOME ",self.name.upper())
        print("*******************************")
        print("your account no is: ",self.ac_no)
        print("your balance is: ",self.dep)
        print("Bank name is : ", bank.name)
        print("IFSC code is: ",bank.IFSC)
        print("MICR code is: ",bank.MICR)
        print("Address : ", bank.address)
        print("LOCATION :",bank.location)
        print("Zip code: ",bank.Zip_code)
        
        
        
        
        
        
class deposit(bank):
    def __init__(self,customer):
        print("*******************************")
        print("\n DEPOSIT")
        print("*******************************")
        no = int(input("\nEnter your Account number:"))
        for b in range(0,len(customer)):
            if customer[b].ac_no == no:
                m = b
        if customer[m].ac_no == no:
            print("Account Number is :",customer[m].ac_no)
            print("Name :",customer[m].name)
            print("Balance is: ",customer[m].dep)
            dep = int(input("How much Deposited Now: "))
            customer[m].dep += dep 
            print("The current amount is : ",customer[m].dep)
            print("\n*******************************")
            print("WELCOME ",customer[m].name.upper())
            print("*******************************")
            print("your account no is: ",customer[m].ac_no)
            print("your balance is: ",customer[m].dep)
            print("Bank name is : ", bank.name)
            print("IFSC code is: ",bank.IFSC)
            print("MICR code is: ",bank.MICR)
            print("Address : ", bank.address)
            print("LOCATION :",bank.location)
            print("Zip code: ",bank.Zip_code)

        else:
            print("Account number is not valid")
            
        



class withdraw(bank):
    b= m =ac_no = 0
    def __init__(self,customer):
        print("*******************************")
        print("\n WITHDRAW")
        print("*******************************")
        no = int(input("\nEnter your Account number:"))
        for withdraw.b in range(0,len(customer)):
            if customer[withdraw.b].ac_no == no:
                withdraw.m = withdraw.b
        if customer[withdraw.m].ac_no == no:
            print("Account Number is :",customer[withdraw.m].ac_no)
            print("Name :",customer[withdraw.m].name)
            print("Balance is: ",customer[withdraw.m].dep)
            dep = int(input("How much Withdraw now: "))
            if customer[withdraw.m].dep - dep > 500:
                customer[withdraw.m].dep -= dep 
                print("The current amount is : ",customer[withdraw.m].dep)
            else:
                print("You have minimum amount")
            print("\n*******************************")
            print("WELCOME ",customer[withdraw.m].name.upper())
            print("*******************************")
            print("your account no is: ",customer[withdraw.m].ac_no)
            print("your balance is: ",customer[withdraw.m].dep)
            print("Bank name is : ", bank.name)
            print("IFSC code is: ",bank.IFSC)
            print("MICR code is: ",bank.MICR)
            print("Address : ", bank.address)
            print("LOCATION :",bank.location)
            print("Zip code: ",bank.Zip_code)

        else:
            print("Account number is not valid")
        
        


class balance(bank):
    def __init__(self,customer):
        print("*******************************")
        print("\n Balance Enquiry")
        print("*******************************")
        no = int(input("\nEnter your Account number:"))
        for b in range(0,len(customer)):
            if customer[b].ac_no == no:
                m = b
        if customer[m].ac_no == no:
            print("Account Number is :",customer[m].ac_no)
            print("Name :",customer[m].name)
            print("Balance is: ",customer[m].dep)
            print("\n*******************************")
            print("WELCOME ",customer[m].name.upper())
            print("*******************************")
            print("your account no is: ",customer[m].ac_no)
            print("your balance is: ",customer[m].dep)
            print("Bank name is : ", bank.name)
            print("IFSC code is: ",bank.IFSC)
            print("MICR code is: ",bank.MICR)
            print("Address : ", bank.address)
            print("LOCATION :",bank.location)
            print("Zip code: ",bank.Zip_code)

        else:
            print("Account number is not valid")
            


customer_creation = customer_deposit = customer_withdraw = customer_balance = []

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
            customer_creation.append(creation())
            customer_creation[-1].display()
        elif choice == 2:
            customer_deposit.append(deposit(customer_creation))
            
        elif choice == 3:
            customer_withdraw.append(withdraw(customer_creation))
        elif choice == 4:
            customer_balance.append(balance(customer_creation))
    elif choice == 5:
        exit()
    else:
        print("please select 1-5 option only")


            

        
        
        










