#Create a program that ask user to input 10 numbers. Print how many are odd numbers.
oddnum = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        oddnum += 1
print(f"There are {oddnum} Odd Numbers")
