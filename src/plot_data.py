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

'''
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('src\merged_data.csv')

# Filter rows with the date '2024-01-14'
rows_2024_01_14 = df[df['Date of scrap'] == '2024-01-14']

# Filter rows with the date '2024-01-18'
rows_2024_01_18 = df[df['Date of scrap'] == '2024-01-18']

# Create a mapping of Product IDs to corresponding Product Types for '2024-01-18'
product_type_mapping = dict(zip(rows_2024_01_18['Product ID'], rows_2024_01_18['Product Type']))

# Replace 'Product Type' values for rows with '2024-01-14' using the mapping
df.loc[df['Date of scrap'] == '2024-01-14', 'Product Type'] = df['Product ID'].map(product_type_mapping)

# Save the updated DataFrame back to the CSV file
df.to_csv('your_updated_file.csv', index=False)
'''