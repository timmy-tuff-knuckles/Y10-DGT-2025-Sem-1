#Input and Loops 
#Judah Thornton
#date: 9/05/25
#Verstion 2

#ask the user a question and store thier answer in a variable
#ask the user for thier name and store it

name = input("Kia ora, what is your name? ")

#print() #this adds a line break
#\n so does this

#check that the name was stored correctly
print(f'\n nice to meet you, {name}')
#to comment out code use ctrl + /

#ask user for 2 numbers then add them together
num1 = int(input("\n what is your first number? "))
num2 = int (input('\n what is youre second number? '))
print(f'\n you entered your first number as {num1}')
print(f'\n you entered your second number as {num2}')

#adding them together
sum = num1 + num2
# numbers added

print(f'\n hi {name} this is your first number added together with youre second number, {sum}')

multiply = num1*num2 
# multiplied numbers

print(f'\n hi {name} this is your first number multiplied together with youre second number, {multiply}')
#check that the name was stored correctly
print(name)
#to comment out code use ctrl + /