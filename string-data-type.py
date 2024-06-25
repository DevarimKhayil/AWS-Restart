myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type "  + str(type(myString)))

#string concatenation
firststring = "water"
secondstring = 'fall'
thirdstring = firststring + secondstring
print(thirdstring)

#working with input strings
name = input("what is your name? ")
print(name)

#Formatting output strings
color = input("what is your favorite color? ")
animal = input("what is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))

