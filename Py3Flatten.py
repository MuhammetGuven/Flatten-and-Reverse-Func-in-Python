#!/usr/bin/env python
# coding: utf-8

# In[11]:


def Flat(ar):
    for num in ar:
        if type(num)==type([]):
            Flat(num)
        else: 
            arz.append(num)
arz=[]
arr = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
Flat(arr)
print(arz)



# In[ ]:




