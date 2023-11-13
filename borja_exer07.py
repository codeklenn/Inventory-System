#Klenn Jakek V. Borja
#CMSC 12 - Lab T21L
#Inventory System

#function for adding a product. first make the user input a product id, if it already exists
#it will say that it already exists
#otherwise, the user shall input a product name, description, and quantity. they are values in a list
#it will return then the product in the products dictionary
import borja_exer07_files
def add_product(d1):
	product_id = input("Enter product ID: ")

	if product_id in d1:
		print("Product already exists")
		return d1
	else:
		product_name = input("Enter product name: ")
		product_description = input("Enter product description: ")
		product_quantity = int(input("Enter product quantity: "))
		#adding keys : value
		d1[product_id] = [product_name, product_description, product_quantity]

		return d1

#function for viewing the products. using the items() function, i can loop over the
#keys and values of the products, and specify which one to use
def view_products(products):
	print(10*"-" + "View Products" + 10*"-")
	if products == {}:
		print("Put a product first.")
	else:
		for k, v in products.items():
			print(k)
			print("Name: ", v[0])
			print("Description: ", v[1])
			print("Quantity: ", v[2])

#function for deleting the products. the user shall first input a product_id which will
#be checked whether it exists, or not. If it exists, using the del keyword, the product_id is deleted.
def delete_product(products):
	print(10*"-" + "Delete Product" + 10*"-")
	if products == {}:
		print("Put a product first.")
	else:
		product_id = input("What ID do you want to delete?: ")
		if product_id in products:
			del products[product_id]
			print("Successfully deleted product!")
		else:
			print("This product does not exist.")	
#function for deleting all the products. using the clear() function, the whole inventory
#is deleted
def deleteall_products(products):
	products.clear()
	print("You have cleared your inventory!")

#function for restocking the product. the user shall first input a product_id, where it
#will be checked whether it exists in the inventory. If it exists, the user shall input
#how many they would like to restock
#using the items() function, we can add the restocks to the stocks
def restock_product(products):
	if products == {}:
		print("Put a product first.")
	else:
		product_id = input("What product do you want to restock? (give id): ")
		if product_id in products:
			restock = int(input("How many would you like to restock?: "))
			for k,v in products.items():
				v[2] = v[2] + restock
		else:
			print("This product does not exist.")

#function for consuming the product. the user shall first input a product_id, where it
#will be checked whether it exists in the inventory. If it exists, the user shall input
#how many they would like to consume
#using the items() function, we can subtract the consume to the stocks
#if consume is greater than the given stocks, it will be prompted that the user
#does not have enough stocks
def consume_product(products):
	if products == {}:
		print("Put a product first.")
	else:
		product_id = input("What product do you want to consume? (give id): ")
		if product_id in products:
			consume = int(input("How many would you like to consume?: "))
			for k,v in products.items():
				if consume > v[2]:
					print("You do not have enough stocks!")
				else:
					v[2] = v[2] - consume
		else:
			print("This product does not exist.")

#menu function

def menu():
	products = {}
	while True:
		print(10*"-" + "MENU" + 10*"-")
		print("[1] Add New Product")
		print("[2] View all Products")
		print("[3] Delete a Product")
		print("[4] Delete All Products")
		print("[5] Restock a Product")
		print("[6] Consume a Product")
		print("[7] Load Inventory")
		print("[8] Save Inventory")
		print("[0] Exit")

		choice = input("Enter your choice: ")
		if choice == "1":
			products = add_product(products)
			print(products)
		elif choice == "2":
			view_products(products)
		elif choice == "3":
			delete_product(products)
		elif choice == "4":
			deleteall_products(products)
		elif choice == "5":
			restock_product(products)
		elif choice == "6":
			consume_product(products)
		elif choice == "7":
			borja_exer07_files.loadInventory(products)
		elif choice == "8":
			borja_exer07_files.saveInventory(products)
		elif choice == "0":
			print("Goodbye!")
			break
		else:
			print("Wrong input.")

menu()