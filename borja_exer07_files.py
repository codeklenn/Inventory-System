#Klenn Jakek Borja
#CMSC 12 T2-1L
#Inventory File Handling Module

#saveInventory function
#saving the user-inputted data to inventory.dat
def saveInventory(products):
    fp = open("inventory.dat", "w")
    #for loop dictionary
    for k,v in products.items():
        fp.write(str(k) + "," + str(v[0]) + "," + str(v[1]) + "," + str(v[2])+ "\n")
    fp.close()


#load inventory function
#loading inventory.dat
def loadInventory(products):
    fp = open("inventory.dat", "r")
    #reads every line
    for line in fp:
        data = line.split(",")
        product_id = data[0]
        product_name = data[1]
        product_description = data[2]
        product_quantity = data[3]
        products[product_id]= [product_name, product_description, int(product_quantity)]
    fp.close()
        




	

