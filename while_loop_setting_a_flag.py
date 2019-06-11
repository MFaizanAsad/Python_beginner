"""
Created on Tue Jun 11 21:46:35 2019

@author: Faizan
"""
capital_cities =["Helsinki","Islamabad","Delhi","Dhaka","Moscow","Washinton"]

# A program using while loop with and setting a flag
# The first two lines of the codes setting the flag

keep_looping = True
while keep_looping == True:
    user_input = input("Enter a name of a capital city or,q to quit:")
    if user_input != "q":
        for a_capital_city in capital_cities:
            if user_input == a_capital_city:
                print("it's one of the capital city")
                break
    else:
        Keep_looping = False
    
