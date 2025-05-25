import pandas as pd
from indeed_scraper import scrape_indeed
from glassdoor_scraper import scrape_glassdoor

def collect_all_data(keyword="Data Analyst"):
    df_indeed = scrape_indeed(keyword)
    df_glassdoor = scrape_glassdoor(keyword)
    combined = pd.concat([df_indeed, df_glassdoor], ignore_index=True)
    combined.to_csv("data/jobs.csv", index=False)
    print("Data saved to data/jobs.csv")
