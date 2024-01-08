import requests
from bs4 import BeautifulSoup
import csv
from src.utilities import scrape_url_and_write_csv, merge_csv_files

def main():
    OUTPUT_DIRECTORY = "output"
    for i in range(10):
        output_path = OUTPUT_DIRECTORY + f"\{i}.csv"
        url = create_url(i) 
        scrape_url_and_write_csv(output_path,url)

def create_url(number):
    return f"https://moodo.pl/pol_m_KOLEKCJA-192.html?counter={number}"
    
if __name__ == "__main__":
    input_folder_name = "output"
    output_folder_name = "single_csv_output"
    output_file_name = "merged_data.csv"
    main()
    merge_csv_files(input_folder_name, output_folder_name, output_file_name)