#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project with Python 

# ## (A part of Big Data Analysis)

# ***

# # Cars Dataset
# Here i hane taken the data of different cars with their specifications.
# 
# This data is available as a CSV file.( i have downloaded this csv data file from google).Here i am going to analyze this data set using the Pandas DataFrame.

# ----

# In[1]:


import pandas as pd


# In[2]:


car  = pd.read_csv(r"C:\Users\ninad\Downloads\2. Cars Data1.csv")


# In[3]:


car.head()


# In[4]:


car.shape


# In[ ]:





# 1) Instruction ( For Data Cleaning ) 
# - Find all Null Value in the dataset. If there is any null value in any column, then fill it with the mean of that column. 

# In[5]:


car.isnull().sum()


# In[6]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True)


# ----

# 2) Question ( Based on Value Counts )
# - Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data
# ?

# In[7]:


car.head(2)


# In[8]:


car['Make'].value_counts()


# ----

# 3) Instruction ( Filtering )
# - Show all the records where Origin is Asia or Europe.

# In[9]:


car.head(2)


# In[10]:


car[car['Origin'].isin(['Asia', 'Europe'])]


# In[11]:


car['Origin'].value_counts()


# In[12]:


158 + 123


# ----

# 4) Instruction ( Removing unwanted records )
# - Remove all the records (rows) where Weight is above 4000.

# In[13]:


car.head(2)


# In[14]:


car[~(car['Weight'] > 4000)]


# In[15]:


428 - 103


# -----

# 5) Instruction ( Applying function on a column )
# - Increase all the values of 'MPG_City' column by 3.

# In[16]:


car.head(2)


# In[17]:


car[car['Horsepower']>200]


# In[18]:


car['MPG_City'] =  car['MPG_City'].apply(lambda x:x+3)


# In[19]:


car


# ----

# ----

# -----

# ----
