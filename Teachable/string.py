# Define the string "FUTURA" into a variable and string "LAB" into another variable
str1 = "FUTURA"
str2 = "LAB"

# print the first and last character of the first string
print(str1[0], str1[-1])

# concatenate two strings into new string
str3 = str1 + str2
print(str3)

# find length of new string
print(len(str3))

# print UTURA LA of the string
print(str1[1:6], str2[:2])

# print first 3 characters of the string
print(str1[0:3])

# print the reversal of the string[ using slicing]
print(str3[::-1])

# Delete the first string
del str1

# change into lower case and uppercase
# replace every ‘a’ with "*"
str4 = "Python is a programming language that lets you work quickly and integrate systems more effectively"
print(str4.upper())
print(str4.lower())
print(str4.replace("a", "*"))

# check if there is 'you' in the string, then print “FOUND”
if "you" in str4:
    print("FOUND")
