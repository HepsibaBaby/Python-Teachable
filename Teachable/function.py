#Find the reverse of a number
def reverse(n):
    rev = 0
    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = int(n / 10)
    return rev
x = int(input("Enter a number:"))
result = reverse(x)
print("Reverse is:", result)

#Create a recursive function to find the sum of numbers
def sum_of_digit(n):
    if n< 10:
        return n
    else:
        return n%10 + sum_of_digit(n/10)
number = int(input("Enter number: "))  # Read number
digit_sum = sum_of_digit(number)  # Function call
print("Sum of digit of number %d is %d." % (number, digit_sum))

#Define a function that accepts 2 values and return its sum,subtraction and multiplication
def add_num(a,b):
    sum=a+b;
    return sum;
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The sum is",add_num(num1,num2))

#Define a function which counts vowels and consonant in a word.
vcount = 0;
ccount = 0;
my_str = str(input("Enter a word: "));

# Converting entire string to lower case to reduce the comparisons
my_str = my_str.lower();
for i in range(0, len(my_str)):
    # Checks whether a character is a vowel
    if my_str[i] in ('a', "e", "i", "o", "u"):
        vcount = vcount + 1;
    elif (my_str[i] >= 'a' and my_str[i] <= 'z'):
        ccount = ccount + 1;
print("Total number of vowel and consonant are");
print(vcount);
print(ccount);

#Define a function that accepts radius and returns the area of a circle.
def circle_area(Radius):
    area = Radius ** 2 * 3.14
    return area

Radius = float(input("Please enter the radius of a circle: "))
print(" The area of the given circle is: ", circle_area(Radius))






