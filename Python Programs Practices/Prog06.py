#Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
firstnum = int(input("Enter the base of your number: "))
secondnum = int(input("Enter the exponent of your number: "))

result = firstnum ** secondnum
print(f'The answer is {result}')