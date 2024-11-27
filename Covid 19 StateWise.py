#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


import numpy as np # linear algebra
import pandas as pd 


# In[2]:


import os


# In[3]:


os


# In[4]:


main_df=pd.read_csv(r"C:\Users\ganes\Latest Covid-19 India Status.csv")


# In[5]:


main_df


# In[6]:


main_df.head(500)


# In[7]:


main_df.info()


# In[8]:


main_df.describe()


# In[9]:


main_df.columns


# In[10]:


main_df.head()


# In[15]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


sns.heatmap(main_df.isnull())


# In[19]:


main_df.corr()


# In[21]:


sns.heatmap(main_df.corr(), annot=True)


# In[22]:


plt.figure(figsize=(8, 10))
sns.barplot(data = main_df, y="State/UTs", x="Total Cases")


# In[23]:


px.bar(main_df, x="State/UTs", y="Total Cases", color="Death Ratio (%)", title="Total Cases as per each State : ")


# In[24]:


px.scatter(main_df, x='Active Ratio (%)',y='Death Ratio (%)', color=main_df['State/UTs'])


# In[26]:


fig = px.choropleth(
    main_df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State/UTs',
    color='Total Cases',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# In[27]:


fig = px.choropleth(
    main_df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State/UTs',
    color='Deaths',
    color_continuous_scale='Blues'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# In[28]:


sns.pairplot(main_df)


# In[29]:


px.density_heatmap(main_df, y="Total Cases", x="State/UTs", nbinsx=20, nbinsy=20)


# In[30]:


px.density_heatmap(main_df, y="Total Cases", x="State/UTs", marginal_x="histogram", marginal_y="histogram")


# In[31]:


sns.relplot(x = 'Total Cases', y ='Discharged', hue = 'State/UTs', data = main_df)


# In[32]:


fig = px.scatter_matrix(main_df, dimensions=["Total Cases", "Active", "Discharged", "Deaths"], color=main_df['State/UTs'])
fig.show()


# In[33]:


fig = px.scatter(main_df, x="Total Cases", y="Active", size="Deaths", color=main_df['State/UTs'], log_x=True, size_max=50)
fig.show()


# In[34]:


px.scatter(main_df, x="Total Cases", y="Active",size="Active Ratio (%)", color="Active Ratio (%)",hover_name="State/UTs", log_x=True, size_max=60)


# In[36]:


fig = px.pie(main_df, values='Total Cases', names=main_df['State/UTs'], title='Covid cases (%) in all states of India')
fig.show()


# In[37]:


main_df.nunique()


# In[39]:


fig = px.pie(main_df, values='Discharge Ratio (%)', names=main_df['State/UTs'], title='Covid cases (%) in all states of India')
fig.show()


# In[40]:


fig = px.pie(main_df, values='Death Ratio (%)', names=main_df['State/UTs'], title='Covid cases (%) in all states of India')
fig.show()


# In[41]:


fig = px.scatter (main_df, x = "Active", y = "Deaths", template = "plotly_dark",  trendline="ols")
fig.show ()


# In[42]:


highest_cases = main_df[main_df['Total Cases'] == max(main_df['Total Cases'])]
highest_cases


# In[44]:


# State having Lowest number of covid cases in India.

lowest_cases = main_df[main_df['Total Cases'] == min(main_df['Total Cases'])]
lowest_cases


# In[45]:


# State having highest number of Active cases in India.

highest_active = main_df[main_df['Active'] == max(main_df['Active'])]
highest_active


# In[46]:


# State having Lowest number of Active cases in India.

lowest_active = main_df[main_df['Active'] == min(main_df['Active'])]
lowest_active


# In[53]:


highest_death_ratio = main_df[main_df['Death Ratio (%)'] == max(main_df['Death Ratio (%)'])]
highest_death_ratio


# In[54]:


# State having lowest number of death ratio in India.

lowest_death_ratio = main_df[main_df['Death Ratio (%)'] == min(main_df['Death Ratio (%)'])]
lowest_death_ratio


# In[55]:


highest_discharge_ratio = main_df[main_df['Discharge Ratio (%)'] == max(main_df['Discharge Ratio (%)'])]
highest_discharge_ratio


# In[56]:


# State having lowest discharge ratio in India.

lowest_discharge_ratio = main_df[main_df['Discharge Ratio (%)'] == min(main_df['Discharge Ratio (%)'])]
lowest_discharge_ratio


# In[58]:


# Visualization of top 5 state having highest Death ratio in India.
df1 = main_df.sort_values(by='Death Ratio (%)', ascending=False).head()
states = df1['State/UTs']
ratio = df1['Death Ratio (%)']
plt.barh(states, ratio)
plt.xlabel('Death Ratio (%)')
plt.ylabel('State')
plt.title('State with  more death ratio in India')
plt.show()


# In[ ]:




