#admin login form

class admin_login:

    def __init__(self):

        self.name_email_id = input("Enter your username or email id: ")
        self.password = input("Enter your password: ")
        while True:
            
           if self.name_email_id == "veera" or self.name_email_id == "veerasolaiyappan@gmail.com":
               if self.password == "26011999":
                   print("login successfully")
                   break
               else:
                    print("invalid password")
                    self.name_email_id = input("Enter your username or email id: ")
                    self.password = input("Enter your password: ")
           else:
                print("invalid username")
                self.name_email_id = input("Enter your username or email id: ")
                self.password = input("Enter your password: ")
        
       
#login = customer_login()
