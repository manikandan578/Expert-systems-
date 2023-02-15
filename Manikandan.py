#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to the plant watering advice system")
soil_moisture = float(input("Please enter the soil moisture level of the plant (as a percentage): "))

if soil_moisture < 0 or soil_moisture > 100:
    print("Invalid soil moisture level.")
elif soil_moisture < 30:
    print("The soil is too dry. Water the plant.")
elif soil_moisture >= 30 and soil_moisture <= 60:
    print("The soil moisture level is good. No need to water the plant.")
else:
    print("The soil is too wet. Do not water the plant.")


# In[ ]:




