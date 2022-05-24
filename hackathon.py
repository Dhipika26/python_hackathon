#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd


# In[39]:


import seaborn as sns


# In[40]:


df = pd.read_csv('./ReAdmissionRegistry.csv')
df.head()


# In[41]:


df.dropna(inplace = True)


# In[42]:


sns.pairplot(df)


# In[43]:


# 2nd question:


# In[44]:


df = pd.read_csv('./Patients.csv')


# In[45]:


df


# In[47]:


df.iloc[101:200,1:3]


# In[48]:


#4. Display data by splitting age in 4 quartiles and labeling the quartiles.


# In[49]:


#5 Display full name of pateints who are bron in 1986


# In[50]:


df = pd.read_csv('./Patients.csv')


# In[51]:


df[df["DateOfBirth"].isin(pd.date_range(1/1/1986, 12/1/1986))]


# In[52]:


#6. Creaate a joint plot on expected mortality and expected length of stay.


# In[53]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[54]:


discharges = sns.load_dataset("Discharges")


# In[55]:


sns.jointplot(x = "ExpectedLOS", y = "ExpectedMortality",
              kind = "kde", data = Discharges)


# In[ ]:


#7.Joint plot by taking parameter 'Hue' as EDDisposition.


# In[36]:


import numpy as np, pandas as pd
import seaborn as sns
sns.set(style="white", color_codes=True)
EDVisits = sns.load_dataset("EDVisits")
g = sns.jointplot(x="PatientID", y="Reason for visit", data=EDVisits, hue= 'EDDisposition')


# In[37]:


# 8 Create a bar chart between expected length of stay and primary diagnosis


# In[ ]:


# 9 Get the list of patient ids which are not there in ReadmissionRegistry

