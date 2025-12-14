#!/usr/bin/env python
# coding: utf-8

# In[257]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[258]:


data = pd.read_excel (r"C:\Users\AY\Documents\Incomplete Projects\Sales Analysis with Python\file.xlsx")


# In[259]:


data


# In[260]:


data.info()


# #### Drop Unwanted Column

# In[261]:


data.drop(columns = 'Unnamed: 0', inplace = True)             # to drop the column from the dataframe


# In[262]:


data.head()                                                   # to show top 5 records of the dataframe 


# #### Changing the Column names

# In[263]:


data.loc[0]


# In[264]:


data.columns = data.loc[0]                                   # Changing all the column names     


# In[266]:


data.head()


# #### Drop the Unwanted first Row

# In[265]:


data.drop(0, inplace = True)


# In[269]:


data.info()


# #### Considering the Manager column

# In[270]:


data.Manager


# In[271]:


data.Manager.unique()


# In[232]:


data.Manager.nunique()


# In[276]:


data['Manager'] =data['Manager'].str.strip().str.replace(r'\s+', ' ', regex=True)


# In[277]:


data.head(20)


# In[278]:


data['Manager'].unique()


# In[279]:


data['Manager'].nunique()


# #### Removing the duplicate Records

# In[281]:


data.head()                                     # to show the top 5 records of the dataframe


# In[282]:


data.describe()                               # to show some statistical summary about the dataset


# In[284]:


data.duplicated()


# In[283]:


data[data.duplicated()]                                      # to show all the duplicated records


# In[237]:


data.drop_duplicates(inplace = True)


# In[238]:


data.describe()


# In[239]:


data[data['Order ID'].duplicated()]


# In[240]:


data[data['Order ID'] == 10483]                     # using filtering to show  same records


# In[241]:


data[data['Order ID'] == 10485]                     # using filtering  to show same records


# In[242]:


data[data['Order ID'] == 10486]                    # using filtering  to show same records


# In[ ]:


data.drop(32, inplace = True)


# In[ ]:


data[data['Order ID'] == 10483]


# In[ ]:


data.drop([33,34], inplace = True)                   # to remove one or more rows with the index numbers


# In[ ]:


data[data['Order ID'] == 10485]


# #### Converting the datatype of columns

# In[243]:


data.info()


# In[285]:


data.Quanlity = data.Quantity.astype(float)


# In[245]:


data.info()


# In[286]:


data.Quantity = data.Quantity.round()


# In[287]:


data.Quantity 


# In[ ]:


data.Quantity = data.Quantity.astype(int)


# In[ ]:


data['Quantity']


# In[ ]:


data['Order ID'] = data['Order ID'].astype(int)             # to change the datatype of a column
data['Order ID'] = data['Price'].astype(float)              # to change the datatype of a column


# In[ ]:


data.info()                                                 # to get some basic info about the dataframe 


# In[ ]:


data.Date = pd.to_datetime(data.Date)                       # to comvert the datatype into datetime format


# In[ ]:


data.Date.dtype                                             # to check the datatype of any column


# In[ ]:


data.info()


# In[ ]:


data


# ## Analyzing the Date
# 
# Q.1) Most Preferred Payment Method?

# data.head()

# In[ ]:


data['Payment Method'].unique()                                 # to show the unique value of a column


# In[ ]:


data['Payment Method'].nunique()                                # to show the count of unique values in a column


# In[ ]:


data['Payment Method'].value_counts()


# In[ ]:


data['Payment Method'].value_counts(normalize = True)*100


# In[ ]:


data['Payment Method'].value_counts().plot(kind = 'bar') ;


# #### Q.2) Most Selling Product ?
# 
#   . By Quantity
#   . By Revenue  

# ### By Quantity

# In[ ]:


data.head()


# In[ ]:


data.groupby('Product')['Quantity'].sum()


# In[ ]:


data.groupby('Product')['Quantity'].sum().sort_values(ascending = False)


# In[ ]:


most_quantity = data.groupby('Product')['Quantity'].sum().sort_values(ascending = False)
most_quantity


# In[ ]:


type(most_quantity)


# In[ ]:


most_quantity.reset_index()


# In[ ]:


