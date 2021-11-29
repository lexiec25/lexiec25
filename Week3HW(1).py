#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as py
import matplotlib.pyplot as plt

fitness_df = pd.read_csv("Fitness_trackers.csv")
fitness_df


# In[4]:


fitness_df.dropna
df2 = fitness_df.loc[fitness_df["Device Type"].str.contains("FitnessBand")]
df2


# In[6]:


df3 = df2.loc[fitness_df["Rating (Out of 5)"] >= 3.5]
df3


# In[15]:


df4 = df3.loc[:,["Brand Name", "Rating (Out of 5)", "Average Battery Life (in days)"]]


# In[9]:


df4.corr()


# In[14]:


df4.plot()


# In[ ]:





# In[ ]:





# In[ ]:




