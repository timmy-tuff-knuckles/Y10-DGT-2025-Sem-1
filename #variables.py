#demonstrate how variables are created
#variables 
#author: Judah Thornton
#Date: 11/4 2025
#version 1.0

#diffrent types of variables
#store a number
my_number = 80 # assigning 80 to my_number (variable)
print(my_number)

my_number2 = 7 # i have reassigned the value of a variable
print(my_number2)

Name_1 = "Judah"
print(Name_1)


my_number = Name_1
print(my_number)  #Dont assign values to bariables that dont make sense for its name

num_1 = 5
num_2 = 17

''' do caculations with variables and store the result in 
 annother variable. i can now
 press enter
 as
 many times
 as i want'''

sum = 5+17 #this is no good practice
print(sum)

#better way
sum1 = num_1 + num_2
print(sum)


sum_string1 = "17" 
sum_string2 = "5"

sum = sum_string1 + sum_string2
print(sum)
print(sum1)

print(f"my calculation for {sum_string1} + {sum_string2} = {sum1}")