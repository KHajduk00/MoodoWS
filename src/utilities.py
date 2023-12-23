import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

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
    'Sukienka', 'Sweter', 'Bluzka', 'Cienki sweter', 'Jeansy', 'Koszula']

    # Cleaned data storage
    cleaned_data = []

    for i, x in enumerate(data):
        product_info = x.text.strip()
        
        # Check for clothing keywords in product_info
        clothing_type = next((keyword for keyword in clothing_keywords if keyword in product_info), 'Other')

        product_id = x.get('data-product_id', 'N/A')
        
        cleaned_data.append((i+1, clothing_type, today_date, product_id))

    write_csv(output_path, cleaned_data)


def write_csv(output_path, cleaned_data):
    # Write cleaned data to a CSV file
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(['Index', 'Product Type', 'Date of scrap', 'Product ID'])
        
        # Write data
        csv_writer.writerows(cleaned_data)

    print(f"Cleaned data has been saved to {output_path}")