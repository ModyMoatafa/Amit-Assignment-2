#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_tuple = (1,2,3,4,5,6)
print(my_tuple)


# In[5]:


def reverse_tuple(tuples):
    new_tup = tuples[::-1]
    return new_tup


print(reverse_tuple(my_tuple))

