#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Input

apparentMagnitude = float(input("Enter the star's apparent magnitude (int/float)"))
absoluteMagnitude = float(input("Enter the star's absolute magnitude (int/float)"))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d_ly = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
print(f"Based on the inputs the star is approximately {d_ly} ly away from us")


# In[ ]:




