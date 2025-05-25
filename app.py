import streamlit as st
import pandas as pd
import plotly.express as px
# from scraper.indeed_scraper import scrape_indeed
# from scraper.glassdoor_scraper import scrape_glassdoor

st.set_page_config(page_title="Real-Time Job Trend Analyzer", layout="wide")

st.title("📊 Real-Time Job Trend Analyzer")

# Keyword input
keyword = st.text_input("Enter job keyword (e.g., Data Analyst, Web Developer)", "Data Analyst")
if st.button("Fetch Latest Data"):
    with st.spinner("Scraping data..."):
        df_indeed = scrape_indeed(keyword)
        df_glassdoor = scrape_glassdoor(keyword)
        df = pd.concat([df_indeed, df_glassdoor], ignore_index=True)
        df.to_csv("data/jobs.csv", index=False)
        st.success("Data updated!")

# Load data
try:
    df = pd.read_csv("data/jobs.csv")
except:
    st.warning("No data found. Click 'Fetch Latest Data'.")

if not df.empty:
    st.subheader("Top 5 Most In-Demand Job Titles")
    top_titles = df['Title'].value_counts().head(5).reset_index()
    fig = px.bar(top_titles, x='index', y='Title', labels={'index': 'Job Title', 'Title': 'Count'})
    st.plotly_chart(fig)

    st.subheader("Most Frequent Skills")
    # Skills are placeholder - you can enhance later
    st.info("Skills scraping is basic in this version.")

    st.subheader("Cities with Highest Job Openings")
    top_cities = df['Location'].value_counts().head(5).reset_index()
    fig2 = px.pie(top_cities, names='index', values='Location')
    st.plotly_chart(fig2)

    st.subheader("Job Postings Over Time (If Available)")
    if 'Date Posted' in df.columns:
        st.write(df['Date Posted'].value_counts())

    st.dataframe(df)



