# index file
#product management and shopping system
import cx_Oracle
from project.customer import *
from project.seller import *
from project.admin import *
from project import *

class sellers:
    def __init__(self):
        print("*"*60)
        print("-"*60)
        print("WELCOME SELLER")
        print("-"*60)
        print("*"*60)
        while True:
            print("1-seller_signup")
            print("2-seller_login")
            print("3-exit")
            choice = input("\nEnter your choice: ")
            if choice=='1':
                self.sign_up()
            elif choice =='2':
                self.login()
            elif choice=='3':
                exit()
            else:
                print("invalid option")

    def sign_up(self):
        signup.signup = seller_signup()

    def login(self):
        login.login = seller_login()


class customers:
    def __init__(self):
        print("*"*60)
        print("-"*60)
        print("WELCOME CUSTOMER")
        print("-"*60)
        print("*"*60)
        while True:
            print("1-customer_signup")
            print("2-customer_login")
            print("3-logout")
            chioce= input("Enter your choice: ")
            if choice=='1':
                self.sign_up()
            elif choice =='2':
                self.login()
            elif choice=='3':
                exit()
            else:
                print("invalid option")

    def sign_up(self):
        signup.signup = customer_sign_up()

    def login(self):
        login.login = customer_login()


class admins:
    def __init__(self):
        print("*"*60)
        print("-"*60)
        print("WELCOME ADMIN")
        print("-"*60)
        print("*"*60)
        while True:
            print("1-customer_login")
            print("2-logout")
            chioce= input("Enter your choice: ")
            if choice=='1':
                self.login()
            elif choice =='2':
                exit()
            else:
                print("invalid option")

    def login(self):
        login.login = admin_login()



            

print("*"*60)
print("-"*60)
print("PRODUCT MANAGEMENT AND SHOPPING SYSTEM")
print("-"*60)
print("*"*60)
while True:
    print("\n1-customer")
    print("2-seller")
    print("3-exit")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        customer = customers()
    elif choice =='2':
        seller = sellers()
    elif choice =='3':
        admin = admins()
    else choice =='4':
        print("*"*60)
        print("-"*60)
        print("THANKING YOU")
        print("-"*60)
        print("*"*60)
        exit()

