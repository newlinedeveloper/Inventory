# signup module
# It gets references as arguments of user_name, email_id, password, conform_password

# sqlite3 database is imported


'''#create signup class
class signup:

    # define constructor for store user data on database
    def __init__(self,name,email_id,password,conform_password):

def get_details():
    import sqlite3

    con = sqlite3.connect('sample.db')
    print("The database opened")

    name = input("Enter your name: ")
    email_id = input("Enter your Email_id: ")
    password = input("Enter your password: ")
    c_password = input("Enter your conform_password: ")
    con.execute('CREATE TABLE sign_up(user_name varchar(50), email_id varchar(50), password varchar(50), conform_password varchar(50));')
    con.execute('INSERT INTO sign_up(user_name,email_id,password,conform_password) VALUES ("%s","%s","%s","%s")' % (name,email_id,password,c_password))
    con.commit()
    con.close()
    return(print("Record is inserted successfully"))
    name = input("Enter your name: ")
    email_id = input("Enter your email_id: ")
    password = input("Enter your password: ")
    conform_password = input("Enter the conform_password:")

    while True:
        if password == conform_password:
            break
        else:
            password = input("Enter your password: ")
            conform_password = input("Enter the conform_password:")
    
    import sqlite3
    con = sqlite3.connect('sample.db')
    con.execute('INSERT INTO signup(username,email_id,password,conform_password) VALUES("%s","%s","%s","%s")' % (name,email_id,password,conform_password))
    print("The records are stored successfully")
    con.close()


name = input("Enter your name: ")
email_id = input("Enter your email_id: ")
password = input("Enter your password: ")
conform_password = input("Enter your conform password: ")
'''
import sqlite3
con = sqlite3.connect('sample.db')
print("The database opened")
#con.execute("INSERT INTO sign_up VALUES('%s','%s','%s','%s')" % (name,email_id,password,conform_password))
#print("The details are inserted successfully")
c = con.cursor()
c.execute("SELECT * FROM sign_up")
all_rows = c.fetchall()
print("Records are:")
for row in all_rows:
    print('{0}:{1},{2}'.format(row[0],row[1],row[2]))
con.commit()
#con.close()
