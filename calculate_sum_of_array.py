#The following code makes an array 
x = [1]
i=1
# defiens a variable that adds up by 1 and append in x through while loop
a= 1
n = int(input("enter a value between 1 to 1000 to create an array with +1 increment = "))
while i < n:
    i += 1
    a += 1
    x.append(a)
print(x)

#The following code sum all the numbers of the array
def find_sum(x):
     total = 0
     for i in x:
         total += i
     return total 
     print(total)        
# if the program does'nt show the sum in spyder try it in jupyter
find_sum(x)

   
