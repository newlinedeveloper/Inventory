import random
#product details

class add_products:
    
    character = "abcdefghijklmnopqrstuvwxyz"
    digit = "1234567890"
    key_len = 20
    def base_str(self):
        return(add_products.character + add_products.digit)

    def key_gen(self):
        keylist = [random.choice(self.base_str()) for i in range(add_products.key_len)]
        return("".join(keylist))

    def add(self):
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
        return self.database()

    def database(self):
        import cx_Oracle
        con = cx_Oracle.connect("system/26011999")
        cur = con.cursor()
        cur.execute("INSERT INTO seller_products(p_id,p_category,p_name,p_quantity,p_price) VALUES ('%s','%s','%s','%s','%s')" % (self.product_id,self.product_category,self.product_name,self.p_quantity,self.p_price))
        con.commit()
        cur.close()
        con.close()
        print("PRODUCT ADDED SUCCESSFULLY!!!!!")
        return self.display()

    def display(self):
        print("~"*50)
        print("DETAILS")
        print("-"*50)
        print("your product category: ",self.product_category)
        print("your prduct name : ",self.product_name)
        print("your product id :",self.product_id)
        print("your product quantity: ",self.p_quantity)
        print("your product price(per each): ",self.p_price)
        print("-"*50)
        print("~"*50)

        #return self.database()



class edit_products(add_products):

    def edit(self,products):
        m = 0
        print("~"*50)
        print("EDIT PRODUCT DETAILS")
        print("-"*50)
        while True:
            p_id = input("Enter product id: ")
            for i in range(0,len(products)):
                if products[i].product_id == p_id:
                    m = i
                    break
            if products[m].product_id == p_id:
                products[m].product_category = input("Enter your product category: ")
                products[m].product_name = input("Enter your product name: ")
                products[m].p_quantity = input("Enter no of products: ")
                products[m].p_price = input("Enter the product price: ")
                self.database(products[m].product_id,products[m].product_category,products[m].product_name,products[m].p_quantity,products[m].p_price)
                print("-"*50)
                print("~"*50)
                products[m].display()
                return self.database

    def database(self,pid,pcat,pname,pquan,pprice):
        import cx_Oracle
        con = cx_Oracle.connect("system/26011999")
        cur = con.cursor()
        cur.execute("UPDATE seller_products SET p_category = '%s',p_name = '%s',p_quantity = '%s',p_price = '%s' WHERE p_id = '%s'" % (pcat,pname,pquan,pprice,pid))
        con.commit()
        cur.close()
        con.close()
        print("PRODUCTS ARE UPDATED SUCCESSFULLY!!!!!")
        
        

        

class delete_products(add_products):

    def delete(self,products):
        m=0
        print("~"*50)
        print("DELETE PRODUCT DETAILS")
        print("-"*50)
        while True:
            p_id = input("Enter product id: ")
            for i in range(0,len(products)):
                if products[i].product_id == p_id:
                    m = i
                    break
            if products[m].product_id == p_id:
                products[m].display()
                self.database(products[m].product_id)
                products.remove(products[m])
                #print("PRODUCT IS DELETED SUCCESSFULLY")
                #self.database(products[m].product_id)
                break
        print("-"*50)
        print("~"*50)

    def database(self,pid):
        import cx_Oracle
        con = cx_Oracle.connect("system/26011999")
        cur = con.cursor()
        cur.execute("DELETE FROM seller_products WHERE p_id = '%s'" % (pid))
        con.commit()
        cur.close()
        con.close()
        print("PRODUCTS ARE DELETED SUCCESSFULLY!!!!!")
        #return self.display()



add_product = edit_product = delete_product = []

print("$"*60)
print("-"*60)
print("PRODUCT DETAILS")
print("-"*60)
print("$"*60)
while True:
    print("1-Add products")
    print("2-Edit products")
    print("3-Delete products")
    print("4-Exit")
    choice = int(input("Enter your choice: "))
    if choice < 4:
        if choice == 1:
            add_product.append(add_products())
            add_product[-1].add()
        elif choice == 2:
            edit_product.append(edit_products())
            edit_product[-1].edit(add_product)
        else:
            delete_product.append(delete_products())
            delete_product[-1].delete(add_product)
    elif choice == 4:
        exit()
    else:
        print("INVALIED OPTION")
            

        
        
        

    
    
