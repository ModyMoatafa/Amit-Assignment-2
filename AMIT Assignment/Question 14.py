#!/usr/bin/env python
# coding: utf-8

# In[8]:


org_tuple = [("ahmed",19), ("ali",20), ("mostafa",34) ,("mohamed",15)]
print(org_tuple)


# In[9]:


modified_list = [[x for x , y in org_tuple],[y for x , y in org_tuple]]


# In[10]:


print(modified_list)

