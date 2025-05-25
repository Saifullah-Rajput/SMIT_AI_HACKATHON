
import requests
import pandas
import matplotlib
import plotly
import streamlit
import selenium 

from bs4 import BeautifulSoup



def scrape_indeed_jobs(keyword, location=''):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # Indeed search URL (example for US)
    url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    job_cards = soup.find_all('div', class_='jobsearch-SerpJobCard')
    
    jobs = []
    
    for card in job_cards:
        title = card.find('a', {'data-tn-element': 'jobTitle'})
        title_text = title.text.strip() if title else 'N/A'
        
        company = card.find('span', class_='company')
        company_text = company.text.strip() if company else 'N/A'
        
        location_tag = card.find('div', class_='recJobLoc')
        location_text = location_tag['data-rc-loc'] if location_tag else 'N/A'
        
        summary = card.find('div', class_='summary')
        skills_text = summary.text.strip() if summary else 'N/A'
        
        date = card.find('span', class_='date')
        date_text = date.text.strip() if date else 'N/A'
        
        job_data = {
            'title': title_text,
            'company': company_text,
            'location': location_text,
            'skills': skills_text,
            'date_posted': date_text
        }
        
        jobs.append(job_data)
    
    return jobs


if __name__ == "__main__":
    keyword = "python developer"
    location = "New York"
    job_listings = scrape_indeed_jobs(keyword, location)
    
    for i, job in enumerate(job_listings, 1):
        print(f"Job {i}:")
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Skills/Description: {job['skills']}")
        print(f"Date Posted: {job['date_posted']}")
        print('-' * 40)

        import csv

# Saving Scrapped file to csv 
with open('indeed_jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'company', 'location', 'skills', 'date_posted']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for job in job_listings:
        writer.writerow(job)

print("Data saved to indeed_jobs.csv")

