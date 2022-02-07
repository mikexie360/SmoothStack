#!/usr/bin/env python
# coding: utf-8

# Coding Exercise 2:

# In[2]:


print(50+50)
print(100-10)


# In[8]:


print(30+6)
print(6^6)
print(6**6)
print(6+6+6+6+6+6)


# In[6]:


6^6


# In[9]:


print("Hello World")


# In[10]:


print("Hello World : 10")


# p = debt
# r = interst rate
# every month p increased by p * (r/12) and decreases by 10000

# In[24]:


import math
p = 800000
r = 6
l = 103

payment = 0

r = r/100
r = r/12

m = (p*r*((1+r)**l))/(((1+r)**l)-1)
print(math.ceil(m))


# In[ ]:




