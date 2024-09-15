
# Load_records function
import csv
# global array
product_ids = []
product_names = []
categories = []
prices = []
quantity_in_stock = []
suppliers = []
csv_file = "product_data2.csv"

def load_record(file):
    with open(file, mode='r') as product_inventory:
        product_data = csv.reader(product_inventory)
        # skip header row
        next(product_data)
        # add product detail data to matrix format
        for row in product_data:
            product_ids.append(int(row[0]))
            product_names.append(row[1])
            categories.append(row[2])
            prices.append(float(row[3]))
            quantity_in_stock.append(int(row[4]))
            suppliers.append(row[5])

# Display
def display_data():
    load_record(csv_file)
    print(f"{'Product_Id':>10} {'Product_Name':<45} {'Category':<10} {'Price':>10} {'Quantity_in_Stock':>19} {'Supplier':<13}")
    print("-" * 110)
    for i in range(len(product_ids)):
        print(f"{product_ids[i]:>10} {product_names[i]:<45} {categories[i]:<10} {prices[i]:>10.2f} {quantity_in_stock[i]:>19} {suppliers[i]:<13}")

# Add record
def add_data():
    product_name = input("Product Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Quantity in Stock: "))
    supplier = input("Supplier: ")
    # create new id variable
    new_id = product_ids[-1] + 1 if product_ids else 1001
    product_ids.append(new_id)
    product_names.append(product_name)
    categories.append(category)
    prices.append(price)
    quantity_in_stock.append(stock)
    suppliers.append(supplier)

# Delete record
def delete_data():
    # no products in the file
    if not product_ids:
        print("No records to delete.")
        return
    # else display data
    display_data()

    # check if id exist,
    # In a while True loop, the loop itself will run indefinitely until you explicitly break out of it.
    while True:
        try:
            delete_id = int(input("Enter the Product Id to be deleted: "))
            if delete_id in product_ids:
                break
            else:
                print("Product ID not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric Product ID.")
    # find ID, and remote it
    delete_index = product_ids.index(delete_id)
    product_ids.pop(delete_index)
    product_names.pop(delete_index)
    categories.pop(delete_index)
    prices.pop(delete_index)
    quantity_in_stock.pop(delete_index)
    suppliers.pop(delete_index)
    print(f"Product with ID {delete_id} deleted successfully.")

# Save record
def save_data():
    with open(csv_file, mode="w", newline="") as product_inventory:
        writer = csv.writer(product_inventory)
        writer.writerow(["Product_Id", "Product_Name", "Category", "Price", "Quantity_in_Stock", "Supplier"])
        for i in range(len(product_ids)):
            writer.writerow([product_ids[i], product_names[i], categories[i], prices[i], quantity_in_stock[i], suppliers[i]])
        print("Records saved successfully.")

# Exit
def exit_app():
    print("Exiting the application successfully.")
    exit()


def menu():
    while True:
        print("Choose menu option: \n 1.Load records \n 2.Display \n 3.Add record \n 4.Delete record \n 5.Save records \n 6.Exit")
        user_choice = input("Select: ")

        match user_choice:
            case 1:
                load_record(csv_file)

            case 2:
                display_data()
            case 3:
                add_data()
            case 4:
                delete_data()
            case 5:
                save_data()
            case 6:
                exit_app()
            case _:
                print("Invalid option. Please select from 1 to 6.")

