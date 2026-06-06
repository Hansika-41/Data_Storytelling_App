import streamlit as st
import pandas as pd
import plotly.express as px


st.title("The Story of Netflix: Evolution of Content")
st.markdown("### Introduction")
st.write("Netflix started as a DVD rental service, but today it is a global streaming giant. Let's look at how its content changed over time to understand its strategy.")


df = pd.read_csv("netflix_titles.csv")
df = df.fillna("Unknown")

st.markdown("### 1. What dominates Netflix: Movies or TV Shows?")
st.write("When we look at the entire catalog, we want to know what type of content Netflix focuses on the most.")

type_counts = df["type"].value_counts().reset_index()
fig1 = px.pie(type_counts, names="type", values="count")
st.plotly_chart(fig1)

st.write("**Finding:** As we can see in the pie chart, Netflix actually has significantly more Movies than TV Shows in its total history.")

st.markdown("### 2. The Shift Over Time")
st.write("Even though movies lead overall, let's analyze the release years to see if their strategy has changed in recent times.")

year_counts = df.groupby(["release_year", "type"]).size().reset_index(name="count")

year_counts = year_counts[year_counts["release_year"] >= 2000]

fig2 = px.line(year_counts, x="release_year", y="count", color="type")
st.plotly_chart(fig2)

st.write("**Finding:** Notice the massive spike in content leading up to recent years. However, TV Shows have grown at a much faster rate in the last decade compared to their historical numbers due to the global popularity of binge-watching.")

st.markdown("### 3. Final Conclusion & Recommendations")
st.write("- **Invest in TV Series:** Netflix should continue putting budget into multi-season TV Shows because they keep users subscribed longer.")
st.write("- **Target Global Markets:** Since content creation is expanding globally, focusing heavily on regional stories will drive the next wave of subscriber growth.")