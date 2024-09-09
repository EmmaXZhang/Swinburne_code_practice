import csv
# global array
product_id=[]
product_name=[]
category=[]
price=[]
quantity_in_stock=[]
supplier=[]

# load data in matrix
csv_file = "data.csv"
matrix = []


# with-> resource management, open()-> open a file, read-only
with open(csv_file, mode='r') as product_inventory:
    product_data = csv.reader(product_inventory)
    # skip header row
    next(product_data)
    # add product detail data to matrix format
    for row in product_data:
        # matrix.append(row)-----------------------
        product_id.append(int(row[0]))
        product_name.append(row[1])
        category.append(row[2])
        price.append(float(row[3]))
        quantity_in_stock.append(int(row[4]))
        supplier.append(row[5])

#------------ load data in parallel arrays-------------
# for row in matrix:
#     product_id.append(row[0])
#     product_name.append(row[1])
#     category.append(row[2])
#     price.append(row[3])
#     quantity_in_stock.append(row[4])
#     supplier.append(row[5])



# print product inventory data in format
def display_data():
    print(f"{'Product_Id':>10} {'Product_Name':<50} {'Category':<10} {'Price':>10} {'Quantity_in_Stock':>19} {'Supplier':<13}")
    print("-" * 50)
    for i in range(len(product_id)):
        print(f"{product_id[i]:>10} {product_name[i]:<50} {category[i]:<10} {price[i]:>10.2f} {quantity_in_stock[i]:>19} {supplier[i]:<13}")

display_data()
