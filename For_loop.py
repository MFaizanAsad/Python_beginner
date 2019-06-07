#!/usr/bin/env python
# coding: utf-8

# In[65]:


# For loop example, its a simple program to understand loop logic and syntax
# The program is using a fuction that identify first 4 letters 

def identifier(letters):
    letters = input("enter a letter from a,b,c,d  =") 
    alphabets = ["a","b","c","d"]
    #note the syntax we have use a variable "x" here to compare
    for x in alphabets:
        #the required output is compare with the variable "x" from For_loop statement
        if letters == x: 
            print("the input letter is =" + " " + letters)
        #condition that checks for invalid input
        elif letters!= "a" and letters !="b" and letters != "c" and letters !="d" :
            print("invalid input, please enter again")
            # returning function in case of invalid input
            return identifier(letters)
# Calling function         
identifier(letters)
    


# In[ ]:


# A program, representing "Nested_for_loop"
# Explanation first for loop is started then the next inner loop is run for all values of last name and then it will move to 
#outer shell

first_names = ["BlueRay ", "Upchuck ", "Lojack ","Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + "_" + a_last_name)
print(full_names)

