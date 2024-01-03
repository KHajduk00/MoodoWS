import requests
from bs4 import BeautifulSoup
import csv
from src.utilities import scrape_url_and_write_csv

def main():
    OUTPUT_DIRECTORY = "output"
    for i in range(10):
        output_path = OUTPUT_DIRECTORY + f"\{i}.csv"
        url = create_url(i) 
        scrape_url_and_write_csv(output_path,url)

def create_url(number):
    return f"https://moodo.pl/pol_m_KOLEKCJA-192.html?counter={number}"
    

if __name__ == "__main__":
    main()
    