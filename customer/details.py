#import sign_up
# customer account details


class customer_address_details:

    def address(self):
        print("#"*30)
        print("-"*30)
        print("WELCOME ")
        print("-"*30)
        print("#"*30)

        self.address = input("\nEnter your Residental address:")
        self.area = input("\nEnter your area: ")
        self.city = input("\nEnter your city: ")
        self.district = input("\nEnter your district: ")
        self.state = input("\nEnter your state: ")
        self.country = input("\nEnter your country :")
        self.phone_no = input("\nEnter your mobile no: ")
        self.email_id = input("\nEnter your email_id: ")
        


    def account(self):
        print("@"*30)
        print("-"*30)
        print("WELCOME ")
        print("-"*30)
        print("@"*30)
        
        self.bank_name = input("\nEnter your bank      :")
        self.ac_no = input("\nEnter your account no: ")


    def database(self):
        import cx_Oracle
        con = cx_Oracle.connect("system/26011999")
        cur = con.cursor()
        cur.execute("INSERT INTO customer_details VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.email_id ,self.address,self.area,self.city,self.district,self.state,self.country,self.phone_no,self.bank_name,self.ac_no))
        con.commit()
        cur.close()
        con.close()
        return("Records are inserted successfully!!!")
    
    def display(self):
        print("^"*60)
        print("-"*60)
        print("your address  : ", self.address)
        print("your area     : ", self.area)
        print("your city     : ", self.city)
        print("your district : ", self.district)
        print("your state    : ", self.state)
        print("your country  : ", self.country)
        print("your mobile no: ", self.phone_no)
        print("your bank is  : ", self.ac_no)
        print("your ac_no    : ", self.bank_name)
        print("-"*60)
        print("^"*60)
        return self.database()
        
details = customer_address_details()
#details.address()



        
        
