import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st

# Load Dataset
main_df = pd.read_csv(r"C:/Users/ganes/Latest Covid-19 India Status.csv")

# Dashboard Title
st.title("COVID-19 Dashboard for India")
st.write("Interactive Dashboard to analyze the COVID-19 cases in India.")

# Dataset Overview
st.header("Dataset Overview")
st.write(main_df)

# Heatmap for Missing Data
st.header("Missing Data Heatmap")
sns.heatmap(main_df.isnull(), cbar=False)
st.pyplot(plt)

# Correlation Heatmap
st.header("Correlation Heatmap")
sns.heatmap(main_df.corr(), annot=True, cmap="coolwarm")
st.pyplot(plt)

# Bar Chart: Total Cases by State
st.header("Total Cases by State")
fig1 = px.bar(main_df, x="State/UTs", y="Total Cases", color="Death Ratio (%)", title="Total Cases as per Each State")
st.plotly_chart(fig1)

# Scatter Plot: Active vs Death Ratio
st.header("Scatter Plot: Active Ratio vs Death Ratio")
fig2 = px.scatter(main_df, x="Active Ratio (%)", y="Death Ratio (%)", color="State/UTs", title="Active vs Death Ratio")
st.plotly_chart(fig2)

# Choropleth Map for Total Cases
st.header("Choropleth Map for Total Cases")
fig3 = px.choropleth(
    main_df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State/UTs',
    color='Total Cases',
    color_continuous_scale='Reds',
    title="COVID-19 Total Cases in India"
)
fig3.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig3)

# Pie Chart: Cases Distribution
st.header("Distribution of Cases")
fig4 = px.pie(main_df, values='Total Cases', names='State/UTs', title="Percentage of Total Cases by State")
st.plotly_chart(fig4)

# Top 5 States by Death Ratio
st.header("Top 5 States by Death Ratio")
df1 = main_df.sort_values(by='Death Ratio (%)', ascending=False).head()
st.write(df1)

# Bar Chart: Top 5 States by Death Ratio
states = df1['State/UTs']
ratio = df1['Death Ratio (%)']
plt.figure(figsize=(8, 6))
plt.barh(states, ratio, color='red')
plt.xlabel('Death Ratio (%)')
plt.ylabel('State')
plt.title('Top 5 States with Highest Death Ratio in India')
st.pyplot(plt)

# State with Highest and Lowest Total Cases
highest_cases = main_df[main_df['Total Cases'] == max(main_df['Total Cases'])]
lowest_cases = main_df[main_df['Total Cases'] == min(main_df['Total Cases'])]
st.write("State with the Highest Total Cases:")
st.write(highest_cases)
st.write("State with the Lowest Total Cases:")
st.write(lowest_cases)
