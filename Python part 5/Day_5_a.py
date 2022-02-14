#!/usr/bin/env python
# coding: utf-8

# In[3]:


def BMICalc(weight, height):
    BMI = weight/ height**2
    if(BMI < 18.5):
        return "Under"
    elif(BMI < 25.0):
        return "Normal"
    elif(BMI < 30.0):
        return "Over"
    else:
        return "Obese"
print(BMICalc(80, 1.73))
print(BMICalc(55, 1.58))
print(BMICalc(49, 1.91))


# In[ ]:




