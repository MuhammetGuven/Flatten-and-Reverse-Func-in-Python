#!/usr/bin/env python
# coding: utf-8

# In[13]:


def rv(ar):
    for num in ar:
        if type(num)==type([]):
            num.reverse()
            arr.append(num)
        else: 
            arr.append(num)
    arr.reverse()
arr=[]
arre = [[1, 2], [3, 4], [5, 6, 7]]
rv(arre)
print(arr)


# In[ ]:




