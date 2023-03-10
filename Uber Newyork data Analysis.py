#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

uber_15=pd.read_csv(r'C:\Users\akank\OneDrive\Desktop\Python usecase\uber-raw-data-janjune-15.csv')

uber_15.head(2)

uber_15.shape
#data preperation

uber_15.duplicated().sum()

uber_15.drop_duplicates(inplace=True)

uber_15.shape

uber_15.dtypes
#Analysing which month havs maximum pickup

uber_15['Pickup_date']=pd.to_datetime(uber_15['Pickup_date'], format = "%Y-%m-%d %H:%M:%S")

uber_15['Pickup_date'].dtype

uber_15['Pickup_date']

uber_15['month'] =uber_15['Pickup_date'].dt.month

uber_15['month'].value_counts().plot(kind='bar')

uber_15['weekday'] =uber_15['Pickup_date'].dt.day_name()
uber_15['Day'] =uber_15['Pickup_date'].dt.day
uber_15['hour'] =uber_15['Pickup_date'].dt.hour
uber_15['month'] =uber_15['Pickup_date'].dt.month
uber_15['minute'] =uber_15['Pickup_date'].dt.minute

uber_15.head(2)


# In[22]:


#Indepth analysis of uber trips


# In[2]:


uber_15['weekday'] =uber_15['Pickup_date'].dt.day_name()
uber_15['Day'] =uber_15['Pickup_date'].dt.day
uber_15['hour'] =uber_15['Pickup_date'].dt.hour
uber_15['month'] =uber_15['Pickup_date'].dt.month
uber_15['minute'] =uber_15['Pickup_date'].dt.minute


# In[3]:


uber_15.head(2)


# In[4]:


uber_15.groupby(['month','weekday']).size()


# In[6]:


temp=uber_15.groupby(['month','weekday'], as_index=False).size()


# In[7]:


temp.head()


# In[8]:


temp['month'].unique()


# In[9]:


dict_month={1:'Jan',2:'Feb',3:'March',4:'April',5:'May',6:'June'}


# In[10]:


temp['month']=temp['month'].map(dict_month)


# In[11]:


temp['month']


# In[13]:


temp


# In[21]:


plt.figure(figsize=(15,8))
sns.barplot(x='month',y='size',hue='weekday',data=temp)


# In[ ]:


#Analysisng hourly demand of uber in newyork city


# In[23]:


uber_15.groupby(['weekday','hour']).count()


# In[24]:


uber_15.groupby(['weekday','hour']).size()


# In[27]:


summary=uber_15.groupby(['weekday','hour'],as_index=False).size()


# In[28]:


summary


# In[30]:


plt.figure(figsize=(15,8))
sns.pointplot(x='hour',y='size',hue='weekday',data=summary)


# In[ ]:


#Most active vehicles on uber base-number


# In[33]:


uber_foil=pd.read_csv(r"C:\Users\akank\OneDrive\Desktop\Python usecase\Uber-Jan-Feb-FOIL.csv")


# In[34]:


uber_foil.head(5)


# In[37]:


get_ipython().system('pip install chart_studio')
get_ipython().system('pip install plotly')


# In[39]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs, plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)


# In[42]:


px.box(x='dispatching_base_number',y='active_vehicles', data_frame=uber_foil)


# In[43]:


px.violin(x='dispatching_base_number',y='active_vehicles', data_frame=uber_foil)


# In[ ]:


#Getting ready for complete analysis
#extracting/collecting desired dataset from list folder


# In[58]:


import os


# In[59]:


files=os.listdir(r'C:\Users\akank\OneDrive\Desktop\Uber_dataset')[-7:]


# In[60]:


files


# In[61]:


files.remove('uber-raw-data-janjune-15.csv')


# In[62]:


files


# In[63]:


path=r'C:\Users\akank\OneDrive\Desktop\Uber_dataset'

final = pd.DataFrame()

for file in files:
    current_df=pd.read_csv(path+'/'+file,encoding='utf-8')
    final=pd.concat([current_df,final])


# In[64]:


final.shape


# In[65]:


final.head(2)


# In[66]:


final.duplicated().sum()


# In[68]:


final.drop_duplicates(inplace=True)


# In[69]:


final.shape


# In[ ]:


#Spatial Analysis to find rush uber pickups


# In[70]:


rush_uber=final.groupby(['Lat','Lon'], as_index=False).size()


# In[71]:


rush_uber


# In[73]:


get_ipython().system('pip install folium')


# In[74]:


import folium


# In[78]:


basemap=folium.Map()


# In[79]:


from folium.plugins import HeatMap


# In[81]:


HeatMap(rush_uber).add_to(basemap)


# In[82]:


basemap


# In[ ]:


#pairwise analysis


# In[83]:


final.head(2)


# In[87]:


final['Date/Time']=pd.to_datetime(final['Date/Time'],format='%m/%d/%Y %H:%M:%S')


# In[88]:


final['weekday']=final['Date/Time'].dt.day
final['hour']=final['Date/Time'].dt.hour


# In[89]:


final.head(3)


# In[91]:


pivot=final.groupby(['weekday','hour']).size().unstack()


# In[92]:


pivot


# In[93]:


pivot.style.background_gradient()


# In[ ]:


#Automation 


# In[95]:


def gen_pivot_table(df,col1,col2):
    pivot=df.groupby([col1,col2]).size().unstack()
    return pivot.style.background_gradient()


# In[96]:


gen_pivot_table(final,'weekday','hour')


# In[ ]:




