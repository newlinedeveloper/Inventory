# seller login form
import cx_Oracle



class seller_login:

    def get_details(self):
        
        print("%"*60)
        print("-"*60)
        self.name = input("\nEnter your username or email id: ")
        self.password = input("Enter your password : ")
        print()
        print("-"*60)
        print("%"*60)

    def database(self):
        import cx_Oracle
        con = cx_Oracle.connect("system/26011999")
        cur = con.cursor()
        cur.execute("select * from seller_sign_up where user_name = '%s' or email_id = '%s' and password = '%s'" % (self.name,self.name,self.password))
        

    def display(self):
        print()
        print("#"*60)
        print("-"*60)
        print("HAI ", self.name)
        print("-"*60)
        print("#"*60)
login = seller_login()
