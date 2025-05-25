import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

st.title("📊 Real-Time Job Trend Analyzer")

df = pd.read_csv('jobs.csv')

keyword = st.text_input("Search by Keyword (optional)", "")

if keyword:
    df = df[df['title'].str.contains(keyword, case=False, na=False)]

st.subheader("Top 5 Job Titles")
st.bar_chart(df['title'].value_counts().head())

st.subheader("Top Cities")
st.bar_chart(df['location'].value_counts().head())

st.subheader("Top Skills (if available)")
skills = []
for s in df['skills'].dropna():
    skills.extend(s.lower().split(', '))
skill_counts = Counter(skills)
skill_df = pd.DataFrame(skill_counts.items(), columns=['Skill', 'Count']).sort_values(by='Count', ascending=False)
st.dataframe(skill_df.head())

if 'date_posted' in df.columns:
    st.subheader("Job Posting Trends (if available)")
    st.bar_chart(df['date_posted'].value_counts())

st.success(f"Total Listings: {len(df)}")
