# customer signup form


class customer_sign_up:
    
    
    def __init__(self):
        print("*"*60)
        print("-"*60)
        print("CUSTOMER SIGNUP")
        print("-"*60)
        print("*"*60)
        SpecialSym ='!@##@%@^#$^&**()}{'
        self.name = input("Enter your name: ")
        for char in self.name:
            if not char.isalpha():
                print("invalid username!!!")
                self.name = input("\nEnter your name: ")
            else:
                break
            
        
        self.email_id = input("\nEnter your email id: ")
        while True:
            if  self.email_id[-10:len(self.email_id)] == '@gmail.com':
                break
            else:
                self.email_id = input("Please enter valid email id:")
            
        print('\n\t1-The password must contain 8 to 16 character.')
        print('\t2-the password should have at least one uppercase letter.')
        print('\t3-the password should have at least one lowercase letter.')
        print('\t4-the password should have at least one numeral.')
        print('\t5-the password should have at least one of the symbols $@#.')    
                
                

        while True:

            self.password = input("\nEnter your password: ")
            self.conform_password = input("Enter your conform_password: ")

            if len(self.password) <= 8 and len(self.password) >= 16:
                print("\nThe password must contain 8 to 16 character!!! ")
                self.password = input("Enter your password: ")
                self.conform_password = input("Enter your conform_password: ")

            elif not any(char.isupper() for char in self.password):
                print('\nthe password should have at least one uppercase letter')
                self.password = input("Enter your password: ")
                self.conform_password = input("Enter your conform_password: ")
                
            elif not any(char.islower() for char in self.password):
                print('\nthe password should have at least one lowercase letter')
                self.password = input("Enter your password: ")
                self.conform_password = input("Enter your conform_password: ")
                
            elif not any(char.isdigit() for char in self.password):
                print('\nThe password should have at least one numeral')
                self.password = input("Enter your password: ")
                self.conform_password = input("Enter the conform_password: ")

            elif not any(char in SpecialSym for char in self.password):
                print('\nThe password should have at least one of the symbols $@#')
                self.password = input("Enter your password: ")
                self.conform_password = input("Enter your conform_password: ")
                      
            elif self.password != self.conform_password:
                print("\nIncorrect password and conform password")
                self.password = input("PLEASE!! Enter correct password: ")
                self.conform_pasword = input("Then Enter correct conform password: ")
            else:
                break
        return self.database()

    def database(self):
        import cx_Oracle
        con = cx_Oracle.connect("system/26011999")
        cur = con.cursor()
        cur.execute("INSERT INTO customer_sign_up(name,email_id,password) VALUES ('%s','%s','%s')" % (self.name,self.email_id,self.password))
        con.commit()
        cur.close()
        con.close()
        print("Records are stored successfully")

#signup = customer_sign_up()
#signup.get_details()
            
            
            
