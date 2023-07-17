#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


inventory_data = {
    'Item Number': ['064-01-1347', '064-01-1361', '064-01-1375', '064-01-1385', '064-01-1399', '064-01-1409',
                    '064-01-1423', '064-01-1430', '064-01-1437', '064-01-1444', '064-01-1348', '064-01-1362',
                    '064-01-1376', '064-01-1386', '064-01-1400', '064-01-1410', '064-01-1424', '064-01-1431'],
    'Date': ['6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023',
             '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023', '6/17/2023',
             '6/17/2023', '6/17/2023'],
    'Inventory': [3561, 4035, 2684, 5136, 6399, 10135, 3309, 2451, 2056, 5449, 3028, 3881, 2, 2719, 6879, 5445, 1452, 2020]
}

inventory_df = pd.DataFrame(inventory_data)


# In[3]:


new_inventory_data = {
    'Item Number': ['064-13-0002', '064-13-0338', '064-13-0340', '064-13-0353', '064-13-0416', '064-13-0010',
                    '064-15-5738', '064-15-5777', '064-15-6305', '064-15-7068', '064-15-7174', '064-18-2305',
                    '064-18-2358'],
    'Inventory Receive date': ['7/7/2023', '7/7/2023', '7/7/2023', '7/7/2023', '7/7/2023', '7/9/2023', '7/9/2023',
                               '7/9/2023', '7/9/2023', '7/9/2023', '7/9/2023', '7/21/2023', '7/21/2023'],
    'Item Qty': [700, 1700, 1000, 1900, 1000, 3140, 5976, 4428, 7352, 9064, 6276, 1134, 1620]
}

new_inventory_df = pd.DataFrame(new_inventory_data)


# In[4]:


merged_df = pd.concat([inventory_df, new_inventory_df], ignore_index=True)

inventory_table = merged_df.pivot(index='Item Number', columns='Inventory Receive date', values='Inventory')

print(inventory_table)

# Create a bar chart showing total monthly inventory levels
inventory_table_sum = inventory_table.sum(axis=1)
monthly_inventory_chart = inventory_table_sum.plot(kind='bar')
plt.xlabel('Item Number')
plt.ylabel('Total Inventory')
plt.title('Total Monthly Inventory Levels')

# Display the bar chart
plt.show()


# In[ ]:




