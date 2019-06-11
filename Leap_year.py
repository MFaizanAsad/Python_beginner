# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 02:29:45 2019

@author: Faizan
"""

# program to find out the next Leap, after year getting the value of current year

# grtting input from user
year = int(input("Enter current year to find out the next Leap year: "))
if (year % 4) == 0:           # condition one it divided by 4
    Leap_year = year+4
    print("The next Leap year is {}".format(Leap_year))
        
        
# defining a condition if the year is divible by 4 with zero reminder        
elif ((year+1)% 4)== 0:      
    Leap_year = year+1
    print("The next Leap year is {}".format(Leap_year))
    

# defining a condition if the year is divible by 4 with zero reminder 
elif ((year+2)% 4)== 0:         
    Leap_year = year+2
    print("The next Leap year is {}".format(Leap_year))
    
# defining a condition if the year is divible by 4 with zero reminder     
elif ((year+3)% 4)== 0:          
    Leap_year = year+3
    print("The next Leap year is {}".format(Leap_year))