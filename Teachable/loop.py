# Find factorial of a given number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print(" Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

# Write a program to print the following number pattern using a loop
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

# Print first ten natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

#Print list in a reverse order using loop
my_list = [1,2,3,4,5,6]
for i in range(len(my_list) - 1,-1,-1) :
    print(my_list[i])

#Write a program that appends the square of each number to a new list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)
