import requests
from bs4 import BeautifulSoup
import gspread
import time

job_list = []
phone_numbers_seen = set()  # Set to store unique phone numbers

def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    listings = soup.find_all('div', class_='listing')
    
    for info in listings:
        job_dict = {}
        job_dict['name'] = info.find('a', class_='listing__link').text.strip()
        address = info.find('li', class_='mlr__item--phone').text.strip()
        
        # Extract only the phone number
        phone_number = address.split('\n')[-1].strip()  # Split by newline and take the last element
        job_dict['address'] = phone_number
        
        # Check if the phone number is already seen, if not add to list and set
        if phone_number not in phone_numbers_seen:
            phone_numbers_seen.add(phone_number)
            job_list.append(job_dict)
    
    return job_list

# Ask user for city and job title
city = input("Enter the city you want to search in: ")
job_title = input("Enter the job title you are looking for: ")


def update_sheet(jobs):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("ScrapeToSheets").sheet1

    for job in jobs:
        sh.append_row([job['name'], job['address']])
    print("Update successful!")

# Scrape and update the sheet
for i in range(1, 6):
    url = f"https://www.yellowpages.ca/search/si/{i}/{job_title}/{city}+ON"
    jobs = scrape(url)

    # Update the sheet after scraping each page
    update_sheet(job_list)
    
    # Wait for 60 seconds before making the next call
    time.sleep(60)
