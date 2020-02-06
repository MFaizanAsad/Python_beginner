#!/usr/bin/env python
# coding: utf-8
####

# In[13]:


# saving ditionaries in a list

customers = [
    {    
      "customer id": 0,
      "first name":"John",
      "last name": "Ogden",
      "address": "301 Arbor Rd.",     
 },
 {
     "customer id": 1,
     "first name":"Ann",
     "last name": "Sattermyer",
     "address": "PO Box 1145",
 },
 {
    "customer id": 2,
    "first name":"Jill",
    "last name": "Somers",
    "address": "3 Main St.",
 },
 ]
#print(customers)
# to get the information from a set of dictionaries, it is good to give customer ID same as dictionary index
# e.g. to find the address of customer Id 2, we use the follwing code

dictionary_to_look_into = customers[2]
customer_address = dictionary_to_look_into["address"]
print(customer_address)


# In[34]:


# we have a list of customers, incase we have a new customer then we use append to add a dictionary in the list



customers = [
    {    
      "customer id": 0,
      "first name":"John",
      "last name": "Ogden",
      "address": "301 Arbor Rd.",     
 },
 {
     "customer id": 1,
     "first name":"Ann",
     "last name": "Sattermyer",
     "address": "PO Box 1145",
 },
 {
    "customer id": 2,
    "first name":"Jill",
    "last name": "Somers",
    "address": "3 Main St.",
 },
 ]

# if we know the total number of dictionaries in "customers-list" we can know the next customer no
# because the first dictionary in customer starts with 0 index

new_customer_id= len(customers)
new_first_name = str(input("Please enter the name of new customer= "))
new_last_name = str(input("Please enter the last name of customer= "))
new_address = str(input("Please enter the address of new customer= "))
# we can define a new dictionary like this:
add_new_customer = {    
"customer id": new_customer_id,
"first name": new_first_name,
"last name": new_last_name,
"address": new_address,
 }
customers.append(add_new_customer)
print(customers)




# In[ ]:




