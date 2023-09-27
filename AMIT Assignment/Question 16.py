#!/usr/bin/env python
# coding: utf-8

# In[4]:


def convert(tup , dic):
    for x,y in tup:
        dic.setdefault(x, []).append(y)
    return dic
    


# In[5]:


tuples = [("ahmed",20) , ("ali",24)]
dicts={}
print(convert(tuples, dicts))

