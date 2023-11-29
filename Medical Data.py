#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv(r'/Users/user/Documents/FreeCodeCamp/medical_examination.csv')


# In[5]:


df.head()


# In[6]:


#Import plotting libraries
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a figure with 2x5 subplots for the different panels
fig, axes = plt.subplots(2, 5, figsize=(20, 8))

# List of variables to plot
variables = ['cholesterol', 'gluc', 'smoke', 'alco', 'active']

# Generate plots for cardio=0 and cardio=1
for i, variable in enumerate(variables):
    sns.countplot(x=variable, data=df[df['cardio'] == 0], ax=axes[0,i]).set_title(f'{variable} when cardio=0')
    sns.countplot(x=variable, data=df[df['cardio'] == 1], ax=axes[1,i]).set_title(f'{variable} when cardio=1')

# Adjust the layout
plt.tight_layout()
plt.show()


# In[8]:


# Calculate BMI and add 'overweight' column (1 if overweight, 0 if not)
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize the 'cholesterol' and 'gluc' columns
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Check the first few rows to verify changes
df.head()


# In[9]:


# Melt the data into long format for the variables of interest
df_long = pd.melt(df, 
                  id_vars=['cardio'], 
                  value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# Create the catplot
catplot = sns.catplot(x='variable', hue='value', col='cardio', data=df_long, kind='count', height=6, aspect=1)

# Set the axis labels and titles
catplot.set_axis_labels("Variable", "Total")
catplot.set_titles("Cardio = {col_name}")

# Adjust the layout
catplot.fig.tight_layout()

# Show the plot
plt.show()


# In[10]:


# Clean the data based on the specified criteria
df_clean = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

# Display the shape of the original and cleaned dataframes to show how many rows were filtered
original_shape = df.shape
cleaned_shape = df_clean.shape

original_shape, cleaned_shape


# In[12]:


# Calculate the correlation matrix
corr = df_clean.corr()


# In[13]:


# Create a mask to hide the upper triangle of the correlation matrix
mask = np.triu(np.ones_like(corr, dtype=bool))


# In[14]:


# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))


# In[15]:


# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)


# In[16]:


# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




