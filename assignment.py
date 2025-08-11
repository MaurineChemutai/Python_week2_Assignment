#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Create an empty list
my_list=[]
#Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert the value 15 at the second position of the list
my_list.insert(1,15)
#Extend my_list
my_list.extend([50,60,70])
print("My list after extending:",my_list)
#Remove the last element from my_list
my_list.pop()
print("My list after removing the last element:", my_list)
#Sort my_list in ascending order
my_list.sort()
print("My list after sorting:", my_list)
#Find and print the index of the value 30
index_of_30=my_list.index(30)
print("The index of the value 30:", index_of_30)


# In[ ]:




