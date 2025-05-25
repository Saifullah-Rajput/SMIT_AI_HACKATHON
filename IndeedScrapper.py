import requests
from bs4 import BeautifulSoup
import pandas as pd
from .utils import polite_delay

def scrape_indeed(keyword="Data Analyst", num_pages=5):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    all_jobs = []
    for page in range(0, num_pages):
        url = f"https://www.indeed.com/jobs?q={keyword}&start={page*10}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('div', class_='cardOutline')
        for job in jobs:
            title = job.find('h2').text.strip() if job.find('h2') else "N/A"
            company = job.find('span', class_='companyName')
            company = company.text.strip() if company else "N/A"
            location = job.find('div', class_='companyLocation')
            location = location.text.strip() if location else "N/A"
            date = job.find('span', class_='date')
            date = date.text.strip() if date else "N/A"
            all_jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Skills": "N/A",
                "Date Posted": date,
                "Source": "Indeed"
            })
        polite_delay()
    return pd.DataFrame(all_jobs)
