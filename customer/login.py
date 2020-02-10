#customer login form

class customer_login:

    def getdetails(self):

        self.name_email_id = input("Enter your username or email id: ")
        self.password = input("Enter your password: ")
        import cx_Oracle
        con = cx_Oracle.connect("system/26011999")
        cur = con.cursor()
        cur.execute("SELECT name from customer_sign_up where name = '%s' or email_id = '%s' and password = '%s'" % (self.name_email_id,self.name_email_id,self.password))
        name = str(cur.fetchall())
        if 
        print("\n HAI ",name)
        con.commit()
        cur.close()
        con.close()

login = customer_login()
