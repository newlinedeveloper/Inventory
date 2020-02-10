#product details
import cx_Oracle
import random

con = cx_Oracle.connect("system/26011999")
cur = con.cursor()
class product_details:
    character = "abcdefghijklmnopqrstuvwxyz"
    digit = "1234567890"
    key_len = 20
    def base_str(self):
        return(product_details.character + product_details.digit)

    def key_gen(self):
        keylist = [random.choice(self.base_str()) for i in range(product_details.key_len)]
        return("".join(keylist))

        
        

    def add_product(self):
        print("~"*50)
        print("ADD PRODUCT DETAILS")
        print("-"*50)
        self.product_category = input("Enter your product category: ")
        self.product_name = input("Enter your product name: ")
        self.product_id = self.key_gen()
        print("your product id is: ",self.product_id)
        self.p_quantity = input("Enter no of products: ")
        self.p_price = input("Enter the product price: ")
        print("-"*50)
        print("~"*50)
        return self.add_database()
    

    def edit_product(self):
        m = 0
        print("~"*50)
        print("EDIT PRODUCT DETAILS")
        print("-"*50)
        while True:
            
            pid = input("\nEnter your product id: ")
            cur.execute("select p_id from seller_products where p_id = '%s'" % (pid))
            value = cur.fetchone()
            if value[0] != '':
                self.product_id = value[0]
                self.product_category = input("Enter your product category: ")
                self.product_name = input("Enter your product name: ")
                self.p_quantity = input("Enter no of products: ")
                self.p_price = input("Enter the product price: ")
                cur.execute("UPDATE seller_products SET p_category = '%s',p_name = '%s',p_quantity = '%s',p_price = '%s' WHERE p_id = '%s'" % (self.product_category,self.product_name,self.p_quantity,self.p_price,pid))
                con.commit()
                break
            else:
                print("INVALIED PRODUCT ID!!!!")

        print("-"*50)
        print("~"*50)
        return self.display()
    

    def delete_product(self):
        m=0
        print("~"*50)
        print("DELETE PRODUCT DETAILS")
        print("-"*50)
        while True:
            pid = input("Enter product id: ")
            cur.execute("select p_id from seller_products where p_id = '%s'" % (pid))
            value = cur.fetchone()
            if value[0] != '':
                #cur.execute("select * from seller_products where p_id = '%s'" % (pid))
                
                cur.execute("DELETE FROM seller_products WHERE p_id = '%s'" % (pid))
                con.commit()
                print("PRODUCT IS DELETED SUCCESSFULLY")
                break
     
            else:
                print("INVALID PRODUCT KEY!!!!!")
                
        print("-"*50)
        print("~"*50)
        

    def display(self):
        print("~"*50)
        print("DETAILS")
        print("-"*50)
        print("your product category: ",self.product_category)
        print("your prduct name : ",self.product_name)
        print("your product id :",self.product_id)
        print("your producpt quantity: ",self.p_quantity)
        print("your product price(per each): ",self.p_price)
        print("-"*50)
        print("~"*50)


    def add_database(self):
        #import cx_Oracle
        #con = cx_Oracle.connect("system/26011999")
        #cur = con.cursor()
        cur.execute("INSERT INTO seller_products(p_id,p_category,p_name,p_quantity,p_price) VALUES ('%s','%s','%s','%s','%s')" % (self.product_id,self.product_category,self.product_name,self.p_quantity,self.p_price))
        con.commit()
        #cur.close()
        #con.close()
        print("PRODUCT ADDED SUCCESSFULLY!!!!!")
        return self.display()
        



product = product_details()
#product.append(product_details())

print("$"*60)
print("-"*60)
print("PRODUCT DETAILS")
print("-"*60)
print("$"*60)
while True:
    print("\n1-Add products")
    print("2-Edit products")
    print("3-Delete products")
    print("4-Exit")
    choice = int(input("Enter your choice: "))
    if choice < 4:
        if choice == 1:
            product.add_product()
        elif choice == 2:
            product.edit_product()
        else:
            product.delete_product()
    elif choice == 4:
        cur.close()
        con.close()
        exit()
    else:
        print("INVALIED OPTION")
            
