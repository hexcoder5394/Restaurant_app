import time
import sys

# Define a Menu class to store menu items and their prices.
class Menu:
    def __init__(self):

        # Define a dictionary to store menu items and their prices.
        self.items = {
            "House Cured Bourbon Gravadlax": 9.99, 
            "Bloc de pate": 14.99, 
            "village market testing plate": 7.99, 
            "White's Out seafood cocktail": 14.99, 
            "Essex camembert souffle": 9.99,
            "Beef": 45.99, 
            "Steak Diane": 49.99, 
            "Lobster": 49.99, 
            "Rack of Welsh lamb": 24.99, 
            "pan fried cod loin": 24.99, 
            "Charred cauliflower steak": 29.99,
            "poached alice pears": 8.99, 
            "Apricot & brandy macaroon": 7.99, 
            "Floating island": 7.99, 
            "Dark chocolate & strawberry cheesecake": 8.99, 
            "Macadamia blondie & chocolate brownie": 5.99,
            "Coffee & biscuits": 5.99,
            "Wine": 8, 
            "Water": 1, 
            "Soda": 2
        }
        
         # Initialize a dictionary to track the popularity of menu items.
        self.menu_popularity  = {item: 0 for item in self.items.keys()}

     # Display the menu items and their prices.
    def display_items(self):
        for item in self.items:
            print(item, self.items[item])



# Define a Restaurant class to manage restaurant operations.
class Restaurant:
    def __init__(self):
        # Initialize dictionaries to manage tables for early and late sessions.
        self.earlysession_tables = {i: {"status": "Free", "Session": "", "Customer Name": "", "Number of Diners": 0, "orders": {}, "cost": 0} for i in range(1, 6)}
        self.latesession_tables = {i: {"status": "Free", "Session": "", "Customer Name": "", "Number of Diners": 0, "orders": {}, "cost": 0} for i in range(1, 6)}

        # Initialize lists to keep track of booked tables.
        self.earlysession_booked_tables = []
        self.latesession_booked_tables = []

        # Initialize a list to store priority orders (Lobster and Steak Diane).
        self.priority_orders = []
        # Initialize variables to track total income, table costs, and tips.
        self.total_income = 0
        self.table_costs = {}
        self.total_amount_tips = 0

        # Create an instance of the Menu class to manage menu items.
        self.menu = Menu()

      # Method to place an order for a table.
    def place_order(self):
        global table
        tip_value = 0
        sessions = ["1. Early Session", "2. Late session"]
        for i in range(len(sessions)):
            print(sessions[i])
        
        try:
            
            Session = int(input("Enter Session: "))
            if (Session == 1 or Session == 2):
                cus_name = input("Customer Name: ")
                nod = int(input("Number of Diners: "))
                if (1 <= nod <= 8):
                    if Session == 1:
                        self.earlysession_order_items = {}
                        self.order_fee = 0
                        table_number = int(input("Table Number(1-5): "))
                        if (1 <= table_number <= 5):
                            if table_number not in self.earlysession_booked_tables:
                                table = self.earlysession_tables[table_number]
                                order_item = input("Enter Item (0 to finish): ")
                                while order_item != "0":
                                    q = int(input("Quantity: "))
                                    self.earlysession_order_items[order_item] = q
                                    order_item = input("Enter Item (0 to finish): ")
                            
                                tip = int(input("Leave a Tip(1.yes/2.no)"))
                                if (tip == 1):
                                    tip_value = int(input("Tip Value: "))
                                

                                for item in self.earlysession_order_items.keys():
                                    if item in ["Lobster", "Steak Diane"]:
                                        self.priority_orders.append(item)
                                        #table["orders"].append("Main Course", item)
                                        #order_items.remove(item)

                                    self.order_fee += self.menu.items[item] * self.earlysession_order_items[item]
                                    self.menu.menu_popularity[item] += 1
                                table["orders"].update(self.earlysession_order_items)
                                table["Session"] = "Early Session"
                                table["Customer Name"] = cus_name

                                if len(self.earlysession_order_items) != 0:
                                    print("Select Payment Method")
                                    payment_methods = ["1. Credit/Debit Card", "2. Cash"]
                                    for i in range(len(payment_methods)):
                                        print(payment_methods[i])
                                    pay_method = int(input("Enter Payment Method: ")) 
                                    if pay_method == 1:
                                        self.order_fee += self.order_fee * 0.1
                                    
                                    print(f"Table Booked Successfully, Total Cost: ${self.order_fee}")
                                    table["status"] = "Booked"
                                    table["Number of Diners"] = nod
                                    table["cost"] = self.order_fee

                                self.total_income += self.order_fee
                                self.total_amount_tips += tip_value
                                self.table_costs[table_number] = self.table_costs.get(table_number, 0) + self.order_fee
                                self.earlysession_booked_tables.append(table_number)
                            else:
                                print(f"Table {table_number} Already Booked for early night session")
                        else:
                            print("Wrong Table Number")

                    elif Session == 2:
                        self.latesession_order_items = {}
                        self.order_fee = 0
                        table_number = int(input("Table Number(1-5): "))
                        if (1 <= table_number <= 6):
                            if table_number not in self.latesession_booked_tables:
                                table = self.latesession_tables[table_number]
                                order_item = input("Enter Item (0 to finish): ")
                                while order_item != "0":
                                    q = int(input("Quantity: "))
                                    self.latesession_order_items[order_item] = q
                                    order_item = input("Enter Item (0 to finish): ")

                                tip = int(input("Leave a Tip(1.yes/2.no)"))
                                if (tip == 1):
                                    tip_value = int(input("Tip Value: "))

                                for item in self.latesession_order_items.keys():
                                    if item in ["Lobster", "Steak Diane"]:
                                        self.priority_orders.append(item)
                                        #table["orders"].append(("Main Course", item))
                                        #order_items.remove(item)

                                    self.order_fee += self.menu.items[item] * self.latesession_order_items[item]
                                    self.menu.menu_popularity[item] += 1
                                table["orders"].update(self.latesession_order_items)
                                table["Session"] = "Late Session"
                                table["Customer Name"] = cus_name

                                
                                if len(self.latesession_order_items) != 0:
                                    print("Select Payment Method")
                                    payment_methods = ["1. Credit/Debit Card", "2. Cash"]
                                    for i in range(len(payment_methods)):
                                        print(payment_methods[i])
                                    pay_method = int(input("Enter Payment Method: ")) 
                                    if pay_method == 1:
                                        self.order_fee += self.order_fee * 0.1
                                    
                                    print(f"Table Booked Successfully, Total Cost: ${self.order_fee}")

                                    table["status"] = "Booked"
                                    table["Number of Diners"] = nod
                                    table["cost"] = self.order_fee

                                self.total_income += self.order_fee
                                self.total_amount_tips += tip_value
                                self.table_costs[table_number] = self.table_costs.get(table_number, 0) + self.order_fee
                                self.latesession_booked_tables.append(table_number)
                            else:
                                print(f"Table {table_number} Already Booked for late night session ")
                        else:
                            print("Wrong table number")
                else:
                    print("Diners up to a maximum of eight allowed for a table")
            else:
                print("Invalid Session")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

     # Method to calculate and display total income and tips collected.
    def income(self):
        try:
            print(f"Total Income: ${self.total_income}")
            print(f"Total Tips collected for Today: ${self.total_amount_tips}")
        except Exception as e:
            print(f"An error occurred while calculating income: {str(e)}")

    # Method to display table status and max table
    def table_status(self):
        try:
            print("Early Session Tables 6pm - 8pm")
            for i in range(1, 6):
                print("Table", i, self.earlysession_tables[i])
            
            print("Late Session Tables 8pm - 10pm")
            for i in range(1, 6):
                print("Table", i, self.latesession_tables[i])

            max_table = max(self.table_costs, key=self.table_costs.get)
            print(f"Table {max_table} has the highest cost: ${self.table_costs[max_table]}")
        except Exception as e:
            print(f"An error occurred while displaying table status: {str(e)}")

    # Method to display menu popularity
    def popularity(self):
        try:
            popularity = sorted(self.menu.menu_popularity.items(), key=lambda x: x[1], reverse=True)
            for item, count in popularity:
                print(f"{item}: {count} orders")
        except Exception as e:
            print(f"An error occurred while displaying menu popularity: {str(e)}")

    # Method to add beverages
    def beverages(self):
        beverage_items = ["Coffee & biscuits", "Wine", "Water", "Soda"]
        sessions = ["1. Early Session", "2. Late session"]
        for i in range(len(sessions)):
            print(sessions[i])
        sess = int(input("Session: "))
        try:
            if (sess == 1):
                print(f"Early Session Booked Tables: {self.earlysession_booked_tables}")
                table_num = int(input("Table Number: "))
                if table_num in self.earlysession_booked_tables:
                    item = input("Enter Item: ")
                    while (item != "0"):
                        if item in beverage_items:
                            q = int(input("Quantity: "))
                            cost = self.menu.items[item] * q
                            self.earlysession_tables[table_num]["orders"][item] = q
                            self.earlysession_tables[table_num]["cost"] += cost
                            self.total_income += cost
                            self.table_costs[table_num] = self.table_costs.get(table_num, 0) + cost
                            self.menu.menu_popularity[item] += 1
                            print("Beverages Added Successfully")
                            item = input("Enter Item: ")
                        else:
                            print("Item not added !!!")
                            break
                else:
                    print(f"Table {table_num} isn't Book yet for Early session")
            
            elif (sess == 2):
                print(f"Late Session Booked tables: {self.latesession_booked_tables}")
                table_num = int(input("Table Number: "))
                if table_num in self.latesession_booked_tables:
                    item = input("Enter Item: ")
                    while (item != "0"):
                        if item in beverage_items:
                            q = int(input("Quantity: "))
                            cost = self.menu.items[item] * q
                            self.latesession_tables[table_num]["orders"][item] = q
                            self.latesession_tables[table_num]["cost"] += cost
                            self.total_income += cost
                            self.table_costs[table_num] = self.table_costs.get(table_num, 0) + cost
                            self.menu.menu_popularity[item] += 1
                            print("Beverages Added Successfully")
                            item = input("Enter Item: ")
                        else:
                            print("Item not added !!!")
                            break
                else:
                    print(f"Table {table_num} isn't Book yet for Late Session")
            else:
                print("Invalid Session")
        except ValueError:
            print("Invalid input. Please enter a valid number")


    
    def run(self):
        # Dictionary to store the runtimes of different options
        runtimes = {}
        while True:
            # Display the available menu options
            print("Options: ")
            options = ["1. Book a Table", "2. Tables Status & Costs", "3. Total Income & Tips", "4. Menu Popularity", "5. Add Beverages", "6. Exit", "!!Runtimes"]

            for i in range(len(options)):
                print(options[i])

            opt = str(input("Select Option: "))
            try:
                if opt == "1":
                    # Option 1: Book a Table
                    start1 = time.time() # Start measuring the runtime
                    self.menu.display_items()
                    self.place_order()  # Call the method to book a table and place orders
                    end1 = time.time() # End measuring the runtime
                    runtime1 = end1 - start1
                    runtimes["runtime1"] = runtime1
                elif opt == "2":
                     # Option 2: Tables Status & Costs
                    print("Tables Status & Table Costs")
                    start2 = time.time()
                    self.table_status() # Call the method to display table statuses and costs
                    end2 = time.time()
                    runtime2 = end2 - start2
                    runtimes["runtime2"] = runtime2
                elif opt == "3":
                    # Option 3: Total Income & Tips
                    print("Total Income & Total amount of Tips")
                    start3 = time.time()
                    self.income()   # Call the method to display total income and tips
                    end3 = time.time()
                    runtime3 = end3 - start3
                    runtimes["runtime3"] = runtime3
                elif opt == "4":
                    # Option 4: Menu Popularity
                    start4 = time.time()
                    print("Menu Popularity")
                    self.popularity()   # Call the method to display menu item popularity
                    end4 = time.time()
                    runtime4 = end4 - start4
                    runtimes["runtime4"] = runtime4
                elif opt == "5":
                     # Option 5: Add Beverages
                    print("Alcoholic or non-alcoholic beverages")
                    start5 = time.time()
                    self.beverages()     # Call the method to add beverages to a booked table
                    end5 = time.time()
                    runtime5 = end5 - start5
                    runtimes["runtime5"] = runtime5
                elif opt == "6":
                    # Option 6: Exit the progra
                    exit()
                elif opt == "0":
                    # Option 0: Display runtime information
                    for i in runtimes:
                        print(i, runtimes[i])
                     # Display the memory size of earlysession and latesession tables dictionaries
                    print("Memmory size of earlysession tables dictionary: ",sys.getsizeof(self.earlysession_tables), 
                          "Memmory size of latesession tables dictionary: ",sys.getsizeof(self.latesession_tables))
                else:
                    print("Invalid Option")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.run()