type(most_quantity)               # to the type of the variable


# In[ ]:


print(type(most_quantity))


# In[ ]:


most_quantity = most_quantity.reset_index()  # to convert  the index of a series into a column to form a dataframe
most_quantity


# In[289]:


type(most_quantity)               # to the type of variable


# In[288]:


import matplotlib.pyplot as plt

plt.figure(figsize = (9,4))
plt.bar(most_quantity['Product'], most_quantity['Quantity'], color = ['red', 'black', 'green', 'yellow', 'cyan'], width=0.4) ;
plt.title("Most Selling Product - By Quantity")
plt.xlabel("Product")
plt.ylabel("Quantity");


# In[290]:


data.head()


# In[291]:


data['Revenue'] = data['Price'] * data['Quantity']               # to create a new column 'Revenue'


# In[292]:


data


# In[293]:


data.groupby('Product')['Revenue'].sum().sort_values(ascending = False)


# In[294]:


most_revnue = data.groupby('Product')['Revenue'].sum().sort_values(ascending = False)
most_revnue


# In[295]:


most_revenue = most_revnue.reset_index()              # to convert the index of a series into a column to form a dataframe
most_revenue


# In[ ]:


plt.figure(figsize = (9,4))
plt.bar(most_revenue['Product'], most_revenue['Revenue'], color = ['red', 'black', 'green', 'yellow', 'cyan'], width=0.3) ;
plt.title("Most Selling Product - By Quantity")
plt.xlabel("Product")
plt.ylabel("Quantity");


# #### 3. Which city had maximum revenue

# #### or

# #### Which Manager earned maximum revenue

# In[297]:


data


# In[298]:


data.City.unique()                                     


# In[299]:


data.City.nunique()                                     # to check the count of unique values of the column 'City'


# In[300]:


data.groupby('City')['Revenue'].sum().sort_values(ascending=False)   # using groupby on 'City' & 'Revenue' column


# In[301]:


data.Manager.unique()


# In[302]:


data.Manager.nunique()                                           # to check the count of unique values of the column 'City'


# In[303]:


data.groupby('Manager')['Revenue'].sum().sort_values(ascending=False)   # using groupby on 'Manager' & 'Revenue' column


# #### 4. Data wise revenue

# In[304]:


data.head()


# In[305]:


data.Date.dtype


# In[306]:


data.info()


# In[307]:


data.plot('Date', 'Revenue', color = 'red', linewidth=2, figsize=(9,4))
plt.title('Date wise Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.show()


# #### Q.5) Average Revenue

# In[309]:


data.head()


# In[308]:


data['Revenue'].mean()


# #### Q.6) Average Revenue of November & December Month

# In[310]:


data.head()


# In[314]:


data['Month'] = data['Date'].dt.month


# In[317]:


import pandas as pd

data['Date'] = pd.to_datetime(data['Date'])

data['Month'] = data['Date'].dt.month


# In[318]:


data


# In[319]:


m11 = data[data['Month'] == 11]
m11


# In[320]:


m11.Revenue.mean()


# In[321]:


m12 = data[data.Month == 12]
m12


# In[322]:


m12.Revenue.mean()                              # to show the mean revenue


# #### Q.7) Standard Deviation of Revenue and Quantity?

# In[323]:


data['Quantity'].std()


# In[324]:


data['Revenue'].std()


# #### Q.8) Variance of Revenue and Qunatity

# In[325]:


data['Quantity'].var()


# In[326]:


data['Revenue'].var()


# #### Q.9) Is revenue Increasing or decreasing over time?

# In[327]:


data.head()


# In[328]:


m11['Revenue'].sum()


# In[329]:


m12 = data[data.Month == 12]                                  # filtering the records with month '12'
m12


# In[331]:


m12.Revenue.sum()


# #### Q.10) Average 'Quantity Sold' & 'Average Revenue' for each product?

# In[332]:


data


# In[335]:


import pandas as pd

print(data.dtypes)

data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce')
data['Revenue'] = pd.to_numeric(data['Revenue'], errors='coerce')

print(data.isnull().sum())

result = data.groupby('Product').agg({'Quantity': 'mean', 'Revenue': 'mean'})
result


# In[ ]:




