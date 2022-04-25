#create a list with name of fruit with size 4
fruit = ["apple","orange","grape","strawberry"]
print(fruit)

#create a list with name of vegetables with size of 3
veg = ["tomato","carrot","potato"]
print(veg)

#insert "cat" in the fruit list to the index 2
fruit.insert(2,"cat")
print(fruit)

#append the fruit to vegetable list
veg.append(fruit)
print(veg)

#ascending order of fruit list
fruit.sort()
print(fruit)

#descending order of vegetable list
veg1 = ["tomato","carrot","potato"]
veg1.sort(reverse=True)
print(veg1)

#make a copy of fruit list
fruit.copy()
print(fruit)

#reverse the vegetable list
veg.reverse()
print(veg)

