
# coding: utf-8

# '''
# Python Homework with Chipotle data
# https://github.com/TheUpshot/chipotle
# '''
# 
# '''
# BASIC LEVEL
# PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
# Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
#       https://docs.python.org/2/library/csv.html
# '''

# In[2]:


import pandas as pd


# In[3]:


# specify that the delimiter is a tab character


# In[4]:


df = pd.read_csv("../2_dataset/chipotle.tsv", sep = "\t")


# '''
# BASIC LEVEL
# PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
# '''

# In[5]:


df.head()


# '''
# INTERMEDIATE LEVEL
# PART 3: Calculate the average price of an order.
# Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
# Hint: Think carefully about the simplest way to do this!
# '''

# In[6]:


df['item_price'] = df['item_price'].map(lambda x: x.lstrip('$'))


# In[7]:


df['item_price'] = df.item_price.astype(float)
df.dtypes


# In[8]:


df.groupby('order_id').item_price.sum().mean()


# '''
# INTERMEDIATE LEVEL
# PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
# Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
# '''

# In[9]:


list_sodas = df[(df.item_name=='Canned Soda') | (df.item_name=='Canned Soft Drink')]
list_sodas


# '''
# ADVANCED LEVEL
# PART 5: Calculate the average number of toppings per burrito.
# Note: Let's ignore the 'quantity' column to simplify this task.
# Hint: Think carefully about the easiest way to count the number of toppings!
# '''
# 

# In[10]:


df_new = df[df['choice_description'].notnull()]
df_new = df_new[df_new['item_name'].str.contains("Burrito")]
Toppings = []
for index, row in df_new.iterrows():
    Toppings.append((len(row['choice_description'].split(','))))

df_new['Toppings'] = Toppings
df_new['Toppings'].mean()


# '''
# ADVANCED LEVEL
# PART 6: Create a dictionary in which the keys represent chip orders and
#   the values represent the total number of orders.
# 
# Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
# 
# Note: Please take the 'quantity' column into account!
# 
# Optional: Learn how to use 'defaultdict' to simplify your code.
# '''

# In[145]:


df_chips = df[df['item_name'].str.contains("Chips")]
df_chips = df_chips[['item_name', 'quantity']].groupby('item_name').sum()
df_chips = df_chips.reset_index()
df_chips
chips = list(df_chips.set_index('item_name').to_dict().values()).pop()
chips


# '''
# BONUS: Think of a question about this data that interests you, and then answer it!
# '''
