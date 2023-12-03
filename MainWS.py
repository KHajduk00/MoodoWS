import requests
from bs4 import BeautifulSoup
import csv


def main():
    OUTPUT_DIRECTORY = "output"
    for i in range(10):
        output_path = OUTPUT_DIRECTORY + f"\{i}.csv"
        scrape_url(i,output_path)

def create_url(number):
    return f"https://moodo.pl/pol_m_KOLEKCJA-192.html?counter={number}"
    

def scrape_url(number,output_path):
    response = requests.get(create_url(number))
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
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(['Index', 'Product Type'])
        
        # Write data
        csv_writer.writerows(cleaned_data)

    print(f"Cleaned data has been saved to {output_path}")

if __name__ == "__main__":
    main()


### this is the same!!!!!
#keyword for keyword in clothing_keywords if keyword in product_info

#for keyword in clothing_keywords:
#    if keyword in product_info
#    return keyword
###