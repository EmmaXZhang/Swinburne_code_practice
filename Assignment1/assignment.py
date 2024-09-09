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
        matrix.append(row)
print(matrix)

# load data in parallel arrays
for row in matrix:
    product_id.append(row[0])
    product_name.append(row[1])
    category.append(row[2])
    price.append(row[3])
    quantity_in_stock.append(row[4])
    supplier.append(row[5])

print(product_id)
print(product_name)
print(category)
print(price)
print(quantity_in_stock)
print(supplier)

