#!/usr/bin/env python
# coding: utf-8

# In[8]:


string = input("Enter the string :\n")
given_list=list(string)
print(given_list)


# In[ ]:





# In[4]:


def count_list(list):
    c = 0
    for i in list:
        c=c+1
    return c    


# In[9]:


print(count_list(given_list))

