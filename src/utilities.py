import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
import os

def scrape_url_and_write_csv(output_path,url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find('div', class_="product__sizes mb-1"))
    data = soup.select('div[class="product col-6 col-sm-4 col-md-3 pt-3 pb-md-3 px-1 px-sm-3 px-md-4"]')
    #print(data)

    #Get time of scraping
    today_date = datetime.now().strftime('%Y-%m-%d')

    for i, x in enumerate(data):
        print(f"Element {i+1}: {x.text}")

    print(f"Total number of elements: {len(data)}")

    # Define keywords for types of clothing
    clothing_keywords = ['Spódnica', 'Koszulka', 'Spodnie',
    'Sukienka', 'Sweter', 'Bluzka', 'Cienki sweter', 'Jeansy',
    'Koszula', 'Bluza', 'Garnitur','Kamizaelka','Koszula','Kurtka',
    'Płaszcz','Legginsy','Marynarka','Komplet','Biżuteria','Czapka','Gumka do włosów',
    'Opaska do włosów','Pasek','Portfel','Rękawiczki','Skarpetki','Szalik','Torba','Strój kąpielowy',
    'Szorty','Buty','Klapki','Kapelusz','Okulary']

    # Cleaned data storage
    cleaned_data = []

    for i, x in enumerate(data):
        product_info = x.text.strip()
        
        # Check for clothing keywords in product_info
        clothing_type = next((keyword for keyword in clothing_keywords if keyword in product_info), 'Other')

        # Scrape ID of each product
        product_id = x.get('data-product_id', 'N/A')
        
        # Scrape Price for each product
        product_price_element = x.find('strong', {'class': 'price'})
        price = product_price_element.text.strip() if product_price_element else 'N/A'
        product_price = float(price.replace(" ", "").replace("zł", "").replace(",","."))
        
        # Scrape Link to product page
        product_link = x.find('a')['href']
        full_link = f"https://moodo.pl{product_link}"

        cleaned_data.append((i+1, clothing_type, today_date, product_id, product_price, full_link))

    write_csv(output_path, cleaned_data)


def write_csv(output_path, cleaned_data):
    # Write cleaned data to a CSV file
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(['Index', 'Product Type', 'Date of scrap', 'Product ID', 'Product Price', 'Product Link'])
        
        # Write data
        csv_writer.writerows(cleaned_data)

    print(f"Cleaned data has been saved to {output_path}")

def merge_csv_files(input_folder, output_folder, output_file_name):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # Loop through all CSV files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            # Read each CSV file and append its data to the merged_data DataFrame
            file_path = os.path.join(input_folder, file_name)
            data = pd.read_csv(file_path)
            merged_data = merged_data._append(data, ignore_index=True)

    # Path to the output file
    output_file_path = os.path.join(output_folder, output_file_name)

    # If the output file already exists, append the data; otherwise, create a new file
    if os.path.exists(output_file_path):
        merged_data.to_csv(output_file_path, mode='a', header=False, index=False)
    else:
        merged_data.to_csv(output_file_path, index=False)