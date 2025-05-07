#Input and Loops 
#Judah Thornton
#date: 7/05/25
#Verstion 1

#ask the user a question and store thier answer in a variable
#ask the user for thier name and store it
name = input("Kia ora, what is your name? ")

#ask user for 2 numbers then add them together
num1 = int(input("what is your first number? "))
num2 = int (input('what is youre second number? '))
print(f'you entered your first number as {num1}')
print(f'you entered your second number as {num2}')

#adding them together
sum = num1 + num2
print(f'hi {name} this is your first number added together with youre second number, {sum}')


#check that the name was stored correctly
print(name)
#to comment out code use ctrl + /