#!/usr/bin/env python
# coding: utf-8

# he outbreak of Covid-19 resulted in a lot of restrictions which resulted in so many impacts on the global economy. Almost all the countries were impacted negatively by the rise in the cases of Covid-19. If you want to learn how to analyze the impacts of Covid-19 on the economy

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[10]:


data =pd.read_csv(r"C:\Users\User\Downloads\archive (6)\transformed_data.csv")
data1=pd.read_csv(r"C:\Users\User\Downloads\archive (6)\raw_data.csv")


# # Data Preparation
# The dataset that we are using here contains two data files. One file contains raw data, and the other file contains transformed one. But we have to use both datasets for this task, as both of them contain equally important information in different columns. So let’s have a look at both the datasets one by one

# In[12]:


print(data.head())


# In[13]:


print(data1.head())


# After having initial impressions of both datasets, I found that we have to combine both datasets by creating a new dataset. But before we create a new dataset, let’s have a look at how many samples of each country are present in the dataset:

# In[16]:


data['COUNTRY'].value_counts()


# In[17]:


data['COUNTRY'].value_counts().mode()


# So 294 is the mode value. We will need to use it for dividing the sum of all the samples related to the human development index, GDP per capita, and the population. Now let’s create a new dataset by combining the necessary columns from both the datasets:

# In[28]:


# Aggregating the data
code =data["CODE"].unique().tolist()
country=data["COUNTRY"].unique().tolist()
#print(code)
hdi =[]
tc =[]
td =[]
sti= []
population = data["POP"].unique().tolist()
gdp =[]
for i in country:
    hdi.append((data.loc[data["COUNTRY"]== i,"HDI"]).sum()/294)
    tc.append((data1.loc[data1["location"]== i,"total_cases"]).sum())
    td.append((data1.loc[data1["location"]== i,"total_deaths"]).sum())
    sti.append((data.loc[data["COUNTRY"]== i,"STI"]).sum()/294)
    population.append((data1.loc[data1["location"]==i,"population"]).sum()/294)
aggregated_data =pd.DataFrame(list(zip(code,country,hdi,tc,td,sti,population)),columns =["Country Code",'Country','HDI','Total Cases',
                                                                                        "Total Deaths",'Stringency Index',"population"])
print(aggregated_data.head())


#  have not included the GDP per capita column yet. I didn’t find the correct figures for GDP per capita in the dataset. So it will be better to manually collect the data about the GDP per capita of the countries.
# 
# As we have so many countries in this data, it will not be easy to manually collect the data about the GDP per capita of all the countries. So let’s select a subsample from this dataset. To create a subsample from this dataset, I will be selecting the top 10 countries with the highest number of covid-19 cases. It will be a perfect sample to study the economic impacts of covid-19. So let’s sort the data according to the total cases of Covid-19:

# In[39]:


data =aggregated_data.sort_values(by =["Total Cases"],ascending=False)
print(data.head())


# In[40]:


#Now here’s how we can select the top 10 countries with the highest number of cases:

data =data.head(10)
print(data)


# In[41]:


#Now I will add two more columns (GDP per capita before Covid-19, GDP per capita during Covid-19) to this datase
data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75, 
                            11497.65, 7027.61, 9946.03, 
                            29564.74, 6001.40, 6424.98, 42354.41]

data["GDP During Covid"] = [63543.58, 6796.84, 1900.71, 
                            10126.72, 6126.87, 8346.70, 
                            27057.16, 5090.72, 5332.77, 40284.64]
print(data)


# In[43]:


# will first have a look at all the countries with the highest number of covid-19 cases
fig =px.bar(data,x="Country",y="Total Cases",title ="Total Case IN country")
fig.show()


# In[44]:


# Now let’s have a look at the total number of deaths among the countries with the highest number of covid-19 cases
fig =px.bar(data,x="Country",y="Total Deaths",title ="Total Deaths IN country")
fig.show()


# In[49]:


fig =go.Figure()
fig.add_trace(go.Bar(x=data["Country"],y=["Total Cases"],name ="Total Case ",marker_color ="green"))
fig.add_trace(go.Bar(x=data["Country"],y=data["Total Deaths"],name ="Total Deaths ",marker_color ="red")) 
fig.update_layout(barmode ="group")
fig.show()


# In[54]:


#Now let’s have a look at the percentage of total deaths and total cases among all the countries 
#with the highest number of covid-19 cases
cases =data["Total Cases"].sum()
decased=data["Total Deaths"].sum()
labels =["Total Cases","Total Deaths"]
values =[cases,decased]
fig =px.pie(data,values =values,names =labels,hole = 0.5)
fig.show()


# # Analyzing Covid-19 Impacts on Economy
# Now let’s move to analyze the impacts of covid-19 on the economy. Here the GDP per capita is the primary factor for analyzing the economic slowdowns caused due to the outbreak of covid-19. Let’s have a look at the GDP per capita before the outbreak of covid-19 among the countries with the highest number of covid-19 cases:

# In[56]:


death_rate =(data["Total Deaths"].sum()/data['Total Cases'].sum())*100
print("Death Rate",death_rate)


# In[57]:


fig =px.bar(data,x="Country",y='Total Cases',hover_data =['population',"Total Deaths"],color ='Stringency Index',
            height =400,title="Stringency index during covid")
fig.show()


# In[58]:


fig =px.bar(data,x="Country",y='Total Cases',hover_data =['population',"Total Deaths"],color ='GDP Before Covid',
            height =400,title="GDP  per capital Before Covid ")
fig.show()


# In[60]:


fig =px.bar(data,x="Country",y="Total Deaths",title ="Total Deaths IN country")
fig.show()


# In[59]:


fig =px.bar(data,x="Country",y='Total Cases',hover_data =['population',"Total Deaths"],color ='GDP During Covid',
            height =400,title="GDP  per capital during Covid ")
fig.show()


# In[64]:


fig =go.Figure()
fig.add_trace(go.Bar(x=data["Country"],y=["GDP Before Covid"],name ="GDP  per capital Before Covid  ",marker_color ="indianred"))
fig.add_trace(go.Bar(x=data["Country"],y=data["GDP During Covid"],name ="GDP per During Covid ",marker_color ="lightsalmon")) 
fig.update_layout(barmode ="group",xaxis_tickangle =-45)
fig.show()


# In[65]:


fig =px.bar(data,x="Country",y='Total Cases',hover_data =['population',"Total Deaths"],color ='HDI',
            height =400,title="HDI during Covid ")
fig.show()


# In[ ]:





# In[ ]:




