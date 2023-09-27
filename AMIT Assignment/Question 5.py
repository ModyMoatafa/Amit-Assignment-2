#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list=[1,2,3,4]
print(my_list)


# In[2]:


def get_largest(list):
    max=list[0]
    for i in list:
        if i > max:
            max= i 
    return max


# In[4]:


print(get_largest(my_list))

