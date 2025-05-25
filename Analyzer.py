import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def analyze():
    df = pd.read_csv('jobs.csv')

    # Top 5 Job Titles
    print("\nTop 5 Job Titles:")
    print(df['title'].value_counts().head())

    # Top Cities
    print("\nTop Cities:")
    print(df['location'].value_counts().head())

    # Top Skills (if available)
    skills = []
    for s in df['skills'].dropna():
        skills.extend(s.lower().split(', '))
    print("\nTop Skills:")
    print(Counter(skills).most_common(5))

    # Date Trends
    if 'date_posted' in df.columns:
        print("\nDate Trends:")
        print(df['date_posted'].value_counts())

if __name__ == "__main__":
    analyze()
