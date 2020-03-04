#program calculates takes 100 random numbers between 1 and 100, and calculates the number of even and odd numbers

import random

counter=0
odd_number=0
even_number=0

while counter!=100:
    number=random.randint(1,100)
    new_number=number%2
    if new_number==1:
        odd_number+=1
    else:
        even_number+=1
    counter+=1    

    
     
print('The number of odd numbers is',odd_number)
print('The number of even numbers is ',even_number)
