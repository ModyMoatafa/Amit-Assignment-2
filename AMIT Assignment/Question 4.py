#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_list=[1,2,3,4]
print(my_list)


# In[3]:


def get_smallest(list):
    min=list[0]
    for i in list:
        if i < min:
            min= i 
    return min


# In[4]:


print(get_smallest(my_list))

