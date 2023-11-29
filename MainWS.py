import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://moodo.pl/pol_m_KOLEKCJA-192.html")
#print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
data = soup.select('div[class="product col-6 col-sm-4 col-md-3 pt-3 pb-md-3 px-1 px-sm-3 px-md-4"]')
#print(data)


for i, x in enumerate(data):
    print(f"Element {i+1}: {x.text}")

print(f"Total number of elements: {len(data)}")

# Define keywords for types of clothing
clothing_keywords = ['Spódnica', 'Koszulka', 'Spodnie',
 'Sukienka', 'Sweter', 'Bluzka', 'Cienki sweter', 'Jeansy', 'Koszula']

# Cleaned data storage
cleaned_data = []

for i, x in enumerate(data):
    product_info = x.text.strip()
    
    # Check for clothing keywords in product_info
    clothing_type = next((keyword for keyword in clothing_keywords if keyword in product_info), 'Other')
    
    cleaned_data.append((i+1, clothing_type))

# Write cleaned data to a CSV file
csv_filename = 'cleaned_clothing_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    csv_writer.writerow(['Index', 'Product Info'])
    
    # Write data
    csv_writer.writerows(cleaned_data)

print(f"Cleaned data has been saved to {csv_filename}")