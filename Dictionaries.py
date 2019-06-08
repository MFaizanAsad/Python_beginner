#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Ditionaries are used to store data for later use
# curly brakets are used and information is saved in pairs seperated by colon
# left side of the colon is called key, used to call infromation
# program to wrtie dictionary and calling it

user= {"name":"Muhammad Faizan Asad","city":"Espoo", "country":"Finland", "Degree":"Masters in Process Systems Engineering"}
calling = user["Degree"]
print(calling)


# In[36]:


# Its good to break dictionary while creating it, if there are different key values

things_to_remember = {
 0: "the lowest number",
 "a dozen": 12,
 "snake eyes": "a pair of ones",
 13: "a baker's dozen",
}

spooky = things_to_remember["snake eyes"]
print(spooky)


# In[38]:


# Deleting information from dictionaries and lists
List = ["apple","dog", "biryani"]
# the below cammand will delete first element form the list
del List[0]
print(List)
dictionary = {"fruit":"apple", "animal":"dog","food":"biryani"}
# the below cammand will delete the key "fruit" and its information "apple" altogether
del dictionary["fruit"]
print(dictionary)


# In[57]:


#Looping through dictionaries, the code below will print the values in dicitonary

spell_numbers = {1:"one",2:"two",3:"three",4:"four",5:"five"}
# for x in spell_numbers.values():
#     print(x)
    
# # The code below will print the keys of ditionary
# for x in spell_numbers.keys():
#     print(x)
    
# The code below will loop through keys and values and print them together
for keys, values in spell_numbers.items():
    print("The spelling of "+ str(keys) + "  is  " + values)

