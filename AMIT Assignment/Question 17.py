#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [(10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
print(my_list)


# In[2]:


print([t[:-1] + (100,) for t in my_list])


# In[ ]:




