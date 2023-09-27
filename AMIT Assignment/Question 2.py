#!/usr/bin/env python
# coding: utf-8

# In[3]:


my_list=[1,2,3,4,5]
print(my_list)


# In[4]:


def sum_list(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum


# In[6]:


print(sum_list(my_list))


# In[ ]:




