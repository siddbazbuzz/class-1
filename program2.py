"""write a program in python to input any two numbers, 
namely "num1"and "num2" from terminal and find
first number being num1
second number being num2
=>sum of two numbers
=>subtraction of two numbers
=>division of two numbers
=>multiplication of two numbers
=>power of two numbers
=>floor division""" 
num1=int(input("enter first number:\n"))
num2=int(input("enter second number:\n"))
sum=num1+num2
sub=num1-num2
mul=num1*num2 
div=num1/num2 
pow=num1**num2
floor=num1//num2
print(f"the sum of {num1} and {num2} is {sum}")
print(f"the subtraction of {num1} and {num2} is {sub}")
print(f"the multiply of {num1} and {num2} is {mul}")
print(f"the division of {num1} and {num2} is {div}")
print(f"the power of {num1} and {num2} is {pow}")
print(f"the floor of {num1} and {num2} is {floor}")
