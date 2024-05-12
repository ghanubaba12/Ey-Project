#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd


# In[80]:


df=pd.read_excel(r"C:\MBA in Business Analytics\r programing\Project1_Pharma Dataset.xlsx")


# In[81]:


df


# In[82]:


df.info()


# In[83]:


df.describe()


# In[84]:


df.groupby("Date")[["Sales","Profit"]].sum()


# In[85]:


df[(df['Date']>='2022-1-1')&(df['Date']<='2022-12-30')].groupby("Date")[["Sales","Profit"]].sum()


# In[86]:


df['Year']=df['Date'].dt.year
df_2022 = df[df['Year']==2022]
monthly_sales_profit_2022=df_2022.groupby(['Year',df_2022['Date'].dt.month])[["Sales","Profit"]].sum()
print(monthly_sales_profit_2022)


# In[87]:


df


# In[88]:


#•	Which are the Top 20 drugs by sales of 2022


# In[89]:


#report=df[(df["Date"]>='2022-1-1') & df(df["Date"]


# In[90]:


df.columns


# In[91]:


# report=df[(df['Date']>='2022-1-1') & (df['Date']<='2022-12-30')].groupby('Drug Name')['Sales'].sum
# df=pd.DataFrame(report)
# df


# In[92]:


report = df[(df['Date'] >= '2022-01-01') & (df['Date'] <= '2022-12-30')].groupby('Drug Name')['Sales'].sum()
# df = pd.DataFrame(report)


# In[ ]:





# In[93]:


df_2022=df[(df['Year']==2021) | (df['Year']==2022)]
monthly_sales_profit_2022=df_2022.groupby(df['Year'])[['Sales']].sum()
monthly_sales_profit_2022.plot(kind='bar')


# In[94]:


df.groupby('Drug Name')['Quantity'].count().plot(kind='hist')


# In[97]:


df.columns


# In[99]:


# .show Region and Market segment wise sales percentage.
df.groupby(['Dispensed Region','Market Segment'])[['Sales']].sum()/df.Sales.sum()*100


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




