'''Project - 1Project - 1
Create a dictionary-based mini project in Python to manage an inventory in stock. The user should have options to add new items, buy items, change the price of items, and update the inventory of current items. There should also be a total sales variable that is initially set to 0. The project should handle inventory, price, and count. The project should be broken down into steps with clear instructions for each step. Each step should be pushed to GitHub.

1. Create a new GitHub repository and set up a new Python project.

2. Define the inventory dictionary to hold item data and a variable for total sales.

3. Create a main function to run the program and print a welcome message.

4. Create a function add_item to add new items to the inventory with a specified name, price, and count.

5. Update the main function to include a menu option for adding new items.

6. Commit the changes to GitHub.

7. Create a function buy_item to handle buying items from the inventory, updating the item count and total sales.

8. Update the main function to include a menu option for buying items.

9. Commit the changes to GitHub.

10. Create a function change_price to update the price of an existing item in the inventory.

11. Update the main function to include a menu option for changing item prices.

12. Commit the changes to GitHub.

13. Create a function display_inventory to print the current state of the inventory and total sales.

14. Update the main function to include a menu option for displaying the inventory.

15. Commit the changes to GitHub.

16. Create a function update_inventory to update the count of an existing item in the inventory.

17. Update the main function to include a menu option for updating the inventory count of existing items.

18. Commit the changes to GitHub.

19. Review and refactor the code if necessary. Add comments and documentation to explain the functionality.

20. Add a final commit to GitHub with any refinements and the completed project.'''


inventory = {
    "Mobile": {"price": 1000, "count": 80},
    "Laptop": {"price": 2000, "count": 90},
    "TV": {"price": 500, "count": 70},
}

def main():
    print("Welcome to the inventory management system by ABC Electronics")
    
    def add_item():
        name = input("Enter the product name: ")
        price = float(input("Enter the price of product: "))  # Convert input to float
        count = int(input("Enter the count of product: "))    # Convert input to int
        inventory[name] = {"price": price, "count": count}
        print(inventory)
    
    def buy_item():
        name = input("Enter the product name: ")
        count = int(input("Enter the count of product: "))
        if name in inventory:
            if inventory[name]["count"] >= count:
                inventory[name]["count"] -= count
                print("Item purchased")
            else:
                print("Item not available")

    def change_price():
        name = input("Enter the name of product: ")
        if name in inventory:
            price = float(input("Enter the price: "))
            inventory[name]["price"] = price
            print("Price updated")
        else:
            print("Item not found in inventory")

    def update_inventory():
        name = input("Enter the product name: ")
        count = int(input("Enter the new count of product: "))
        if name in inventory:
            inventory[name]["count"] = count
            print("Count updated successfully")
        else:
            print("Item not available")

    def display_inventory():
        total_sales = 0
        print("Inventory")

        for key, values in inventory.items():
            print(f"{key}: {values['count']}")
            total_sales += values['price'] * values['count']
        
        print(f"Total sales: {total_sales}")

    while True:
        print("1. Add Item")
        print("2. Buy Item")
        print("3. Change Price")
        print("4. Display Inventory")
        print("5. Update Inventory Count")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_item()
        elif choice == 2:
            buy_item()
        elif choice == 3:
            change_price()
        elif choice == 4:
            display_inventory()
        elif choice == 5:
            update_inventory()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
