#import sign_up
# customer account details


class seller_address_details:

    def address(self):
        print("#"*30)
        print("-"*30)
        print("WELCOME ")
        print("-"*30)
        print("#"*30)
        self.email_id = input("\nEnter your email_id: ")
        self.address = input("\n Enter your Residental address:")
        self.area = input("\nEnter your area: ")
        self.city = input("\n Enter your city: ")
        self.district = input("Enter your district: ")
        self.state = input("Enter your state: ")
        self.country = input("Enter your country :")
        self.phone_no = input("Enter your mobile no: ")
        


    def account(self):
        print("@"*30)
        print("-"*30)
        print("WELCOME ")
        print("-"*30)
        print("@"*30)
        
        self.bank_name = input("Enter your bank :")
        self.ac_no = input("Enter your account no: ")

    def display(self):
        print("^"*60)
        print("-"*60)
        print("your email_id is: ",self.email_id)
        print("your address : ", self.address)
        print("your area : ", self.area)
        print("your city  : ", self.city)
        print("your district : ", self.district)
        print("your state : ", self.state)
        print("your country : ", self.country)
        print("your mobile no : ", self.phone_no)
        print("your bank is: ", self.ac_no)
        print("your ac_no  : ", self.bank_name)
        print("-"*60)
        print("^"*60)
        return self.database()

        def database(self):
            import cx_Oracle
            con = cx_Oracle.connect("system//26011999")
            cur= con.cursor()
            cur.execute("INSERT INTO seller_details('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"% (self.email_id,self.address,self.area,self.city,self.district,self.state,self.country,self.phone_no,self.bank_name,self.ac_no constraint sp_ac_pk primary key))
            con.commit()
            cur.close()
            con.close()
            return("\n Details are stored successfully!!!!")
            
details = seller_address_details()
#details.address()



        
        
