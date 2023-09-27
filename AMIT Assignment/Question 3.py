#!/usr/bin/env python
# coding: utf-8

# In[4]:


my_list=[1,2,3]
print(my_list)


# In[5]:


def multiply_list(list):
    result=1
    for i in list:
        result=result*i
    return result


# In[6]:


print(multiply_list(my_list))

