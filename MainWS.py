import requests
from bs4 import BeautifulSoup
import csv
from src.utilities import scrape_url_and_write_csv, merge_csv_files

def main():
    OUTPUT_DIRECTORY = "output"
    OUTPUT_FOLDER_NAME = "single_csv_output"
    OUTPUT_FILE_NAME = "merged_data.csv"
    for i in range(10):
        output_path = OUTPUT_DIRECTORY + f"\{i}.csv"
        url = create_url(i) 
        scrape_url_and_write_csv(output_path,url)
    merge_csv_files(OUTPUT_DIRECTORY, OUTPUT_FOLDER_NAME, OUTPUT_FILE_NAME)

def create_url(number):
    return f"https://moodo.pl/pol_m_KOLEKCJA-192.html?counter={number}"
    
if __name__ == "__main__":
    main()
