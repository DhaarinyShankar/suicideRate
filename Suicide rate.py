#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('suicide_data.csv')
df.head(5)


# In[3]:


df[['sex','age','population']].head(5)


# In[4]:


#lets start with data cleaning process
# age has years appended to it. Lets trim years from age using regex pattern


df['age_group']=df['age'].str.replace(r'\s*years', '', regex=True)
df['age_group']


# In[5]:


# splittling country-year to only country

df['country']=df['country-year'].str[0:-4]
df['country'].unique()


# In[6]:


#the data is cleaned. Lets start visualizing by plotting graphs
# Lets see the count of age group 
ax=df['age_group'].value_counts()
a=ax.plot(kind='bar')
x=a.set_xlabel('Age Group')
y=a.set_ylabel('Count')
a.bar_label(a.containers[0],label_type='edge')


# In[7]:


# seems the count of age group are almost same count


# In[8]:


df.describe()


# In[9]:


# Rename column
df=df.rename(columns={'sex':'Gender','suicides_no':'suicides_count'})
df


# In[10]:


# lets plot male and female count of suicide rate
df.Gender.unique()


# In[11]:


# ax=df.Gender.value_counts()
ax = df.groupby('Gender')['suicides_count'].sum().reset_index()
ax
pt=ax.plot(kind='bar',color='yellow')
a=pt.set_xlabel('Gender')
b=pt.set_ylabel('Count')


# In[69]:


gen_count=df['generation'].value_counts()
suicide_gen = df.groupby(['generation']).suicides_count.sum()
ax=suicide_gen.plot(kind='bar',color='brown')


# In[13]:


# plotting the suicide count over the span of years
grouped_df = df.groupby('year')['suicides_count'].sum().reset_index()
x=grouped_df['year']
y=grouped_df['suicides_count']
a=plt.plot(x,y)


# In[14]:


df['country'].value_counts()


# In[15]:


df.isnull().any()


# In[16]:


df['HDI for year'].isnull().sum()


# In[17]:


# 19456 records are null for HDI for Year column. Dropping this column.
df.drop(columns=['HDI for year'])


# In[18]:


year_count=df.groupby(['country'])['suicides_count'].sum()
year_count


# In[19]:


plt.figure(figsize=[15,4])
year_count=df.groupby(['country'])['suicides_count'].sum()
sorted=year_count.sort_values().head(10)
bar=sorted.plot(kind="bar",color="brown")
plt.xlabel('Country')
plt.ylabel('Total Suicides Count')
plt.title('Total Suicides Count by Country')
plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


# In[20]:


year_count_plot = year_count.sort_values(ascending=False)  # Sort by count (descending)

# Create the bar plot
plt.figure(figsize=(35, 20))  # Set the figure size
plt.barh(year_count_plot.index, year_count_plot.values)  # Horizontal bar chart
plt.xlabel('Suicides Count')
plt.ylabel('Country')
plt.title('Total Suicides Count by Country (Descending)')
plt.gca().invert_yaxis()  # Invert y-axis to display the highest count at the top

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[25]:


sns.countplot(x='generation',hue='Gender', data=df)
plt.xticks(rotation=45)
plt.show()


# In[45]:


df=df.rename(columns={'gdp_per_capita ($)':'Gdp Capital'})


# In[57]:


sns.set(style='whitegrid')
sns.boxplot(df.year)
plt.xlabel('Year')
plt.show()


# In[56]:


sns.set(style='whitegrid')
sns.boxplot(df['Gdp Capital'])
plt.xlabel('Gdp Capital')
plt.show()


# In[61]:


max(df.suicides_count)
df[df.suicides_count==max((df.suicides_count))]


# In[63]:


min(df.suicides_count)
df[df.suicides_count==min((df.suicides_count))]


# In[66]:


sns.heatmap(df.corr(),annot=True)
plt.show()


# In[ ]:


# population and suicides count are highly correlated to each other

