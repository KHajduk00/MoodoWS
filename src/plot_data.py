'''
# Assuming your CSV file has a column named 'Sizes'
csv_file_path = 'path/to/your/file.csv'

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Access the 'Sizes' column
        sizes_list = row['Sizes'].strip('[]').replace("'", "").split(', ')

        # Check if 'S' is present in the sizes list
        if 'S' in sizes_list:
            print(f"Product {row['ProductID']} has size 'S'")
'''

'''
# Assuming your CSV file has a column named 'Sizes' and 'Price'
csv_file_path = 'path/to/your/file.csv'

# Lists to store data
product_ids = []
prices = []

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Access the 'Sizes' and 'Price' columns
        sizes_list = row['Sizes'].strip('[]').replace("'", "").split(', ')

        # Check if 'S' is present in the sizes list
        if 'S' in sizes_list:
            product_ids.append(row['ProductID'])
            prices.append(float(row['Price']))

# Plotting
plt.bar(product_ids, prices, color='blue')
plt.xlabel('Product ID')
plt.ylabel('Price')
plt.title('Prices of Products with Size "S"')
plt.show()
'''