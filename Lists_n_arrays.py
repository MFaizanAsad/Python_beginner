#!/usr/bin/env python
# coding: utf-8

# In[23]:


# A program to understand Lists
# append is a function to add an element 
Cities= ["Karachi","Lahore","Islamabad","Quetta","Peshawar"]
print(Cities)
Cities.append("Bahawalpur")
print(Cities)
Cities.append(47)
print(Cities)
# note here that insert cammand add elements in where ever specifically you want it to be
Cities.insert(2,"Hyderabad")
print(Cities)



# In[41]:


# you can make an empty lists and then later add elements to it
# not here doubel quotation and single are same in python
task_today =[]
task_today= task_today + ["gym","cooking" ,"car cleaning", 'call home'] 
print(task_today)
# you can delete any element from the list by delete cammand
del task_today[2]
print(task_today)
# you can also remove element by remove cammand
task_today.remove("cooking")
print(task_today)


# In[39]:


# taking slices from the lists
# note the syntax for slicing lists
print(Cities[1:5])
x= Cities[2:5]
print(x)
print(x[1:])
print(x[:1])


# In[44]:


# Tuples is same as lists, however small bracker "()" are used instead of "[]"
# Unlike lists, Tuple can not be added or subtracted, unless a whole Tuple is redefine

Alphabets = ("Alpha","Bravo","Charlie")
num_alph = Alphabets +(1,2,4)
#Alphabets = Alphabets + ("Delta")       # check this for error
print(num_alph)
#print(Alphabets)

