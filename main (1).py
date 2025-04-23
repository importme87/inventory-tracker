#define the main function that runs the purchase tracking system
def purchase():
    
    #list to store all purchase dictionaries
    add_purchase = []
   
    #main menu loop
    while True:
        print("n/Menu:")
        print("Click [1] to add an item ")
        print("Click [2] to view")
        print("Click [3] to exit")
        
        #ask the user to choose an operation
        operation = int(input("Enter your choice:"))
        
        #option 1: add a new purchase 
        if operation == 1:
            
            item_category = input("Enter the category")
            item_name = input("Enter the item name")
            item_quantity = input("Enter the quantity")
            item_date = input("Enter the date")
            
            #create a dictionary for the new item
            item = {
            "name": item_name,
            "quantity": item_quantity,
            "date": item_date,
            "category": item_category
        }
            
            #add the new item to the purchase list
            add_purchase.append(item)
            
            #confirm the item was added
            print(f'you added, {item["category"]}, {item["name"]}, {item["quantity"]}, {item["date"]}, on the list')
        
        #option 2: view purchases (with filters)    
        elif operation == 2:
            
            view_category = input("Enter the category (or press Enter to skip): ")
            view_name = input("Enter the item name (or press Enter to skip): ")
            view_quantity = input("Enter the quantity (or press Enter to skip): ")
            view_date = input("Enter the date (or press Enter to skip): ")
            
            #loop through purchases and apply filter check
            for purchase in add_purchase:
                if matches_filters(purchase, view_category, view_name, view_quantity, view_date):
                   print(f'{purchase["name"]}')
                   print(f'{purchase["quantity"]}')
                   print(f'{purchase["date"]}')
        
        #option 3: exit the loop    
        elif operation == 3:
            break
        
        #handle invalid input
        else:
            print("Invalid choice. Please try again")
        
# helper function to check if a purchase matches selected filters    
def matches_filters(purchase, view_category, view_name, view_quantity, view_date):
    
    if view_category != "" and view_category != purchase["category"]:
        return False
    elif view_name != "" and view_name != purchase["name"]:
        return False
    elif view_quantity != "" and view_quantity != purchase["quantity"]:
        return False
    elif view_date != "" and view_date != purchase["date"]:
        return False
    else:
        return True

#call the function to start the program        
purchase()
        

        
        
        
        
        
            



    


 